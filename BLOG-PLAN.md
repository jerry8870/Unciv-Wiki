# Unciv Wiki · 技术方案

> 状态：**实施中**（阶段一 · 骨架）
> 站点名称：**Unciv Wiki**　·　仓库：`jerry8870/Unciv-Wiki`（待创建）
> 定位：**英文优先**的 Unciv 攻略与数据百科，主要面向**国外用户**，**严格符合 Google SEO**
> 技术栈：Astro + **Starlight**，托管于 **GitHub Pages**（项目页）
> 数据源：本地 iOS 移植版源码 `/Users/ai/code/Unciv4iOS-Private`

---

## 1. 核心判断

### 1.1 攻略站 ≠ 博客

博客是时间线，攻略是**常青内容**。用户从搜索引擎进来时，目标是"某文明怎么开局""这个奇观值不值得造"，而不是"最新发布了什么"。

**结论**：首屏必须是分类目录，不能是文章倒序列表。所有时间线性质的内容收敛到唯一的 Changelog 板块。

### 1.2 数值不用手写

游戏规则数据全部在源码内，且中英译名现成（实测覆盖率 98.4%，见 5.2）。共 812 条数据，手写不现实，自动化是唯一选择。

### 1.3 定位与受众

| 项 | 结论 |
|---|---|
| 主导语言 | **英文（`/`）**，中文为次（`/zh/`） |
| 受众 | **国外用户为主** |
| 获客渠道 | **Google 自然搜索为核心**——SEO 是硬指标，不是加分项 |
| 游戏数值 | iOS 移植版不改数值，全平台通用 |

**连带影响**：

- GitHub Pages 由 Fastly CDN 提供全球加速，欧美读者访问速度良好——此前担心的"国内访问速度"**不再是问题**（且面向国外用户，无影响）
- 内容撰写顺序反转：**英文为先，中文为译**
- 站名采用英文 **Unciv Wiki**

---

## 2. SEO 要求（面向 Google）

SEO 是核心目标，独立成节。

### 2.1 技术 SEO 清单

| 项 | 要求 | 由谁提供 |
|---|---|---|
| 渲染 | 静态 HTML，正文不依赖 JS | Astro SSG ✅ |
| Core Web Vitals | LCP < 2.5s · INP < 200ms · CLS < 0.1 | Astro 零 JS ✅ |
| 语义化 HTML / 唯一 h1 | 每页唯一 `h1`，层级正确 | Starlight ✅ |
| `title` / `description` | title ≤ 60 字符；description 140–160 字符；每页唯一 | frontmatter（须逐页写） |
| canonical | 每页自指绝对 URL | Starlight ✅ |
| `sitemap.xml` | 自动生成，含全部语言 | `@astrojs/sitemap` + i18n ✅ |
| `robots.txt` | 允许抓取并指向 sitemap | 自建 |
| RSS | 按语言输出 | 需自建（Starlight 无内置） |
| 结构化数据 | JSON-LD（见 2.3） | **需自建** |
| OG / Twitter Card | 含 `og:image` | Starlight 基础 ✅ / 动态图需自建 |
| 移动友好 | 响应式 | Starlight ✅ |
| 404 页 | 自定义 | Starlight ✅ |
| 内链 | 侧边栏 + 面包屑 + 相关链接 | Starlight ✅ |

### 2.2 双语站的 SEO 关键 —— hreflang

**这是双语站最容易翻车的地方。** 配错会导致中英页面互相竞争同一批关键词，或 Google 只收录其中一边。

Google 硬性规则：

1. **每个页面都要列出全部语言版本**，含自己（self-reference）
2. **必须双向**：`/` 引用 `/zh/`，`/zh/` 必须反向引用 `/`
3. **必须含 `x-default`**，指向默认语言（本项目为英文）
4. **必须用绝对 URL**
5. URL 用**子目录**（`/zh/`），不用参数（`?lang=zh`）或子域名

