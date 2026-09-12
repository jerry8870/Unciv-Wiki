# Unciv Wiki：维护与上线手册

本轮交付仅为本地代码、预览和验证记录。没有推送、合并或部署。内容基线是 4.21.20（1293），Gods & Kings。系统实施见 [交付记录](IMPLEMENTATION-2026-09-12.md)，首批 8 篇双语攻略见 [攻略交付记录](CONTENT-REVIEW-AND-GUIDES-2026-09-12.md)，第二批 4 篇文明＋4 篇机制双语文章见 [第二批交付记录](CIVILIZATIONS-AND-MECHANICS-2026-09-12.md)。

## 日常开发与验收

环境：Node 22、pnpm 9、Python 3.10+（CI 使用 3.12）。

```sh
pnpm install --frozen-lockfile
pnpm validate
pnpm preview --host 127.0.0.1
```

预览中文入口为 `http://127.0.0.1:4321/Unciv-Wiki/zh/`，英文为 `http://127.0.0.1:4321/Unciv-Wiki/`。端口占用时采用命令实际输出的地址。Astro 7 预览服务可用 `pnpm exec astro preview status` 查看，`pnpm exec astro preview stop` 停止。更新静态构建后刷新浏览器；搜索需要构建后的 Pagefind 索引。

`pnpm validate` 依次执行：快照与生成结果检查、数据回归/失败保护测试、统计开关测试、Astro + Pagefind 构建、sitemap 后处理、所有内容页面的 HTML 检查。报告数量由当前内容集合计算；40 个成就和 365 个数据库实体则属于本次固定版本的目录契约。

构建只读取本仓库快照，不调用游戏仓库，不需要私有仓库凭据。新增的 Markdown 处理依赖是 Astro 7 对 remark 插件的显式要求，锁文件已更新；CI 使用冻结锁文件。

## 数据来源与更新

- `site.config.json` 集中保存站点域名、基础路径、TestFlight 链接及快照版本。
- `data/snapshots/4.21.20-1293/manifest.json` 保存版本、来源提交、原始来源摘要和导出文件 SHA-256。
- 快照包含 4 类游戏数据的所需字段、网站使用的中文翻译、V3 规则和中英文案、40 个 SVG。没有复制私有游戏代码、发布记录或凭据。
- 建筑导出还保留 percentStatBonus 与 specialistSlots，正文分别显示属性加成及专家槽位。维护导出字段时须核对嵌套对象，避免只保存基础产出而丢掉加成；大学 33% 科研、2 科学家槽位等实际样例有回归检查。
- `scripts/export-snapshot.py` 是独立的来源导出步骤，仅更新来源时使用。当前脚本有意固定 1293 的两个提交，不能用改变本地工作区文件的方式偷偷更新来源。
- `scripts/generate.py` / `scripts/wiki_data.py` 是离线验证与生成步骤，不访问外部仓库。

在有权读取来源的机器上重建当前快照：

```sh
python3 scripts/export-snapshot.py --public-repo "$UNCIV_PUBLIC_REPO" --private-repo "$UNCIV_PRIVATE_REPO"
python3 scripts/generate.py
pnpm validate
```

上述两个变量由维护者设置为授权源码仓库目录，不应将凭据写入命令或仓库。正常 CI 不运行导出器。

更新到新版本时，先核实对应的公开数据提交、成就提交与中英资源哈希；明确修改导出器固定提交、版本契约、快照目录和样例测试，审阅差异后再生成。检查真实源码成本算法是否改变。不要仅改页面的版本号。目录名称变化要维护旧 URL 的兼容跳转，成就 `N01–N40` 锚点须保留。

生成器先完成快照清单、校验值、名称/slug、引用关系和双语资源验证，再在临时目录渲染。全部成功后，仅更新 `data/generated-files.json` 列出的归属文件。输入缺失、校验错误、引用错误或语言目录不完整时，输出保持原状。文件系统写入阶段不是跨整个目录的事务；写入失败应修复原因后重新生成并执行完整检查。

规则来源要点：

