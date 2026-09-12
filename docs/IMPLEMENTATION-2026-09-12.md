# Unciv Wiki 优化交付记录

本记录保留系统优化完成时的验收基线（764 页）。随后已补写 8 篇双语对局攻略并修正建筑效果字段；最新内容规模、索引与检查结果见 [后续内容审查记录](CONTENT-REVIEW-AND-GUIDES-2026-09-12.md)。

状态：本地实施与自动检查完成；桌面、平板、手机代表页面已进行浏览器验证。没有推送、合并或线上发布。

本地预览：[中文首页](http://127.0.0.1:4321/Unciv-Wiki/zh/) · [英文首页](http://127.0.0.1:4321/Unciv-Wiki/)。预览服务保留运行，中文首页已在 Codex 中打开。

## 已完成

- 保留 Astro + Starlight、GitHub Pages 子路径、双语路由，以及此前全部 754 个内容 URL。当前共 764 个内容页，新增 10 个双语页面（数据库总览、排查文章、About、Credits、Privacy 各两页）。
- 首页实际渲染分类卡片、精选文章与 TestFlight 入口，修正基础路径；数据页清除重复 H1。手机表格独立滚动，首页补手机主题/语言入口，中文菜单与搜索控件使用中文。
- 导出 1293 所需的 45 个快照文件及校验清单，约 488 KB；正常生成与 CI 不依赖游戏私有仓库。公开游戏提交固定为 `5fa2f57457755c403ea82cc21fec9e617feaf2d0`，成就来源也固定在与 1293 对应的提交。
- 修正科技和建筑/奇观的基础造价解析，保留显式覆盖与零值；区分不可直接建造。示例已核对 Writing 55、Library 75、The Great Library 185、Shrine 40、Palace 0、Cathedral 0 + Unbuildable、National College 125。
- 修正英文表格混入中文、中文类型未翻译和翻译占位符顺序；数据库正文增加科技、升级、专属文明、替代建筑与反向关联链接。
- 成就统一使用匹配哈希的 V3 规则及中英文案，40 项、600 分，保留两语言的 N01–N40 锚点，明确本机记录边界。人工说明单独存放，不会被再生成覆盖。
- 完成双语第一局指南、1293 成就未解锁排查、iOS 安装页、花费机制、1293 更新说明和网站信息页。设备最低要求来自固定配置，没有编造截图或 App Store 链接。
- `indexable` 统一控制 noindex、主导航、Pagefind、sitemap 与语言备选。4 个未完成页面保留可访问 URL，但不进入索引集合。
- 更新 Article、有效 BreadcrumbList、真实内容日期及 sitemap lastmod，移除 SearchAction，更新 llms.txt。
- 增加可选 GA4 同意/拒绝/撤回机制，原生外链 click + 稳定链接 ID；未配置或未同意时不加载 GA4。CI 改为冻结依赖并执行整套验证。

## 验证证据

| 范围 | 结果与证据 |
| --- | --- |
| 全站结构与索引 | **PASS**：[site-check.json](validation/site-check.json)，764 页检查、760 页 sitemap、4 页排除、0 错误；包括 canonical、description、唯一 H1、内部链接/图片/锚点、面包屑、语言对应和日期。 |
| 原有 URL | **PASS**：[route-compatibility.json](validation/route-compatibility.json)，754/754 保留；检查数量不作为永久常量写死。 |
| 数据与生成 | **PASS**：4 组 Python 回归测试；实际成本例子、V3 条件、翻译参数顺序、两次生成一致、人工内容不变、缺失文件/校验错误/关联错误/语言缺失均不更新输出。 |
| 统计开关 | **PASS（模拟环境）**：未配置、非法 ID、未同意、拒绝、同意、撤回和存储禁用；验证只有一个 loader、没有自定义重复 click。没有向 Google 发送测试事件。 |
| 主工作区完整流水线 | **PASS**：[validate.log](validation/validate.log)，`pnpm validate`；`git diff --check` 通过。 |
| 独立目录构建 | **PASS**：[independent-build.json](validation/independent-build.json) 与 [日志](validation/independent-validate.log)。只复制本站 src/public/scripts/data 和构建配置，在新目录执行 `pnpm install --frozen-lockfile --offline` 与 `pnpm validate`。依赖来自本机 pnpm 缓存，未包含游戏仓库或凭据；并非重新在线下载依赖的 CI 运行证明。 |
| 浏览器 | **PASS（代表场景）**：[browser-checks.json](validation/browser-checks.json)，1440×1000、768×1024、390×844；首页/导航/表格/中英搜索/语言/主题/成就目录与旧 N08 锚点；拒绝统计后正常浏览。 |

验证输入清单：[input-sha256.json](validation/input-sha256.json)。构建输出数量含框架 404/重定向时会不同于内容页数量，本记录按内容集合统计。

源码目录中没有“默认成本的不可建造建筑”和“继承成本的国家奇观”实际条目，所以这两个分支使用真实项目的明确标注变体测试；没有冒充实际游戏样例。V3 中文 N40 翻译相对规则原文省略“中文”二字，属于匹配资源中的措辞差异，测试已明确记录；不混用旧英文 copy.json。

## 待配置与未验证

- **GA4 真实链路**：没有真实测量 ID 或后台配置，统计当前关闭；未证明 page_view / click 真实入库。阻断 Google 请求时的完整真实浏览器验收也留待该配置完成。
- **TestFlight 1293 开放状态**：真实邀请 URL 与站内入口已核对，早先 HTTP 读取能取得邀请标题；浏览器加载 Apple 页面时超时，没有以此推断测试名额、版本可用或安装成功。
- **游戏运行验证**：本轮是网站实施，不是全部 40 项成就的真实 iOS 自然对局回归，也不是全部 iPhone/iPad 型号性能验证。
- **线上结果**：未部署，未执行 Google/Bing 后台 sitemap 提交、索引检查或 Google 生成式 AI 包含状态核查。根级 robots 没有改动其他仓库。
- **截图**：未提供无法对应版本的游戏截图；浏览器布局检查使用真实本地页面。首次浏览器连接/外部 Apple 导航有超时，已用新本地标签页恢复，不把工具超时记作网页功能失败。

下一步按 [维护与上线手册](MAINTENANCE-AND-LAUNCH.md) 配置及验收外部服务，获得上线授权后再执行发布。本轮没有待定产品决策。