Starlight 的处理：

- 多语言路由、HTML `lang` 属性、语言切换器：**内置** ✅
- `@astrojs/sitemap` 的 `i18n` 配置会自动在 sitemap 中生成 hreflang alternates ✅
  - Google 官方认可三种声明方式（HTML `<link>` / sitemap / HTTP header），**sitemap 已满足要求**
- ⚠️ HTML `<head>` 内的 `<link rel="alternate" hreflang>` 是否由 Starlight 自动输出，**实施时需验证**；若缺失则通过 `head` 配置补齐（建议两者一致）
- 建议**按语言拆分 sitemap** 并分别提交 Search Console，便于分语言观测收录与抓取错误

### 2.3 结构化数据（JSON-LD）

Starlight 不默认输出业务型 JSON-LD，**需自建组件注入**：

| 页面类型 | Schema |
|---|---|
| 全站 | `WebSite` + `SearchAction` |
| 攻略文章 | `Article` / `BlogPosting`（含 author、datePublished、dateModified） |
| 分类与百科层级 | `BreadcrumbList` |
| 步骤型攻略 | `HowTo` |
| 问答型内容 | `FAQPage` |
| 百科列表页 | `ItemList` |
| 成就图鉴 | `ItemList` + 单项 `CreativeWork` |

`HowTo` 与 `FAQPage` 对攻略站尤其值钱——有机会直接进入 Google 富结果，显著提升点击率。

### 2.4 内容层面的 E-E-A-T

- 需有 About / 作者页
- **署名方式**：以 **`Unciv4iOS` 项目名义**（非个人署名）。JSON-LD 的 `author` 与 `publisher` 均使用 `Organization` 类型，`name` = `Unciv4iOS`，`url` 指向 GitHub 仓库。权威感来自项目而非个人，同时不暴露个人账号
- 机制类文章标注依据来源（可引用 Unciv 源码文件路径，体现一手来源）
- **"能读源码写机制"本身就是最强的 E-E-A-T 信号**——这是本项目的结构性优势，多数攻略站只能复述游戏内所见
- ⚠️ **英文内容不可直接机翻**。Google 对无人工校对的翻译内容会降权

### 2.5 部署侧

- GitHub Pages 由 Fastly CDN 提供全球加速，欧美访问速度快
- 静态资源长缓存 `max-age=31536000, immutable`；HTML 用较短 TTL（Actions 部署自动处理）
- sitemap 提交 Google Search Console
- 统计使用 **Cloudflare Web Analytics**：无 Cookie、**无需 GDPR 同意横幅**、脚本轻量不影响 CWV（注：仅统计用 Cloudflare，与托管平台无关，仍可选）

### 2.6 AI 检索与收录（AEO / GEO）

目标：让 ChatGPT / Perplexity / Claude / Google AI Overviews 等能收录并引用本站内容。

#### ① 托管平台对 AI 爬虫的态度

**已切换至 GitHub Pages**，它**默认不屏蔽任何爬虫**（包括 AI 爬虫），无 Cloudflare 那套 "Block AI scrapers" 默认开启的问题。

> 背景：若留在 Cloudflare Pages，新 zone 自 2025-07 起默认屏蔽 AI 爬虫，需手动关闭 "Block AI scrapers and crawlers" 并检查 "Manage AI bots' robots.txt"。切换后此风险**已消除**。

#### ② robots.txt：显式放行检索型爬虫

GitHub Pages 本身不屏蔽，但仍需显式声明以表达意图、并利于排查：

| 类型 | 代表 UA | 作用 | 处理 |
|---|---|---|---|
| **检索型** | `Googlebot` · `Bingbot` · `OAI-SearchBot` · `ChatGPT-User` · `PerplexityBot` | 实时抓取，用于**回答并附引用** | **必须允许**，否则 AI 搜不到你 |
| 训练型 | `GPTBot` · `Google-Extended` · `CCBot` · `Bytespider` · `Amazonbot` · `meta-externalagent` · `Applebot-Extended` | 采集用于**离线训练** | 可选屏蔽 |

