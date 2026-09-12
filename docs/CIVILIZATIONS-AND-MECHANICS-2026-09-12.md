# 第二批交付：四个文明与四篇机制实操

已按确认的计划新增 **8 篇文章的中英文版本，共 16 个页面**。当前全站 796 个内容页，其中 794 个可索引，2 个未完成的模组目录继续排除。首批记录保留在 [内容审查与攻略](CONTENT-REVIEW-AND-GUIDES-2026-09-12.md)，本记录对应第二批最终内容及新一轮验证。

交付是本地内容和预览，没有提交、推送、合并或部署。原有未提交工作保留。文章以 4.21.20（1293）、Gods & Kings、标准速度、无模组、单人王子至国王为教学范围；难度是编辑目标，没有实测胜率、真实战报或 iOS 对局运行验证。

## 已交付文章

| 文章 | 本批的具体决策 | 中文源文件 | 英文源文件 |
| --- | --- | --- | --- |
| 巴比伦 | 文字与安全学院、工作回合、科研点数、大学、防守与飞船瓶颈 | [中文](../src/content/docs/zh/strategies/babylon/index.md) | [English](../src/content/docs/strategies/babylon/index.md) |
| 朝鲜 | 专家食物预算、5／7 基础科研、首都半中位数奖励、特色单位限制 | [中文](../src/content/docs/zh/strategies/korea/index.md) | [English](../src/content/docs/strategies/korea/index.md) |
| 罗马 | 首都先导建筑、分城排程、25% 生产力、军团与弩炮、战后恢复 | [中文](../src/content/docs/zh/strategies/rome/index.md) | [English](../src/content/docs/strategies/rome/index.md) |
| 希腊 | 衰减与均衡点恢复、礼物预算、竞争者、城邦保护和投票前余量 | [中文](../src/content/docs/zh/strategies/greece/index.md) | [English](../src/content/docs/strategies/greece/index.md) |
| 政策选择 | 时代、全部前置、互斥、开启与完成奖励、传统／自主及虔信／理性比较 | [中文](../src/content/docs/zh/mechanics/policies/index.md) | [English](../src/content/docs/mechanics/policies/index.md) |
| 市民与改良 | 工作地块和资源接入分开检查、专家机会成本、学院、工人与道路顺序 | [中文](../src/content/docs/zh/mechanics/resources-improvements/index.md) | [English](../src/content/docs/mechanics/resources-improvements/index.md) |
| 战斗与晋升 | 河流 −20%、地貌防御、视野与移动、晋升可选前置、单位类型与目标地形 | [中文](../src/content/docs/zh/mechanics/combat-promotions/index.md) | [English](../src/content/docs/mechanics/combat-promotions/index.md) |
| 信条收益 | 四类受益对象、信徒与多数城市口径、持续／一次金币、食物与传播成本 | [中文](../src/content/docs/zh/mechanics/religion-beliefs/index.md) | [English](../src/content/docs/mechanics/religion-beliefs/index.md) |

每篇均有两个明确的教学情境，并写出条件、选择、代价与复查。中英文共 32 次情境呈现，对应 16 个教学情境；不是 32 个不同实战案例。按去除链接目标后的正文统计，本批约 1.49 万中文汉字、7,821 个英文词，统计方法与逐页结果见 [内容清单](validation/batch2/content-inventory.json)。

## 规则与文案复核

固定公开规则提交为 `5fa2f57457755c403ea82cc21fec9e617feaf2d0`。本批直接读取本机该提交下的 31 个规则、算法及翻译文件，逐项记录路径、SHA-256、涉及文章与事实摘要，见 [来源记录](validation/batch2/rule-sources.json)。这是固定本地源码证据，不是对公网源码链接当前可访问性的声明。

主要纠偏与条件：

- 巴比伦 +50% 修正的是大科学家点数；两名科学家 6 基础点数可变为 9，但基础科研不是因此乘 1.5。
- 朝鲜全部已工作的专家 +2 科研；首都科研关联建筑／奇观奖励为当前可研究科技实际成本中位数的一半，再取整。100／200／300／500 示例得到 125 科研；不等于免费获得一项科技。
- 罗马检查首都是否已完成同名建筑，+25% 为生产力加成；不适用于单位生产或作为金币购买折扣。图书馆 75、基础生产力 8 的简化算例为 8 回合对 10 回合。
- 希腊在均衡点以上减缓衰减，在均衡点以下加快恢复且停在均衡点；关系竞争、性格、宗教及政策仍会改变结果。礼物收益不使用固定兑换表。
- 政策多个前置需要全部满足；晋升允许至少一个所列前置，但仍必须匹配单位类型。虔信与理性互斥；自由、秩序、独裁互斥。
- 森林丘陵常规防御不是 25%＋25%；地貌取适用最大值。开阔／崎岖晋升看被攻击格。战斗算例比较修正战斗力，不承诺固定伤害。
- 火厢车没有普通抛石机的 +200% 对城攻击，龟船不能进入海洋；军团只具有道路／堡垒建设能力，不替代一般工人。
- 创立者、强化与本地万神殿、追随者效果分开处理。拾壹税按全球信徒比例，教会财富按多数宗教城市数；宗教建筑购买许可不是免费建筑。