- 科技：`Ruleset.kt` 的科技加载逻辑，零或缺省值继承所在列 `techCost`。
- 建筑：`Ruleset.updateBuildingCosts`，显式成本（含 0）优先；缺省 −1 的不可建造项不继承；其余按最新所需科技列，普通建筑用 `buildingCost`，世界/国家奇观用 `wonderCost`。
- 科技列选择：`IHasUniques.requiredTechs/techColumn`，包括所需科技和可用性条件中的科技要求。
- iOS 要求：1293 的 `ios/Info.plist.xml` 声明 MinimumOSVersion 15.0、设备类型 1/2；设备构建配置为 ARM64。它们不证明所有设备的性能或当前 TestFlight 可安装状态。

## 人工内容与索引

人工文章位于 `src/content/docs/` 中未列入生成清单的路径。数据库总览也由人工维护。成就通用说明在 `src/content/fragments/achievements-en.md`、`achievements-zh.md`；只编辑片段，不直接改生成的成就目录。

首页用 MDX 的实际 LinkCard/CardGrid 渲染。手工 Markdown 的站内链接从语言路径根写起，例如 `/zh/database/`，remark 插件统一加 `site.config.json` 的 base。MDX 组件链接使用 `localUrl()`；hero 动作通过内容 schema 加 base。生成器使用同一配置。修改邀请链接时还应搜索人工文章、片段和 llms.txt 中的旧邀请并同步更新，保持入口 ID 不变。

当前手工页面的 frontmatter 使用 JSON 格式（有效 YAML），便于检查脚本稳定解析。必备字段为 `title`、`description`、`gameVersion`、`appBuild`、`ruleset`、`sources`、`lastUpdated`。新文章另加 `article: true` 和 `publishedAt`，并建立同路径 `zh/` 版本。Article 只用于实际文章。

`lastUpdated` 是实质内容变化日期，不是构建日期；生成内容采用快照清单中的 `contentUpdated`（本轮内容纠正日期 2026-09-12）。更新规则、翻译或生成语义时，应明确更新这个日期；仅安装依赖或重建时不要改。sitemap 的 `lastmod` 取同一页面日期。

`indexable` 默认 `true`。攻略目录、12 篇对局攻略与 4 篇机制实操均已完成并可索引；目前仅未完成的 `mods/` 及对应中文页为 `false`，同时控制 robots noindex、主导航、Pagefind、sitemap 和 hreflang。路由仍保留，并提供已完成页面的返回链接。完成内容后将该字段改为 `true`，运行整套检查即可恢复。它不是访问控制，不能用于存放私密内容。

详细对局攻略位于 `strategies/<slug>/index.md` 与对应中文路径，属于人工文件，生成器不能覆盖。新增攻略应同时更新两语言目录、侧栏与必要的首页/llms.txt 入口。正文至少解决适用条件、阶段目标、选择分支、教学情境和失败补救；不能只用固定建造顺序替代决策解释。

机制实操位于 `mechanics/{policies,resources-improvements,combat-promotions,religion-beliefs}/index.md` 及中文对应路径；文明专篇位于 `strategies/{babylon,korea,rome,greece}/index.md`。两组都属于人工内容，不扩展生成器的文件归属。机制首页的原三个花费章节正文与标题／锚点必须保持兼容；新增内容放在独立目录章节，不替换旧段落。

第二批采用标准速度、无模组、单人王子至国王的教学范围。新增文章每篇至少两个明确标注的教学情境，包含条件、选择、代价、复查；双语保留同样的数值与判断条件。没有对局记录时不写固定胜率或实测回合。版本更新重点复查政策 ALL 前置、晋升 ANY 前置与单位类型、宗教受益范围、城邦均衡点、首都奖励算法与文明特色单位限制。

四个文明的七条歧义文案在 `scripts/translation.py` 的 `ZH_RULE_OVERRIDES` 按完整英文规则键修正。此映射仅覆盖固定规则，不用通用字符串替换改写所有百分比；它不是游戏客户端翻译修改。重新导出会写入带校验的 `zh.json`，再由生成器写数据库页；七条实际样例覆盖翻译、快照和渲染链。更新来源时确认这些键及算法仍成立，不成立就先修正映射和回归样例。