两点注意：

- `Google-Extended` **不影响** Google 搜索与 AI Overviews（那是 `Googlebot` 的职责）
- 厂商的 UA 命名规则不统一（同一家可能同时有训练与检索爬虫），**实施时须以各厂商官方文档为准，不要照抄二手清单**

**本项目建议：全部允许，不屏蔽训练爬虫。** 理由：本站无广告变现，内容是社区知识；屏蔽训练爬虫没有收益，反而损失长期曝光——让 AI 认识 Unciv 与本站本身就是收益。策略可随时调整。

#### ③ 内容结构要利于被摘取

- 静态 HTML、无 JS 依赖 ✅（Starlight 天然满足）
- **问答式小节**：以玩家会问的问题作小标题，紧随直接答案。AI 检索系统按段落摘取，此结构最易被引用
- **JSON-LD 的 `author` / `publisher` 字段**：AI 用它生成引用归属；缺失时内容会被归给"某网站"而非具体作者
- **术语一致**：统一使用 `Unciv`、`Civilization V` 及游戏内官方英文名（本站数据正是权威来源）
- **时效性标注**：页面标注对应游戏版本（当前 4.21.19）与更新日期

#### ④ llms.txt：低成本期权，不是主战场

`/llms.txt`（及 `/llms-full.txt`）是站点摘要的 Markdown 约定。须如实了解其现状：

| 事实 | 数据 |
|---|---|
| 站点采用率 | 约 10%（30 万域名抽样） |
| AI 引用最高的 50 个域名中 | **仅 1 个**有该文件 |
| AI 爬虫实际请求量 | 5 亿+ AI bot 事件中仅数百次请求 `/llms.txt` |
| Google 立场 | **明确不支持**，已列入"不必要做法" |
| 厂商承诺 | 无任何主流 AI 厂商公开承诺读取 |
| 已发布文件构成 | 约 40% 是插件生成的默认垃圾 |

**结论：不要把它当策略。** 但值得花 20 分钟发布，理由有三：成本近零且是对未来的一次期权；撰写过程强制梳理"最重要的页面"，能暴露重复内容与孤岛页面；它是面向 **agent** 的接口。

格式：H1 站点名 → blockquote 一句话摘要 → H2 分组 → 每组下列 `- [标题](绝对URL): 一句话说明`。**控制在 10–40 个链接，不要当 sitemap 用。**

#### ⑤ 优先级

时间有限时，投入顺序为：**爬取权限（①②）> 答案结构（③）> 原创数据 > llms.txt（④）**。

前两项是硬门槛——**门槛没过，后面做再多也没用**。第三项恰好是本项目的强项（源码、812 条数据、40 项成就图鉴）。

---

## 3. 技术选型

| 层 | 选型 |
|---|---|
| 框架 | **Astro** |
| 主题 | **Starlight**（Astro 官方文档框架） |
| 托管 | **GitHub Pages**（项目页 `jerry8870.github.io/Unciv-Wiki/`） |
| 语言 | **英文根路径 `/`，中文 `/zh/`** |
| 数据源 | 本地 Unciv4iOS 源码 |
| 搜索 | Pagefind（Starlight 内置） |
| 图片 | 随文章存仓库，Astro 构建时优化 |
| 统计 | **Cloudflare Web Analytics** |
| 评论 | 暂不接入 |

### 3.1 为什么是 Astro + Starlight

Astro 的 SEO 与性能无需论证（技术 SEO 5/5、性能 5/5，默认零客户端 JS）。

**选 Starlight 而非博客主题的三个决定性理由**：

**① i18n 原生，直接消掉本项目最大的一块成本**

