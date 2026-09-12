#!/usr/bin/env node
/**
 * 为每个 <url> 注入 hreflang="x-default" 备选链接（指向 en/root 版本），
 * 补全 Starlight 内置 sitemap 缺失的 x-default，满足 Google 多语言规范。
 *
 * 在 `astro build` 之后运行（见 package.json 的 build 脚本）。
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const sitemapPath = resolve('dist/sitemap-0.xml');
let xml = readFileSync(sitemapPath, 'utf8');

const urlRe = /<url>([\s\S]*?)<\/url>/g;
let count = 0;

xml = xml.replace(urlRe, (full, inner) => {
  const enMatch = inner.match(
    /<xhtml:link rel="alternate" hreflang="en" href="([^"]+)"\s*\/>/
  );
  if (!enMatch) return full; // 无 en 备选则不处理
  if (inner.includes('hreflang="x-default"')) return full; // 已有则跳过
  const enHref = enMatch[1];
  const xdefault = `<xhtml:link rel="alternate" hreflang="x-default" href="${enHref}" />`;
  const pos = inner.indexOf(enMatch[0]) + enMatch[0].length;
  const newInner = inner.slice(0, pos) + xdefault + inner.slice(pos);
  count++;
  return `<url>${newInner}</url>`;
});

writeFileSync(sitemapPath, xml);
console.log(`[postbuild-sitemap] injected x-default into ${count} <url> entries`);
