import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const SITE_URL = 'https://jerry8870.github.io';
const BASE = '/Unciv-Wiki/';

export default defineConfig({
  site: SITE_URL,
  base: BASE,
  integrations: [
    starlight({
      title: 'Unciv Wiki',
      description: 'The community guide and database for Unciv, the open-source Civilization V remake.',
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        zh: { label: '简体中文', lang: 'zh-CN' },
      },
      sidebar: [
        { label: 'Getting Started', translations: { zh: '新手上路' }, link: 'getting-started/' },
        {
          label: 'Database',
          translations: { zh: '数据百科' },
          items: [
            { label: 'Civilizations', translations: { zh: '文明' }, link: 'database/civilizations/' },
            { label: 'Units', translations: { zh: '单位' }, link: 'database/units/' },
            { label: 'Buildings', translations: { zh: '建筑' }, link: 'database/buildings/' },
            { label: 'Technologies', translations: { zh: '科技' }, link: 'database/technologies/' },
          ],
        },
        { label: 'Mechanics', translations: { zh: '机制详解' }, link: 'mechanics/' },
        { label: 'Strategies', translations: { zh: '攻略流派' }, link: 'strategies/' },
        { label: 'Achievements', translations: { zh: '成就系统' }, link: 'achievements/' },
        { label: 'iOS', link: 'ios/' },
        { label: 'Mods', translations: { zh: 'MOD 专区' }, link: 'mods/' },
        { label: 'Changelog', translations: { zh: '更新日志' }, link: 'changelog/' },
      ],
      head: [
        // 站点级结构化数据：WebSite + Organization（Unciv4iOS）+ Sitelinks SearchAction
        {
          tag: 'script',
          attrs: { type: 'application/ld+json' },
          content: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: 'Unciv Wiki',
            url: 'https://jerry8870.github.io/Unciv-Wiki/',
            description:
              'The community guide and database for Unciv, the open-source Civilization V remake.',
            inLanguage: 'en',
            publisher: {
              '@type': 'Organization',
              name: 'Unciv4iOS',
              url: 'https://github.com/jerry8870/Unciv-Wiki',
            },
            potentialAction: {
              '@type': 'SearchAction',
              target: {
                '@type': 'EntryPoint',
                urlTemplate:
                  'https://jerry8870.github.io/Unciv-Wiki/?q={search_term_string}',
              },
              'query-input': 'required name=search_term_string',
            },
          }),
        },
        // 默认社交分享图（所有页面共用，成就页可用各自图标覆盖）
        {
          tag: 'meta',
          attrs: {
            property: 'og:image',
            content: 'https://jerry8870.github.io/Unciv-Wiki/og-default.png',
          },
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:image',
            content: 'https://jerry8870.github.io/Unciv-Wiki/og-default.png',
          },
        },
      ],
    }),
  ],
});