所有 Astro 博客主题（Fuwari、Firefly、AstroPaper）的 i18n **都只是 UI 文案级**，双语**内容**路由必须自建——要改 Content Collections、动态路由、分页、RSS、Pagefind 索引、导航、语言切换器。Starlight 的 i18n 是**框架能力**：多语言路由、语言切换器、HTML `lang`、导航本地化、`@astrojs/sitemap` 的 hreflang alternates 全部内置。

**② 侧边栏天然就是攻略站要的"分类目录"**

Starlight 的多级侧边栏 + 面包屑 + 目录，正好对应"新手上路 / 数据百科 / 机制详解 / 攻略流派 / 成就系统 / MOD / Changelog"的结构。博客主题的时间线形态反而是要改造的对象。

**③ Splash 首页天然就是分类入口**

Starlight 的 `template: splash` 首页支持 Hero + CardGrid，**开箱即是分类入口**，无需自己设计落地页。

**附带红利**：

- **Fallback 内容机制**——未翻译的页面自动回落默认语言并显示"尚未翻译"提示。这意味着**英文先写，中文渐进翻译**，未翻译页面中文用户看到英文而非 404。对双语渐进上线极其有用。
- 官方维护，升级与 a11y 有保障
- Pagefind 多语言搜索内置

**代价（已确认接受）**：视觉偏文档风格，不如博客主题花哨。对"英文攻略站 / Wiki"定位而言这是合适的取舍。

**明确不用 Next.js**：纯内容站无需 SSR/ISR，且在 Cloudflare 上有 Runtime 适配坑。

### 3.2 被否决的候选

| 候选 | 否决原因 |
|---|---|
| `CuteLeaf/Firefly`（2,114★） | 卖点是装饰性功能（Live2D 看板娘、APlayer 音乐、樱花特效、Swup 过渡），**与严格 SEO 冲突**（拖累 CWV），且二次元风格不契合英文攻略站；i18n 仍需自建 |
| `satnaing/astro-paper`（5,038★） | SEO 友好、质量高，但仍是**博客时间线**形态，分类目录与双语路由都要自建 |
| `markhorn-dev/astro-nano`（936★） | 一年多未更新（2025-06-16） |
| Fuwari 的任何镜像 fork | 上游 `saicaca/fuwari` 自 2025-09 后仅依赖升级，**实质停更** |

---

## 4. 信息架构

```
/ (English, root locale)   |   /zh/ (简体中文)
├── Getting Started            入门 · 界面 · 与文明 5 的差异
├── Database ⌁                 数据百科
│   ├── Civilizations          聚合表 + 热门文明独立页
│   ├── Units                  聚合表 + 热门单位独立页
│   ├── Buildings              聚合表 + 热门建筑独立页
│   └── Technologies           聚合表 + 热门科技独立页
├── Mechanics                  机制详解
├── Strategies                 攻略流派
├── Achievements ⌁             40 项成就图鉴（iOS 版）
├── iOS                        测试邀请 · App Store 链接
├── Mods                       MOD 专区
└── Changelog                  版本差异（唯一时间线内容）
```

⌁ = 由脚本从本地源码生成，非人工撰写。

### 4.1 页面粒度（已确认：聚合页 + 热门实体页）

| 类型 | 数量 | 作用 |
|---|---|---|
| **聚合索引页** | 4（每类一个可筛选表格页） | 该类总览与检索入口 |
| **热门实体独立页** | 约 40（4 类各约 10 个） | 独立着陆页，承载长尾搜索 |
| **成就图鉴** | **1 个单列表页**（含 40 项） | iOS 成就总览；每项带稳定锚点 ID |
| 数据覆盖 | 聚合页从全量 812 条生成；独立页首期只覆盖热门实体 | |

**独立页的内容要求**（规避 thin content —— 这是该路线唯一的风险点）：

不能只列数值，每页必须包含：

- 基础数值
- `uniques` 逐条解析
- 关联关系（前置科技 / 升级路径 / 可被何种对象替代）
- **使用建议**（人工补充，这是唯一无法自动化、也最能拉开差距的部分）

