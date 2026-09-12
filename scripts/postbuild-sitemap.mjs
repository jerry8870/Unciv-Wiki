#!/usr/bin/env node
// The rendered index policy is authoritative for sitemap URLs, alternates and lastmod.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';
import config from '../site.config.json' with { type: 'json' };

const sitemapPath = resolve('dist/sitemap-0.xml');
let xml = readFileSync(sitemapPath, 'utf8');
const records = [...xml.matchAll(/<url>([\s\S]*?)<\/url>/g)].map(([full, inner]) => {
  const loc = inner.match(/<loc>(.*?)<\/loc>/)[1];
  const path = new URL(loc).pathname.slice(config.base.length);
  const file = resolve('dist', path, 'index.html');
  if (!existsSync(file)) throw new Error('Missing sitemap page: ' + loc);
  const html = readFileSync(file, 'utf8');
  const excluded = /<meta\b[^>]*name="robots"[^>]*content="[^"]*noindex/.test(html);
  const lastmod = html.match(/<meta\b[^>]*name="wiki:lastmod"[^>]*content="([^"]+)"/)?.[1];
  if (!excluded && !lastmod) throw new Error('Missing content update date: ' + loc);
  return { full, inner, loc, excluded, lastmod };
});
const allowed = new Set(records.filter((r) => !r.excluded).map((r) => r.loc));
for (const record of records) {
  if (record.excluded) { xml = xml.replace(record.full, ''); continue; }
  let inner = record.inner.replace(/<lastmod>.*?<\/lastmod>/g, '').replace(/<xhtml:link\b[^>]*\/>/g, (link) => allowed.has(link.match(/href="([^"]+)"/)?.[1]) ? link : '');
  const en = inner.match(/<xhtml:link[^>]*hreflang="en"[^>]*href="([^"]+)"/)?.[1];
  if (en && !inner.includes('hreflang="x-default"')) inner += `<xhtml:link rel="alternate" hreflang="x-default" href="${en}"/>`;
  inner += `<lastmod>${record.lastmod}</lastmod>`;
  xml = xml.replace(record.full, `<url>${inner}</url>`);
}
writeFileSync(sitemapPath, xml);
console.log(`[sitemap] ${allowed.size} indexable URLs; ${records.length - allowed.size} excluded; stable content dates.`);
