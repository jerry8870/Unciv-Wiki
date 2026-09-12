#!/usr/bin/env python3
"""Check every content route in the built site; expectations follow the content set."""
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
config = json.loads((ROOT / 'site.config.json').read_text())
origin = config['site'] + config['base']

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags=[]; self.ids=[]; self.h1=0; self.jsonld=[]; self.script=None
        self.text=[]; self.ignore_text=False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs); self.tags.append((tag,attrs))
        if tag in ('script','style'): self.ignore_text=True
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag=='h1': self.h1+=1
        if tag=='script' and attrs.get('type')=='application/ld+json': self.script=''
    def handle_data(self,data):
        if not self.ignore_text: self.text.append(data)
        if self.script is not None: self.script+=data
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.ignore_text=False
        if tag=='script' and self.script is not None:
            self.jsonld.append(json.loads(self.script)); self.script=None
    def attr(self,tag,key,value,out):
        return [a.get(out) for t,a in self.tags if t==tag and a.get(key)==value]

pages={}; expected={}; errors=[]
for source in (ROOT/'src/content/docs').rglob('*'):
    if source.suffix not in ('.md','.mdx'): continue
    rel=source.relative_to(ROOT/'src/content/docs').as_posix()
    route=rel.rsplit('/',1)[0]+'/' if '/' in rel else ''
    meta=json.loads(source.read_text().split('---',2)[1])
    url=origin+route; expected[url]=meta
    file=ROOT/'dist'/route/'index.html'
    if not file.exists(): errors.append(f'Missing route: {route}'); continue
    pages[url]=Page(file.read_text())
allowed={url for url,data in expected.items() if data.get('indexable',True)}
excluded=set(expected)-allowed

def check_ref(source,ref,anchor=True):
    if not ref or ref.startswith(('mailto:','tel:','data:','javascript:')): return
    target=urlparse(urljoin(source,ref))
    if target.netloc!=urlparse(config['site']).netloc: return
    if not target.path.startswith(config['base']): errors.append(f'Outside base: {source} -> {ref}'); return
    target_url=target._replace(fragment='',query='').geturl()
    path=unquote(target.path[len(config['base']):])
    file=ROOT/'dist'/path
    if target_url in pages:
        if anchor and target.fragment and unquote(target.fragment) not in pages[target_url].ids: errors.append(f'Missing anchor: {source} -> {ref}')
    elif not file.is_file(): errors.append(f'Broken local target: {source} -> {ref}')