**热门实体的选定标准**：待定（见第 13 节）

**成就图鉴为单列表页**：40 项集中在一页。虽只产生 1 个 SEO 着陆页，但内容厚实不会被判 thin content；通过**每项稳定锚点 ID**（如 `#n01`）与页面级 `ItemList` JSON-LD，仍可让搜索引擎与 AI 解析出 40 个独立条目。若日后成就名被验证有搜索量，内容模型支持再拆分为独立页。

### 4.2 实现方式

- Starlight `sidebar` 配置 + 内容目录结构
- 首页：`template: splash` + CardGrid 作为分类入口

---

## 5. 数据管道

### 5.1 数据源

```
/Users/ai/code/Unciv4iOS-Private/public/Unciv4iOS/android/assets/jsons/
  ├── Civ V - Gods & Kings/     ← 唯一规则集（本方案只做这一个）
  ├── translations/             53 个语言的 .properties
  ├── Tutorials.json            66 KB，新手教程文本
  └── TileSets/
```

配套：`changelog.md`（285 KB，上游更新日志）

**用本地而非上游 GitHub 的理由**：离线可复现；与 iOS 版本严格对齐；iOS 移植版声明改动仅限 iOS 支持，游戏数值与上游一致。当前基线 **4.21.19**。

### 5.2 数据结构实测结论

均为实际读取源码验证，非推测。

**① JSON 含注释与尾随逗号** —— `//` 与 `/* */` 均存在，标准 `JSON.parse` 会直接报错，必须用容错解析器。

**② 嵌套层级不一致** —— 同步脚本必须按类目分别处理：

| 类型 | 取值路径 |
|---|---|
| Techs | `data[*].techs[*].name`（两级） |
| Policies | `data[*].policies[*].name`（两级） |
| 其余 14 类 | `data[*].name`（平铺） |

**③ 数据规模（递归去重后，共 812 条）**

Nations 83 · Units 127 · Buildings 124 · Techs 80 · Policies 70 · UnitPromotions 106 · Beliefs 56 · TileResources 35 · Terrains 33 · TileImprovements 35 · 其余 5 类 54

**④ `civilopediaText` 几乎不存在**（Buildings / Units / Techs 各 1 条，Nations / Policies 为 0）
→ 自动生成只能产出**数值表 + 结构化字段**；观点性内容必须人工撰写。排期须如实计入。

**⑤ `Nations.json` 字段丰富** —— `leaderName` · `startBias` · `preferredVictoryType` · `uniqueName` + `uniques` · 文明配色 · `favoredReligion` · `cities`（40 个城市名）· 外交台词。足以支撑信息量充足的文明页。

**⑥ 译文在独立的 `.properties` 文件中**

```
android/assets/jsons/translations/Simplified_Chinese.properties
```

格式 `英文原名 = 译文`，**key 即英文原名**（`Archer = 弓箭手`）。英文名取自 JSON 的 `name` 字段，中文名查该表。

**实测覆盖率：812 条中命中 799 条，98.4%**。16 个类目中 15 个达 100%。唯一缺口 UnitPromotions 的 13 条为模板合成 key（如 `[Mohawk Warrior] ability`），非真实缺失。

→ **中英数据百科零人工翻译成本。**

### 5.3 成就数据（iOS 版专属）

权威目录：`assets/achievements/gamecenter-catalog.json`

| 项 | 值 |
|---|---|
| 成就数 | **40**（N01–N40） |
| 语言 | 20 种，每语言 40 条完整条目（**博客只用其中的英文与简中**） |
| 分值 | 5 / 10 / 25 / 50，总分 600 |
| 字段 | `name` · `condition` · `summary` · `honor` · `tier` · `points` |
| 图标 | 原创矢量（manifest 声明 `artwork_origin: "Original vector compositions"`），SVG + PNG @1x/@2x/@3x + 1024 分享图 |

