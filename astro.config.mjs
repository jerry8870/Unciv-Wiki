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
        // Cloudflare Web Analytics —— 部署后替换为真实 beacon token
        // <script defer src="https://static.cloudflareinsights.com/beacon.min.js"
        //   data-cf-beacon='{"token": "YOUR_TOKEN"}'></script>
      ],
    }),
  ],
});
