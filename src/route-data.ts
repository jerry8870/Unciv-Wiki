import { getCollection } from 'astro:content';
import { defineRouteMiddleware, type StarlightRouteData } from '@astrojs/starlight/route-data';
import { config, localUrl } from './site';

const cleanId = (id: string) => id.replace(/(^|\/)index$/, '').replace(/\/$/, '');
export const onRequest = defineRouteMiddleware(async (context) => {
  const route = context.locals.starlightRoute;
  const entries = await getCollection('docs');
  const byPath = new Map(entries.map((entry) => [config.base + (cleanId(entry.id) ? cleanId(entry.id) + '/' : ''), entry]));
  const excluded = new Set([...byPath].filter(([, entry]) => !entry.data.indexable).map(([path]) => path));
  const filterNav = (items: StarlightRouteData['sidebar']): StarlightRouteData['sidebar'] => items.flatMap((item) => {
    if (item.type === 'link') return excluded.has(item.href) ? [] : [item];
    const children = filterNav(item.entries);
    return children.length ? [{ ...item, entries: children }] : [];
  });
  route.sidebar = filterNav(route.sidebar);
  for (const direction of ['prev', 'next'] as const) if (excluded.has(route.pagination[direction]?.href || '')) route.pagination[direction] = undefined;
  const data = route.entry.data;
  if (!data.indexable) route.head.push({ tag: 'meta', attrs: { name: 'robots', content: 'noindex, follow' } });
  route.head = route.head.filter((tag) => !(tag.tag === 'link' && tag.attrs?.rel === 'alternate' && (!data.indexable || excluded.has(new URL(String(tag.attrs.href), config.site).pathname))));
  if (route.lastUpdated) route.head.push({ tag: 'meta', attrs: { name: 'wiki:lastmod', content: route.lastUpdated.toISOString().slice(0, 10) } });
  const zh = route.locale === 'zh';
  const path = context.url.pathname;
  const home = localUrl('', zh);
  const parts = path.slice(home.length).split('/').filter(Boolean);
  const crumbs = [{ name: zh ? '首页' : 'Home', item: config.site + home }];
  let current = home;
  for (const part of parts) {
    current += part + '/';
    const entry = byPath.get(current);
    if (entry) crumbs.push({ name: entry.data.title, item: config.site + current });
  }
  const jsonLd = (value: object) => route.head.push({ tag: 'script', attrs: { type: 'application/ld+json' }, content: JSON.stringify(value).replace(/</g, '\\u003c') });
  if (data.indexable) jsonLd({ '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: crumbs.map((crumb, index) => ({ '@type': 'ListItem', position: index + 1, ...crumb })) });
  if (data.article && data.indexable) jsonLd({ '@context': 'https://schema.org', '@type': 'Article', headline: data.title, description: data.description, datePublished: data.publishedAt?.toISOString(), dateModified: route.lastUpdated?.toISOString(), inLanguage: route.lang, mainEntityOfPage: config.site + path, author: { '@type': 'Organization', name: 'Unciv Wiki contributors', url: config.site + localUrl('about/', zh) } });
});
