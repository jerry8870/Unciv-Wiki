import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import config from './site.config.json' with { type: 'json' };
import remarkBase from './scripts/remark-base.mjs';

export default defineConfig({
  site: config.site,
  base: config.base,
  trailingSlash: 'always',
  markdown: { remarkPlugins: [remarkBase] },
  integrations: [starlight({
    title: 'Unciv Wiki',
    description: 'Unciv guides, Gods & Kings data and the Unciv4iOS community port.',
    defaultLocale: 'root',
    locales: { root: { label: 'English', lang: 'en' }, zh: { label: '简体中文', lang: 'zh-CN' } },
    customCss: ['./src/styles/custom.css'],
    routeMiddleware: './src/route-data.ts',
    components: { Footer: './src/components/Footer.astro', MarkdownContent: './src/components/MarkdownContent.astro' },
    sidebar: [
      { label: 'Getting Started', translations: { 'zh-CN': '新手上路' }, link: 'getting-started/' },
      { label: 'Database', translations: { 'zh-CN': '数据百科' }, items: [
        { label: 'Overview', translations: { 'zh-CN': '数据库总览' }, link: 'database/' },
        { label: 'Civilizations', translations: { 'zh-CN': '文明' }, link: 'database/civilizations/' },
        { label: 'Units', translations: { 'zh-CN': '单位' }, link: 'database/units/' },
        { label: 'Buildings', translations: { 'zh-CN': '建筑' }, link: 'database/buildings/' },
        { label: 'Technologies', translations: { 'zh-CN': '科技' }, link: 'database/technologies/' },
      ] },
      { label: 'Mechanics', translations: { 'zh-CN': '机制详解' }, collapsed: true, items: [
        { label: 'Overview and costs', translations: { 'zh-CN': '机制目录与花费' }, link: 'mechanics/' },
        { label: 'Policy planning', translations: { 'zh-CN': '政策选择与规划' }, link: 'mechanics/policies/' },
        { label: 'Citizens and improvements', translations: { 'zh-CN': '市民、资源与改良' }, link: 'mechanics/resources-improvements/' },
        { label: 'Terrain and promotions', translations: { 'zh-CN': '地形、战斗与晋升' }, link: 'mechanics/combat-promotions/' },
        { label: 'Beliefs and returns', translations: { 'zh-CN': '信条效果与收益' }, link: 'mechanics/religion-beliefs/' },
      ] },
      { label: 'Match guides', translations: { 'zh-CN': '详细对局攻略' }, collapsed: true, items: [
        { label: 'Choose a guide', translations: { 'zh-CN': '攻略目录与路线' }, link: 'strategies/' },
        { label: 'The first 50 turns', translations: { 'zh-CN': '前 50 回合' }, link: 'strategies/opening/' },
        { label: 'Expansion and economy', translations: { 'zh-CN': '扩张与经济' }, link: 'strategies/expansion-economy/' },
        { label: 'Combat and sieges', translations: { 'zh-CN': '战斗与攻城' }, link: 'strategies/combat-siege/' },
        { label: 'Science victory', translations: { 'zh-CN': '科技胜利' }, link: 'strategies/science-victory/' },
        { label: 'Culture victory', translations: { 'zh-CN': '文化胜利' }, link: 'strategies/culture-victory/' },
        { label: 'Domination victory', translations: { 'zh-CN': '征服胜利' }, link: 'strategies/domination-victory/' },
        { label: 'Diplomatic victory', translations: { 'zh-CN': '外交胜利' }, link: 'strategies/diplomatic-victory/' },
        { label: 'Religion', translations: { 'zh-CN': '宗教' }, link: 'strategies/religion/' },
        { label: 'Babylon', translations: { 'zh-CN': '巴比伦专篇' }, link: 'strategies/babylon/' },
        { label: 'Korea', translations: { 'zh-CN': '朝鲜专篇' }, link: 'strategies/korea/' },
        { label: 'Rome', translations: { 'zh-CN': '罗马专篇' }, link: 'strategies/rome/' },
        { label: 'Greece', translations: { 'zh-CN': '希腊专篇' }, link: 'strategies/greece/' },
      ] },
      { label: 'Achievements', translations: { 'zh-CN': '成就系统' }, link: 'achievements/' },
      { label: 'Achievement troubleshooting', translations: { 'zh-CN': '成就未解锁排查' }, link: 'guides/achievement-troubleshooting/' },
      { label: 'Unciv on iOS', translations: { 'zh-CN': 'iOS 安装' }, link: 'ios/' },
      { label: 'Mods', translations: { 'zh-CN': 'MOD 专区' }, link: 'mods/' },
      { label: 'Changelog', translations: { 'zh-CN': '更新日志' }, link: 'changelog/' },
    ],
    head: [
      { tag: 'script', attrs: { type: 'application/ld+json' }, content: JSON.stringify({ '@context': 'https://schema.org', '@type': 'WebSite', name: 'Unciv Wiki', url: config.site + config.base, inLanguage: ['en', 'zh-CN'] }) },
      { tag: 'meta', attrs: { property: 'og:image', content: config.site + config.base + 'og-default.png' } },
      { tag: 'meta', attrs: { name: 'twitter:image', content: config.site + config.base + 'og-default.png' } },
    ],
  })],
});
