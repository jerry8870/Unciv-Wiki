# Unciv Wiki 搜索曝光与 iOS 推广审查

> 本文件记录实施前的只读审计基线。优化后的结果与当前未验证事项见 [实施交付记录](IMPLEMENTATION-2026-09-12.md)。

审查日期：2026-09-12。代码基线：`a72cdd9`。目标：通过玩法、攻略和成就内容获得 Google / AI 搜索曝光，并引导读者使用 iOS App。

**总体判断：Astro + Starlight 可以继续使用。当前最需要解决的是首页入口断路、核心攻略尚未完成、iOS 下载链路缺失，以及数据内容缺少解释和来源。** 继续增加自动生成页面或 AI 专用标签，不能补上这些缺口。

**证据范围**

- 阅读配置、发布流程、内容生成器及代表性页面；通过 Repomix 整理 765 个相关文件，并按模式检索。
- 执行 `pnpm build`，退出码为 0；全量检查 754 个内容页面的构建 HTML、链接、canonical、description、结构化数据和 sitemap。
- 对线上站点发出 13 个普通 HTTPS GET 请求；读取首页、中英文页面、iOS 页、成就页、单位页、sitemap、robots.txt 和不存在的地址。
- 核对 Google 和 OpenAI 官方说明；没有访问 Search Console、Bing Webmaster Tools、App Store Connect 或站点统计后台。
- 浏览器自动化打开页面超时；线上结论来自 HTTP 响应及返回 HTML，不包含完整的桌面/手机交互与视觉测试。
- Python HTTP 客户端最初出现本机 CA 信任错误；改用正常验证证书的系统 curl 后成功，未关闭 TLS 校验，也不据此认定站点证书有问题。
- 没有运行内容生成器、访问外部游戏私有源码、修改站点实现或发布部署。本次新增文件仅为本报告。

**已经具备的基础**

| 项目 | 实际结果 | 结论边界 |
|---|---|---|
| 内容规模 | 754 个 Markdown 页面，中英文各 377 个 | 页面数量不代表已收录或有搜索流量 |
| 实体数据 | 每种语言 365 个实体页：34 个主要文明、127 个单位、124 个建筑、80 个科技 | 城邦在汇总表中，不能把实体页数理解为全部游戏数据条数 |
| 渲染 | 正文存在于构建 HTML；线上抽查也能直接读取 | 站内搜索、菜单等仍使用 JavaScript |
| canonical / description | 754 个内容页均有 description 和自指 canonical | 文案质量需要另外改善 |
| sitemap | 线上 754 个 URL，与本地内容页面对应 | 尚未确认站长后台提交状态 |
| 双语对应 | 线上所有 sitemap 条目均有 en、zh-CN、x-default，检查双向对应通过 | 无需为了 SEO 再重复实现一套 HTML hreflang |
| 基本可访问性 | 首页、iOS、成就、抽查的数据页与 sitemap 返回 200；不存在的测试页返回 404 | 普通客户端成功不等于验证过真实 Google / AI 爬虫 IP |
| 索引限制 | 内容 HTML 未发现 noindex；线上抽查未见 X-Robots-Tag 限制 | 不证明已被任何搜索引擎收录 |
| 已有素材 | 成就条件、分值、40 个图标；默认 OG 图片 | 尚未形成完整攻略或 iOS 产品介绍 |