中文术语按固定游戏目录复核，包含“学院、文官制度、抛石机、投石车、轻帆船、国立研究院、理性政策、拾壹税”等。

七条文明能力文案通过 [translation.py](../scripts/translation.py) 的完整规则键覆盖修正，再重新导出快照和生成页面。四个文明均有实际样例回归；覆盖翻译器、快照中文字符串及最终 Markdown。未直接手改生成页。快照仍是 45 个网站数据／翻译／成就资源文件，`rules.json` 未发生本批变更，没有增加全量政策、地形或信条数据库。

## 导航、兼容与生成范围

- 机制首页增加四篇实操目录，保留原三个花费章节的完整正文、标题和已有锚点。中英 URL 均未改变。
- 攻略首页现在列出 12 篇对局攻略，另有四篇机制入口；侧栏同步新增机制分组和四个文明。
- 首批八篇中英文文章增加对应的机制／文明入口，新文反向连接旧攻略与数据库。
- 生成器提供数据库反向入口，覆盖四个文明、特色单位／建筑及相关科技、建筑等；相对本批开始时有 54 个生成数据库页面变化。
- 16 个新文保持人工文件归属，使用现有 Article、双语路由、Pagefind、sitemap 和索引机制；无新增应用 API 或依赖。
- 原 780 个内容路径全部保留。机制原正文与锚点使用哈希匹配的旧独立目录基线交叉检查，见 [兼容记录](validation/batch2/route-compatibility.json)。

## 验证结果

| 检查 | 结果与边界 | 证据 |
| --- | --- | --- |
| `pnpm validate` | 通过；6 组 Python 回归、统计开关模拟、全站构建、链接／双语／索引检查 | [主目录日志](validation/batch2/validate.log) |
| 重复生成与失败保护 | 重复两次生成，人工及生成内容哈希不变；缺文件、校验错误、坏引用、坏翻译输入不改变已发布文件 | [回归实现](../scripts/test_pipeline.py)与上述日志 |
| 文案回归 | 七条真实文明规则贯穿翻译—快照—页面检查；非目标伟人规则保持原处理 | [回归实现](../scripts/test_pipeline.py) |
| 内容与链接 | 796 内容页、794 sitemap／索引页、2 排除页、0 错误；构建额外输出一个 404 页面 | [站点检查](validation/batch2/site-check.json) |
| 独立目录 | 仅复制本站源文件与配置；离线冻结安装及完整 `pnpm validate` 通过，全部构建输入哈希匹配 | [报告](validation/batch2/independent-build.json)、[日志](validation/batch2/independent-validate.log) |
| 浏览器 | 390px 手机表格、目录跳转、朝鲜搜索及语言切换、1280px 目录、希腊数据库互链通过 | [浏览器记录](validation/batch2/browser-checks.json) |
| 编辑复审 | 8 对双语的条件、数值、两情境与限制一致；正文无残留 Markdown 粗体标记 | [复审记录](validation/batch2/editorial-review.json)、[最终输入哈希](validation/batch2/input-sha256.json) |

浏览器实测：“朝鲜”得到 19 条搜索结果，第一条为新专篇；手机语言切换保留 `strategies/korea/` 对应路径。英文表格容器 356px、内容 369px，按右键可滚动到 13px，而页面仍宽 390px。中文战斗文章目录跳到渡河教学情境，目标标题位于粘性导航下方。截图经工具可视检查，未保存为额外 PNG 文件。

这里的“独立目录”是构建隔离检查，不是另一位审查者或独立游戏实测。浏览器过程中有定位器与受限 evaluate 的调用修正，已在记录中区分；最终页面检查通过。

## 本地预览与维护

- [中文攻略目录](http://127.0.0.1:4321/Unciv-Wiki/zh/strategies/)
- [中文机制目录](http://127.0.0.1:4321/Unciv-Wiki/zh/mechanics/)
- [英文攻略目录](http://127.0.0.1:4321/Unciv-Wiki/strategies/)

后续维护方式已同步到 [维护与上线手册](MAINTENANCE-AND-LAUNCH.md)。更新版本必须重新核对规则键、算法和例子，不能只改文章版本号；调整路由时同步生成器映射、目录、侧栏和双语链接，并保留旧花费锚点。

真实战报需要存档、种子、设置与实际回放记录；皇帝以上专项、更多文明、多人和海空军专篇继续留待后续。当前交付不包含这些范围，也不包含线上发布。