**版权干净**：原创矢量设计，非游戏素材。

> ⚠️ 数据中声明的 20 种语言**仅用于 App 内显示**，博客只做中英。
> ⚠️ 同目录 `rules-en.json` / `gamecenter-en.json` 中的 A01–A40 为 **V1 废弃编号**，不作为数据源。

### 5.4 管道设计

```
本地源码 (jsons/ + achievements/)
      │
      ▼
  同步脚本
  ├─ 容错解析（剥离注释）
  ├─ 按类目处理嵌套路径
  ├─ JOIN Simplified_Chinese.properties / 英文原文
  └─ 输出中英双语中间数据
      │
      ▼
Starlight 内容集合（Zod schema 校验）
      │
      ▼
GitHub Pages
```

要点：

- 脚本产出**中间数据**，输出到 `src/content/docs/`（英文）与 `src/content/docs/zh/`（中文），不直接改模板
- `docs/Modders/schemas/` 下有 **27 个官方 JSON Schema**，可直接转写为 Zod schema
- 升级 iOS 版时重跑脚本即可
- 已验证的解析原型位于 `/tmp/unciv_i18n_probe2.py`

---

## 6. 双语策略

### 6.1 URL 与目录结构

| 语言 | URL | 内容目录 | hreflang |
|---|---|---|---|
| **英文（默认 / root locale）** | `/` | `src/content/docs/` | `en` |
| 简体中文 | `/zh/` | `src/content/docs/zh/` | `zh-CN` |

Starlight 配置（`root` locale 让英文不带前缀）：

```js
locales: {
  root: { label: 'English', lang: 'en' },
  zh: { label: '简体中文', lang: 'zh-CN' },
}
```

目录名用 `zh`（URL 为 `/zh/`），`lang` 设为 `zh-CN`（hreflang 用标准 BCP-47）。**同文件名即自动关联多语言页面**，这是 hreflang 配对的基础。

### 6.2 板块覆盖与内容来源

| 板块 | 英文 | 中文 | 内容来源 |
|---|---|---|---|
| 数据百科 | ✅ | ✅ | 脚本自动 JOIN，**零成本** |
| 成就系统 | ✅ | ✅ | 脚本自动 JOIN，**零成本** |
| 攻略 / 机制文章 | ✅ **主版本** | ✅ 译文 | **人工撰写，英文优先** |

### 6.3 渐进翻译（Starlight 红利）

Starlight 的 fallback 机制：某页面缺少中文版本时，`/zh/` 下自动展示英文内容并标注"尚未翻译"。

**这允许：英文全量上线 → 中文按优先级逐步补齐**，未翻译页面不会 404，也不需要在导航里隐藏。对本项目是最实用的特性之一。

---

## 7. 图片

截图数量与体积都不大，**直接随文章存放在仓库内**，由 Astro 构建时优化。

```
src/content/docs/getting-started/
  ├── index.md
  ├── cover.webp
  └── screenshot-01.webp
```

- 正文引用：`![](./screenshot-01.webp)`
- Astro 自动生成多尺寸 WebP / AVIF

**SEO 相关要求**（图片影响排名与体验）：

- 每张图必须有**描述性 `alt` 文本**，并随语言本地化
- 显式指定宽高，避免 CLS
- 懒加载（首屏 LCP 图除外，需 `loading="eager"`）
- 文件命名语义化（`unciv-archer-stats.webp` 而非 `img_01.webp`）

平台限制（当前规模下不构成问题）：Pages 免费版每站点 20,000 文件、单文件 25 MiB。

---

## 8. 源码作为攻略写作的参考

本地源码是"机制详解"类文章的**权威参考**，可直接查证游戏公式与判定逻辑。

```
public/Unciv4iOS/core/src/com/unciv/
  ├── logic/           游戏逻辑：战斗、外交、城市、回合、地图
  ├── models/ruleset/  数据模型：Unique、Policy、Technology…
  ├── ui/              界面实现
  └── utils/
```