Google 认可通过 HTML、HTTP Header 或 sitemap 中的任意一种方式声明语言版本；三种方式没有叠加的搜索收益。当前 sitemap 双语实现可以保留。[Google 多语言说明](https://developers.google.com/search/docs/specialty/international/localized-versions)

**发现的问题，按对目标的影响排序**

1. **最高优先级：中英文首页的主要入口地址错误，分类卡片没有渲染。**

   首页采用 splash 模板，实际 HTML 中没有分类侧边栏，主要依赖两个 Hero 按钮。英文按钮分别指向 `/getting-started/` 和 `/database/civilizations/`，遗漏 `/Unciv-Wiki/`；中文两个按钮也遗漏该前缀。线上验证英文新手按钮目标返回 404。全量构建扫描确认共 4 个这类错误链接。

   frontmatter 中虽然定义了六张 `cards`，首页正文为空，当前构建没有输出这些卡片。它们也没有出现在返回的线上 HTML 中。因此配置描述的分类入口实际上不存在，访问者和仅沿 HTML 链接抓取的客户端难以从首页进入正文。

   来源：[英文首页](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/index.md:8)、[中文首页](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/zh/index.md:8)。

   建议：修正四个链接；使用实际渲染的内容组件建立分类入口，提供成就与 iOS 入口。验收时从中英文首页逐一访问，目标必须返回 200；禁用脚本仍应能沿正文链接访问分类和文章。

2. **最高业务优先级：iOS 推广链路尚未建立。**

   `/ios/` 的正文只有标题和一句“TestFlight beta and App Store links for the iOS port.”，没有可点击的下载地址。全站内容和配置检索未发现 `apps.apple.com`、`testflight.apple.com` 或 Smart App Banner 配置。成就页也没有 App 下载链接。

   来源：[iOS 页](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/ios/index.md:1)、[成就页](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/achievements/index.md:1)。

   建议：根据真实发行状态建立英文 iOS 落地页，写清产品名称、发布者、与上游 Unciv 的关系、设备要求、已验证功能、游戏截图以及真实的 App Store 或 TestFlight 入口。给首页、成就页和相关攻略添加有语境的下载入口，并记录点击来源。App 的当前上架状态未在本次审查中核实，不能假定已上架或虚构链接、价格、评分。

3. **高优先级：承接玩法和攻略搜索需求的页面仍是占位页。**

   Getting Started、Mechanics、Strategies、Mods、Changelog、iOS 六类页面，中英文共 12 页，目前都是标题加一句介绍，没有兑现 description 中承诺的指导内容。这些占位页仍在 sitemap 中。

   数据百科适合查数值，但“如何开始”“怎么赢”“为什么成就不解锁”“iPhone 上怎么安装”需要具体答案。当前站点尚未提供这些内容。

   建议先完成少量高价值文章，覆盖新手第一局、前期发展、一种胜利路线、常见成就失败原因和 iOS 安装。每篇给出适用规则集/版本、条件、操作步骤、失败例子和截图。长期未完成的占位页面可暂缓进入导航及索引；已有排名页面应先核查流量，再决定处理方式。

   成就汇总页可以保留。只为需要详细路线的成就增加独立攻略，避免把 40 条简短条件机械拆成 40 个薄页面。

4. **高优先级：数据页面的信息完整性与可信度不足。**

   - 80 个科技实体页中，每种语言仅 2 页显示科技花费；78 页缺少该字段。
   - 124 个建筑实体页中，每种语言只有 35 页显示造价。
   - Writing 页的 description 承诺提供花费和解锁内容，正文没有花费，也没有可用的解锁建筑/单位清单。
   - 英文规则直接显示 `[+25]`、`<Civilopedia link [...]>` 等游戏内部语法，读者需要自行解释。
   - 页面没有明确的数据版本、规则集适用边界、提取日期和可追溯来源，`llms.txt` 却声称所有数值与 App 完全一致。

   来源：[科技生成逻辑](/Users/ai/code/Unciv4iOS-Blog/scripts/generate.py:205)、[科技页面输出](/Users/ai/code/Unciv4iOS-Blog/scripts/generate.py:832)、[Writing 实例](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/database/technologies/writing/index.md:1)、[llms.txt](/Users/ai/code/Unciv4iOS-Blog/public/llms.txt:3)。

   建议：先核查游戏对默认值、继承值、速度/难度修正和解锁关系的计算方式，再补齐生成逻辑。对玩家展示可读解释，保留必要的规则依据。每页标明来源版本和适用范围；未验证前不要声称与所有平台、所有玩法设置完全一致。

   本次确认的是“页面字段缺失及承诺不匹配”，没有验证游戏运行时，不直接判定现有数值错误。

5. **高优先级：英文内容生成时混入中文。**

   英文单位汇总表有 127 行含中文单位类型，英文科技汇总表 80 行含中文时代；英文文明汇总页也有 47 行中文城邦类型。生成器在英文分支调用了 `tr()`。中文个别页面也保留了英文类型，例如弓箭手页的 `Archery`。

   来源：[单位汇总生成](/Users/ai/code/Unciv4iOS-Blog/scripts/generate.py:486)、[科技汇总生成](/Users/ai/code/Unciv4iOS-Blog/scripts/generate.py:773)、[中文弓箭手](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/zh/database/units/archer/index.md:16)。

   建议：修正语言分支，对类别、时代、资源与术语做一致性校验。影响首先是英文读者理解和内容质量，不能把它描述成已经触发 Google 降权。

6. **中优先级：实体正文缺少关联链接，结构化面包屑包含不存在的页面。**

   中英文共 730 个实体页均未发现 Markdown 正文链接。比如弓箭手的“所需科技”“升级为复合弓兵”只有文字，不能顺着阅读。分类表和公共侧栏提供了链接，所以这些页面不是完全孤立页面，但站内知识关系没有落实到正文导航。

   738 个数据库页面的 BreadcrumbList 都引用了不存在的英文或中文 `/database/`。英文目标线上返回 404。这是结构化数据里的无效节点，不能误称为 738 个用户可见的坏按钮。

   来源：[弓箭手页面](/Users/ai/code/Unciv4iOS-Blog/src/content/docs/database/units/archer/index.md:14)、[面包屑生成](/Users/ai/code/Unciv4iOS-Blog/scripts/generate.py:282)。

   建议：建立真实数据库总览，或移除不存在的面包屑层级；把文明专属单位、科技解锁、单位升级、相关攻略互相连接。优先选语义清晰、能帮助读者继续解决问题的链接。

7. **中优先级：robots.txt 部署位置不符合爬虫读取规则。**

   线上 `/Unciv-Wiki/robots.txt` 返回 200，但域名根目录 `/robots.txt` 返回 404。标准爬虫读取主机根目录的 robots.txt，项目子目录中的文件不能承担该职责。因此当前“显式允许各爬虫”和 sitemap 声明没有通过正确位置生效。

   **这不等于禁止抓取。** 根目录 robots.txt 不存在时，Google 通常没有相应的抓取禁止规则。此处问题是配置没有发挥预期作用，不能用它解释所有收录问题。[Google robots.txt 位置与默认规则](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt)

   建议：保持现有部署时，在该 GitHub 用户站根目录提供正确 robots.txt，并在站长后台直接提交项目 sitemap；如决定长期采用独立域名，可在域名根目录部署同样配置。独立域名便于品牌和运维控制，本身不保证排名提升。迁移前需制定旧地址到新地址的重定向方案。

8. **中优先级：缺少可观测的获客和转化数据。**

   仓库有 Google 验证文件，但文件存在不能证明 Search Console 已验证、sitemap 已提交或页面已收录。方案提到 Cloudflare Web Analytics，实际配置和页面检索未找到对应埋点，也没有下载点击事件。

   一次公开 `site:` 查询未返回本站结果；这不是完整的 Google 索引检查，不能据此报告“Google 收录为 0”。

   建议建立基线：Search Console 的查询/页面曝光、点击、CTR、索引原因；Bing Webmaster Tools 的抓取与索引；站内搜索来源和 iOS 下载点击。App 安装量及后续使用需使用 App 侧或 App Store Connect 的数据，不能把网页点击直接算作安装。

9. **较低优先级：752 个内容页存在两个 h1。**

   Starlight 自动输出 frontmatter 标题，正文又以一级标题开始；除中英文首页外的 752 个内容页均重复。抽查线上 iOS、弓箭手、成就页也一样。

   建议由模板输出页面一级标题，正文从二级标题开始。这是页面语义和阅读体验问题，不能声称“多个 h1 必然被惩罚”。

**原技术方案需要纠正的判断**

| 原方案判断 | 当前应采用的判断 |
|---|---|
| Astro 零 JS，因此 Core Web Vitals 已达标 | 构建 HTML 明确含搜索、目录、主题等脚本；框架选择不能代替移动端测试和真实用户 CWV。当前未测出性能分数。 |
| x-default 是 Google 硬性要求 | 官方将其作为默认语言回退的建议；当前实现可以保留，但不是“没加就不能收录”。 |
| HowTo / FAQPage 可显著争取 Google 富结果 | HowTo 富结果已于 2023 年停用；FAQ 富结果自 2026-05-07 起不再展示，不能作为本项目的增长收益预期。 |
| SearchAction 带来站内搜索框展示 | Google 已在 2024 年移除 Sitelinks Search Box；不应继续为该搜索外观投入。当前 `?q=` 是否真正触发站内搜索尚未进行交互测试。 |
| 必须显式放行所有列出的机器人 | 默认允许、搜索抓取、用户触发访问和训练采集是不同事情；应按厂商文档分别处理。 |
| JSON-LD 作者字段必然决定 AI 引用归属 | 结构化数据应准确对应可见内容，不能承诺某个 AI 一定按指定字段署名或引用。 |

对应来源：[原方案](/Users/ai/code/Unciv4iOS-Blog/BLOG-PLAN.md:45)、[Google 多语言规则](https://developers.google.com/search/docs/specialty/international/localized-versions)、[HowTo 停用](https://developers.google.com/search/blog/2023/08/howto-faq-changes)、[FAQ 最新更新](https://developers.google.com/search/updates)、[站内搜索框停用](https://developers.google.com/search/blog/2024/10/sitelinks-search-box)。

**适合这个项目的 AI 搜索策略**

Google 当前的指南把传统 SEO、独特且可靠的内容和可访问页面作为基础；没有要求额外的 AI schema。Google 明确表示 llms.txt 不会提高或降低 Google 搜索可见性。保留该文件可以，但应把维护优先级放在真实内容和可用入口之后。[Google 生成式搜索优化指南](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

对本站而言，值得积累的是有实际证据的 iOS 操作截图、成就触发条件与失败排查、游戏规则计算的可读解释，以及带版本边界的玩法验证。可用“简明结论—适用条件—操作过程—证据—相关内容”组织文章，目的是让玩家读懂，不能保证因此被 AI 引用。没有必要为每种关键词变体单独生成一个页面。

ChatGPT 搜索应关注 OAI-SearchBot 的可达性及官方 IP 访问策略。GPTBot 对应训练，两者控制独立；ChatGPT-User 是用户触发访问，不负责决定自动搜索收录。因此允许训练不能被当成获得搜索引用的保证。[OpenAI 爬虫说明](https://developers.openai.com/api/docs/bots)

另一个需在后台核查的新事项：Google 官方说明 Search Console 的 **Search generative AI** 控制已于 2026-08-31 全球推出，默认包含网站，但子属性可能继承父属性。应确认本项目没有被排除或继承排除状态；本次没有读取或修改该设置。[Google 生成式 AI 控制](https://support.google.com/webmasters/answer/16908024)

**建议执行顺序及验收标准**

| 阶段 | 工作 | 可验证的完成标准 |
|---|---|---|
| 第一批：修通访问与推广 | 四个首页链接、真实分类卡片、数据库总览/面包屑、真实 iOS 落地页及下载入口 | 中英文首页的主要入口全为 200；可从首页和成就页到达真实下载入口；结构化数据不再指向不存在的数据库节点 |
| 第二批：内容质量 | 完成首批攻略；修正英文混入中文；验证数值默认/继承规则；补版本和来源；增加正文关联链接 | 占位页有实际答案或退出待推广内容范围；生成字段与已验证规则一致；关键关联可点击；来源能追溯 |
| 第三批：搜索与测量 | 根目录 robots、站长后台验证与 sitemap 提交、AI 包含状态核查、下载点击归因、移动端检查 | 后台记录可复核；明确索引基线；能区分自然搜索、AI 引荐、下载点击和实际安装；性能结论有实测证据 |
| 持续运营 | 根据查询和玩家问题补文章、维护版本、在相关社区分享真正有用的攻略 | 用页面/查询表现和下载转化调整选题；外部分享、发布和消息发送另行执行 |

首批选题可以考虑以下方向。它们依据产品目的与当前缺口提出，**不是已经验证有搜索量的关键词**：

- Unciv on iPhone / iPad：获取方式、设备要求、操作与功能边界。
- Unciv beginner guide：第一局设置、前期决策及常见错误。
- 一种胜利路线的完整演示：科技、城市发展与关键转折。
- iOS achievements not unlocking：资格条件、是否需要新游戏、常见失败原因，全部以实际机制验证为准。
- Rome / Babylon 等文明的打法：连接现有数值页、专属单位和实战过程。

长期域名、品牌名称、App 发行状态和可使用的截图来源需要在实施对应事项时确定。当前没有必要为了开始修复首页而等待这些决定。

**复核记录**

| 检查地址或对象 | 结果 |
|---|---|
| `https://jerry8870.github.io/Unciv-Wiki/` | 200；两个 Hero 链接缺少项目路径；未输出六张卡片 |
| `https://jerry8870.github.io/Unciv-Wiki/zh/` | 200；中文两个 Hero 链接有同样问题 |
| `https://jerry8870.github.io/getting-started/` | 404，英文首页按钮的实际目标 |
| `https://jerry8870.github.io/Unciv-Wiki/ios/` | 200；占位正文，无下载链接 |
| `https://jerry8870.github.io/Unciv-Wiki/database/` | 404，JSON-LD 中的 Database 节点 |
| `https://jerry8870.github.io/robots.txt` | 404 |
| `https://jerry8870.github.io/Unciv-Wiki/robots.txt` | 200，文件位于项目子目录 |
| `https://jerry8870.github.io/Unciv-Wiki/sitemap-index.xml` | 200 |
| `https://jerry8870.github.io/Unciv-Wiki/sitemap-0.xml` | 200；754 个 URL；语言对应异常 0；没有 lastmod |
| `https://jerry8870.github.io/Unciv-Wiki/achievements/` | 200；条件与图标存在，无 App 下载链接 |
| `https://jerry8870.github.io/Unciv-Wiki/database/units/archer/` | 200；正文表格可直接读取；重复 h1 |
| `https://jerry8870.github.io/Unciv-Wiki/llms.txt` | 200 |
| 测试用不存在的项目内地址 | 404 |

原始临时证据：[构建扫描](/tmp/unciv-wiki-audit-20260912/build-scan.json)、[HTTP 样本](/tmp/unciv-wiki-audit-20260912/http-sample.json)、[构建日志](/tmp/unciv-wiki-audit-build-20260912.log)、[代码整理输出](/tmp/unciv-wiki-audit-20260912.xml)。临时文件可能被系统清理，关键发现和统计已写入本报告。