数据库到攻略的入口在 `scripts/generate.py` 的 `GUIDES` / `RELATED_GUIDES` 中维护；四个文明和其专属单位／建筑自动关联各自专篇。改变文章路由时同步更新这里、侧栏、双语目录和现有文章链接，执行 `pnpm validate` 检查，不直接编辑生成页面。第二批证据位于 `docs/validation/batch2/`；来源记录只含固定文件路径、校验值及事实摘要，没有复制完整游戏代码或扩充全量机制数据库。

攻略涉及的胜利、政策、宗教和战斗规则须回查固定源码；不能把其他资料片或模组机制套入 Gods & Kings。依据摘要见攻略交付记录及其 rule-sources.json。更新版本时，重新检查这些规则；仅修改快照成本不足以证明攻略仍适用。没有存档、种子、设置和实际回放依据时，将例子称为教学情境，不写成实战战报或保证胜率。

## 攻略配图维护

36 个中英文 Article 页面已加入源码素材图解，详见 [配图交付记录](ARTICLE-ILLUSTRATIONS-2026-09-12.md)。图解保存在人工 Markdown 的 `<figure class="guide-figure ...">` 中，样式在 `src/styles/custom.css`；普通构建不读取游戏仓库。修改文字时同步核对图中数字、标签与另一种语言。

PNG 位于 `public/game-assets/`，52 个文件的来源路径、固定提交、尺寸与 SHA-256 在 `data/guide-assets.json`；公开副本是 `public/game-assets/manifest.json`，上游原始署名随站保存为 `UPSTREAM-CREDITS.md`。恢复这些已选素材可运行 `python3 scripts/export-guide-assets.py --source-repo "$UNCIV_PUBLIC_REPO"`，只读固定提交并校验全部输入后写入。新增素材时维护清单、原作者与许可记录，不把整个素材目录无差别复制进网站。

HTML 配图使用 `/game-assets/...` 根路径，`scripts/remark-base.mjs` 为 `src`／`href` 统一补上站点 base。保留 alt、明确尺寸、lazy loading 和图注；图示应注明教学性质，不冒充实战截图。新图解须检查手机、桌面和深浅主题，运行 `pnpm validate`；七组 Python 回归包含素材原字节及署名校验，重复生成仍应保留人工图解。

## GA4 配置与验收

默认不配置测量 ID，GA4 完全不加载。可在本地 `.env` 中设置 `PUBLIC_GA_MEASUREMENT_ID=G-...` 后重新构建；GitHub Actions 使用同名 repository variable。测量 ID 不是 API 密钥，不需要增加后端接口。

上线前在 GA4 Web 数据流中开启所需页面访问与增强型衡量外链点击。关闭与本轮目标无关的增强型衡量项目，并确认不会通过其他标签重复上报。只有用户同意后才加载脚本，广告相关 consent 被设为 denied，Google signals 和广告个性化关闭。

使用原生 `click` 事件，按 `link_domain=testflight.apple.com`、`outbound=true` 识别 TestFlight 转出；`link_id` 区分入口：

| 入口 | 英文 ID | 中文 ID |
| --- | --- | --- |
| 首页 | `tf-home-en` | `tf-home-zh` |
| iOS 安装 | `tf-ios-en` | `tf-ios-zh` |
| 成就目录 | `tf-achievements-en` | `tf-achievements-zh` |
| 第一局文章 | `tf-first-game-en` | `tf-first-game-zh` |
| 排查文章 | `tf-troubleshooting-en` | `tf-troubleshooting-zh` |

没有自定义 TestFlight 点击事件。GA4 后台应核查原生 `link_id`、`link_url`、`link_domain` 与 `outbound` 是否入库；需要在报告/探索中使用未提供为内置维度的字段时，再按后台实际支持情况建立事件范围自定义维度。不要重复注册已有的内置维度。

浏览器验收步骤：