| 素材 | 位置 | 用途 |
|---|---|---|
| `Tutorials.json`（66 KB） | jsons/ | Getting Started 的官方教程文本 |
| `changelog.md`（285 KB） | 仓库根目录 | Changelog 板块，含版本差异 |
| `docs/Modders/schemas/`（27 个） | docs/ | 字段语义，数据页注解来源 |
| `core/src/.../logic/` | 源码 | 机制文章的公式与判定依据 |
| `Uniques` 系统 | 源码 + JSON | 特色能力解读，本作攻略的核心难点 |

**这既是内容差异化的来源，也是 SEO 上最强的 E-E-A-T 信号**（一手来源、可验证）。

---

## 9. 部署链路

1. 在 `jerry8870` 账号下创建仓库 **`Unciv-Wiki`**，推送本项目代码
2. 仓库 Settings → Pages → Source 选 **GitHub Actions**（本方案已提供 `.github/workflows/deploy.yml`）
3. 首次 push 后 Actions 自动 `pnpm install && pnpm build` 并部署到 `jerry8870.github.io/Unciv-Wiki/`
4. 站点 URL 为 **`https://jerry8870.github.io/Unciv-Wiki/`**（Astro 已设 `base: '/Unciv-Wiki/'`）
5. 自定义域名（后续购买）→ 加 CNAME + 改 `base` 为 `/` 即可切换
6. 提交 sitemap 至 Google Search Console
7. **AI 爬虫验证**：GitHub Pages 默认不屏蔽，`curl -A "OAI-SearchBot" -I https://jerry8870.github.io/Unciv-Wiki/` 应返回 200

环境要求：Node ≥ 22、pnpm ≥ 9。**本地已确认可用**（Node 22.22.2 / pnpm 9.15.9 / git 2.50.1）。
免费额度：公开仓库 GitHub Actions 免费，站点软限制 1GB / 带宽 100GB/月。

---

## 10. 里程碑

| 阶段 | 内容 | 验收标准 |
|---|---|---|
| **一 · 骨架** | 初始化 Starlight → 配置 i18n（root=en / zh）→ 配置 sidebar 分类目录 → splash 首页 → 基础 SEO（robots.txt 含 AI 爬虫放行 / sitemap / 统计脚本）→ **GitHub Actions 部署工作流** | 本地 dev server 正常；`/` 与 `/zh/` 均可访问；Lighthouse SEO 与性能高分；Actions 部署成功 |
| **二 · 数据管道** | 同步脚本（容错解析 + 嵌套处理 + 双语 JOIN）+ Zod schema + 4 个聚合索引页 + 约 40 个热门实体页模板 + 成就图鉴单列表页 | 812 条数据可从源码生成聚合页；热门实体页与 40 项成就列表页中英双语可用 |
| **三 · SEO 与 AI 检索补全** | JSON-LD 组件（Article 含 author/publisher、HowTo、FAQPage、BreadcrumbList、ItemList）+ 动态 OG 图 + RSS + 验证 hreflang 完整性 + `/llms.txt` | 富结果测试通过；hreflang 双向且含 x-default；Search Console 无报错 |
| **四 · 内容与上线** | 攻略文章写作（**英文优先，首批 2 篇测试**）+ 自定义域名 + 提交 sitemap | 正式域名可用；核心页面被 Google 收录 |

> **首批 2 篇测试文章的选题原则**：分别验证两条核心假设——
>
> ① **流量假设**：选一个搜索意图明确的主题（胜利路线 / 新手入门 / 与文明 5 的差异），验证能否从 Google 拿到自然流量，并顺带走通数据管道。
> ② **差异化假设**：选一个**必须读源码才能写清**的机制主题（如战斗伤害计算、幸福度公式、Unique 系统解析），验证"能读源码"是否真能产出其他攻略站写不出的内容。
>
> 两篇一起跑，即覆盖整站的两个核心假设。具体选题待定，可调整。