for url,page in pages.items():
    meta=expected[url]
    reader_text=' '.join(page.text + [attrs.get('content','') for tag,attrs in page.tags if tag=='meta'])
    if re.search(r'4\.21\.20|(?<!\d)1293(?!\d)|\bV3\b|内容基线|Content baseline|版本|\bversions?\b', reader_text, re.I):
        errors.append(f'Game version wording in reader content or metadata: {url}')
    if page.h1!=1: errors.append(f'H1 count {page.h1}: {url}')
    if page.attr('link','rel','canonical','href')!=[url]: errors.append(f'Canonical mismatch: {url}')
    if page.attr('meta','name','description','content')!=[meta['description']]: errors.append(f'Description mismatch: {url}')
    if page.attr('meta','name','wiki:lastmod','content')!=[meta['lastUpdated']]: errors.append(f'lastmod mismatch: {url}')
    duplicates=[k for k,v in Counter(page.ids).items() if v>1]
    if duplicates: errors.append(f'Duplicate IDs {duplicates}: {url}')
    noindex=any('noindex' in value for value in page.attr('meta','name','robots','content'))
    if noindex!=(url in excluded): errors.append(f'Index policy mismatch: {url}')
    pagefind=any('data-pagefind-body' in attrs for _,attrs in page.tags)
    if pagefind!=(url in allowed): errors.append(f'Pagefind policy mismatch: {url}')
    for tag,attrs in page.tags:
        if tag=='a': check_ref(url,attrs.get('href'))
        if tag in ['img','script'] and attrs.get('src'): check_ref(url,attrs['src'],False)
        if tag=='img' and not attrs.get('alt'): errors.append(f'Missing image alt: {url}')
        if tag=='link' and attrs.get('rel')=='alternate':
            check_ref(url,attrs.get('href'))
            if url in excluded or attrs.get('href') in excluded: errors.append(f'Excluded alternate: {url}')
        if tag=='a' and attrs.get('href')==config['testflight'] and not attrs.get('id','').startswith('tf-'): errors.append(f'Missing stable TestFlight ID: {url}')
    for ld in page.jsonld:
        if ld.get('potentialAction',{}).get('@type')=='SearchAction': errors.append(f'Obsolete SearchAction: {url}')
        if ld.get('@type')=='BreadcrumbList':
            for item in ld['itemListElement']: check_ref(url,item['item'])
        if ld.get('@type')=='Article':
            if not ld.get('datePublished') or not ld.get('dateModified'): errors.append(f'Missing Article dates: {url}')
    if meta.get('article') and not any(x.get('@type')=='Article' for x in page.jsonld): errors.append(f'Missing Article: {url}')
    if url in allowed and not any(x.get('@type')=='BreadcrumbList' for x in page.jsonld): errors.append(f'Missing breadcrumbs: {url}')
    other=origin+(url[len(origin):].removeprefix('zh/') if url.startswith(origin+'zh/') else 'zh/'+url[len(origin):])
    if other not in expected: errors.append(f'Missing language counterpart: {url}')
    # Main navigation must not contain excluded routes; explicit return links in body are permitted.
    html=(ROOT/'dist'/url[len(origin):]/'index.html').read_text()
    for nav in re.findall(r'<nav\b[^>]*aria-label="(?:Main|主)[^"]*"[\s\S]*?</nav>',html):
        for ex in excluded:
            if 'href="'+urlparse(ex).path+'"' in nav: errors.append(f'Excluded navigation: {url}')
for lang in ['', 'zh/']:
    page=pages[origin+lang+'achievements/']
    found={i for i in page.ids if re.fullmatch(r'N\d{2}',i)}
    if found!={f'N{i:02}' for i in range(1,41)}: errors.append('Achievement anchor mismatch: '+lang)
    for section in ['units','civilizations','buildings','technologies']:
        if not lang:
            html=(ROOT/f'dist/database/{section}/index.html').read_text()
            main=re.search(r'<main\b[\s\S]*?</main>',html)[0]
            # Exclude the language-picker UI, which is outside main.
            main=re.sub(r'<script\b[\s\S]*?</script>', '', main)
            if re.search(r'[\u4e00-\u9fff]',main): errors.append('Chinese in English data table: '+section)
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
xml=ET.parse(ROOT/'dist/sitemap-0.xml'); sm={}
for node in xml.findall('s:url',ns):
    url=node.findtext('s:loc',namespaces=ns);sm[url]=node
    if node.findtext('s:lastmod',namespaces=ns)!=expected.get(url,{}).get('lastUpdated'): errors.append('Sitemap date mismatch: '+url)
    links={a.attrib['hreflang']:a.attrib['href'] for a in node.findall('x:link',ns)}
    if set(links)!={'en','zh-CN','x-default'}: errors.append('Sitemap languages mismatch: '+url)
    if any(v not in allowed for v in links.values()): errors.append('Invalid sitemap alternate: '+url)
    if links.get('x-default')!=links.get('en'): errors.append('Invalid x-default: '+url)
if set(sm)!=allowed: errors.append(f'Sitemap set differs: missing {allowed-set(sm)}, extra {set(sm)-allowed}')
summary={'contentPages':len(expected),'indexablePages':len(allowed),'excludedPages':len(excluded),'sitemapPages':len(sm),'errors':errors}
print(json.dumps(summary,ensure_ascii=False,indent=2))
if '--report' in sys.argv:
    report=ROOT/'docs/validation/site-check.json';report.parent.mkdir(parents=True,exist_ok=True);report.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
raise SystemExit(bool(errors))