1. 清除该测试站点的偏好后进入页面：无同意时不应加载 `googletagmanager.com/gtag/js` 或发送分析请求。
2. 拒绝后重载仍不加载；链接和搜索可正常操作。
3. 同意后只出现一个 GA loader，并在 GA4 调试视图核实页面访问。点击一次 TestFlight 应只有一次原生外链事件。
4. 撤回会记录拒绝、停用 GA、清除可访问的 GA Cookie 并刷新页面；之后不再加载。
5. 阻断 Google 分析请求，验证页面及 TestFlight 普通链接仍可用。无需为了统计成功拦截或延迟跳转。

本地自动测试使用模拟 window/document，不向 Google 发请求。没有真实测量 ID、后台和真实事件证据时，不得报告“统计链路已打通”。浏览器存储不可用时，选择仅在当前页有效。撤回不删除已发送到后台的数据。

参考：[GA4 外链点击](https://support.google.com/analytics/answer/13566436?hl=en)、[自动事件参数](https://support.google.com/analytics/table/13594742?hl=en)。

## 上线清单（本轮未执行）

- [ ] 维护者审阅本地 diff、快照导出范围、署名说明和完整验证结果。
- [ ] 在 TestFlight 核实 1293 是否对目标测试群体开放，确认安装页不把上传成功当作可安装。
- [ ] 如需统计，提供真实 GA4 测量 ID、配置数据流并完成同意/拒绝/撤回和原生 click 的后台验收。
- [ ] 获得上线授权后，再提交、推送并让 Pages workflow 执行部署；本轮没有执行这些动作。
- [ ] 部署后检查 HTTPS、子路径资源、canonical、两种语言、404、搜索与 TestFlight 跳转。
- [ ] 在 Google Search Console 与 Bing Webmaster Tools 直接提交 `https://jerry8870.github.io/Unciv-Wiki/sitemap-index.xml`，检查它引用的 `sitemap-0.xml`。
- [ ] 检查 Google / Bing 的已抓取 URL、索引状态、选定 canonical 与抓取失败信息；确认未完成页面保留 noindex。
- [ ] 在适用的 Google Search Console 资源设置中核查生成式 AI 包含状态及上级资源继承状态，记录实际生效值。若后台尚未显示该设置，记录这一事实，不假定已经启用或禁用。
- [ ] 记录上线后的连续 28 天曝光、自然点击、已同意用户的页面访问与 TestFlight 转出。

根级 robots 的作用域是 origin 根路径。项目的 `/Unciv-Wiki/robots.txt` 不能替代 `https://jerry8870.github.io/robots.txt`；本轮没有修改其他根站点仓库。直接提交 sitemap，并在站长后台确认抓取；如需根 robots 变更，另行由根站点维护者处理。

转出率的分母只能使用同一统计口径下实际记录到的访问，不能把未同意用户的未记录流量当作零转出。点击不是安装，也不是留存。`llms.txt` 只是内容发现辅助，不是 Google 排名或 AI 引用保证。

参考：[Google sitemap 与准确 lastmod](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)、[多语言版本](https://developers.google.com/search/docs/specialty/international/localized-versions)、[AI 搜索优化说明](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)。

### 数据百科图标

文明、单位、建筑和科技的双语列表与详情页由 `scripts/generate.py` 添加源码图标。列表使用 32px 图标，详情使用 80px 图标；原始黑白素材通过 CSS 统一显示为白色图形并使用深绿色底，避免深浅主题下看不清；PNG 原字节不变。

`data/guide-assets.json` 的 `databaseIcons` 按类别及源码英文名称映射到素材路径，复用已有攻略素材，不重复复制。同一清单记录所有 PNG 的源码路径、固定提交、尺寸与 SHA-256；`public/game-assets/manifest.json` 是公开副本。原有 `export-guide-assets.py --source-repo <源码仓库>` 同时恢复攻略与数据百科素材。常规生成和构建无需访问源码仓库。

升级数据快照时，为新增条目补齐对应图标映射、素材记录及上游署名，再运行恢复脚本、`pnpm generate` 和 `pnpm validate`。覆盖回归检查全部类别的中英文列表和详情页，缺少映射会阻止生成；不要直接手改生成页面。