> 相较早期方案，原第三阶段"自建 `[lang]` 双语路由"因选用 Starlight 而**消失**，替换为"SEO 补全"。

---

## 11. 合规与素材

**代码授权：MPL-2.0**（非 GPL）。媒体素材为混合 CC 授权（CC BY-SA 4.0 / CC BY 3.0-4.0 / CC0 / Public Domain），清单见仓库 `docs/Credits.md`。

| 素材类型 | 结论 |
|---|---|
| 自己截的游戏截图 | ✅ 可用 |
| 自绘图表 / 数据表 | ✅ 可用（脚本生成，无素材风险） |
| **成就系统图标** | ✅ 可用，原创矢量设计 |
| **Unciv 自有图标 / 贴图** | ✅ 可用，须按各自 CC 授权署名 |
| **Firaxis 原版 Civ V 素材** | ❌ **绝对不可用**（README 原文 "definitely illegal"） |
| "Civilization" 名称 / 相似标识 | ⚠️ 商标风险，避免 |

必须准备 **Credits / 素材来源页**（英文），逐项标注来源与许可证。

---

## 12. 已决事项

| 项 | 决定 |
|---|---|
| 站点名称 | **Unciv Wiki** |
| 仓库 | **`jerry8870/Unciv-Wiki`**（待创建，与 app 源码仓库分离） |
| 框架 / 主题 | **Astro + Starlight** |
| 托管 | **GitHub Pages**（项目页 `jerry8870.github.io/Unciv-Wiki/`，`base=/Unciv-Wiki/`） |
| 语言策略 | 英文根路径 `/`，中文 `/zh/`；**全站双语含攻略文章** |
| 中文上线节奏 | **英文全量先上，中文渐进补齐**（利用 Starlight fallback） |
| 统计 | **Cloudflare Web Analytics** |
| 数据源 | 本地 `/Users/ai/code/Unciv4iOS-Private` 源码 |
| 规则集 | 仅 Gods & Kings |
| 数据百科粒度 | **聚合索引页 + 约 40 个热门实体独立页** |
| 成就板块 | 40 项一次全上；**单列表页**（每项带稳定锚点 ID） |
| iOS 专属内容 | **成就系统 + TestFlight 测试邀请 + App Store 上架链接** |
| 作者署名 | **以 `Unciv4iOS` 项目名义**（JSON-LD 用 `Organization` 类型） |
| 图片 | 随文章存仓库 |
| 首批攻略 | **2 篇测试**（分别验证流量假设与差异化假设，选题原则见第 10 节） |
| 评论 | 暂不接入 |
| 域名 | 后续自行购买 |

---

## 13. 待决事项

**需要用户提供具体信息**

- [ ] 热门实体的选定标准（4 类各约 10 个，合计约 40）
- [ ] TestFlight 邀请链接与 App Store 链接（上架后补）

**需要用户决策**

- [ ] 首批 2 篇测试文章的具体选题（原则已定，见第 10 节）
- [ ] RSS 是否要做（Starlight 无内置，属自建项）

**可后定，不影响架构**

- [ ] 本地工作区目录名是否改为 `Unciv-Wiki`（现为 `Unciv4iOS-Blog`，与仓库名不一致；纯重命名，无功能影响）
- [ ] 域名倾向（影响 `site` 配置与 canonical，可先占位）
- [ ] 仓库公开还是私有
- [ ] 游戏截图来源（iOS 版 / 桌面版 / 混合）
- [ ] 品牌视觉（主题色、Logo）
- [ ] 数据同步触发方式（定时跑 vs 跟随上游 release）

---

## 14. 实施前置约定

**只有用户明确说"开始实施"时才动手。** 方案讨论阶段不改动项目文件、不拉取模板、不安装依赖。

本地环境已确认可用：Node 22.22.2 / pnpm 9.15.9 / git 2.50.1。
