---
{
  "title": "罗马：首都带动扩张，军团抓住有限窗口",
  "description": "协调首都与分城建筑顺序，计算罗马加成，组织军团和弩炮，并在战争后恢复快乐、金币与科研。",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293",
    "public-source:5fa2f57457755c403ea82cc21fec9e617feaf2d0"
  ],
  "lastUpdated": "2026-09-12",
  "article": true,
  "publishedAt": "2026-09-12"
}
---

本文以 **Gods & Kings、标准速度、无模组、单人王子至国王难度** 为教学基线。以下情境是根据规则构造的决策练习，不是真实战报或胜率验证。

[罗马](/zh/database/civilizations/rome/)可以让分城复制首都建筑更快，也有早期陆军优势。与[通用扩张](/zh/strategies/expansion-economy/)相比，核心变化是把首都和分城建设排成一张时间表；与通用征服相比，战争目标必须配合铁、道路、弩炮架设和战后预算。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>把首都建设与军事窗口分开安排</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/nation/rome.png" alt="罗马图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>罗马</strong><span class="visual-metric">复制首都建筑 +25%</span><p>首都必须已经完成同名建筑。</p></li>
<li><span class="visual-image is-pixel"><img class="visual-art" src="/game-assets/sprite/legion.png" alt="古罗马军团图标" width="96" height="96" loading="lazy" decoding="async" /></span><strong>古罗马军团</strong><span class="visual-metric">战斗力 17</span><p>需要铁；能修道路和堡垒。</p></li>
<li><span class="visual-image is-pixel"><img class="visual-art" src="/game-assets/sprite/ballista.png" alt="罗马弩炮图标" width="96" height="96" loading="lazy" decoding="async" /></span><strong>罗马弩炮</strong><span class="visual-metric">远程 10 / 对城 +200%</span><p>先保护架设位置，再组织占城。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>


## 能力解释与专属单位

| 项目 | 效果 | 实际边界 |
| --- | --- | --- |
| 罗马荣耀 | 建造首都已建成的同名建筑时 +25% 生产力 | 检查首都是否已经完成，不是正在建；不加速单位，不是金币购买折扣 |
| 古罗马军团 | 战斗力 17，普通剑士 14；需要铁 | 能修道路和堡垒，但不能因此替代工人的农场、矿井等改良 |
| 罗马弩炮 | 近战 8、远程 10，普通投石车为 7／8 | 保留 +200% 对城市攻击；需要架设，没有地形防御加成 |

“首都有一份，分城都加速”首先是建设顺序规则。它没有让分城免费得到建筑，也不会让首都第一次造该建筑时自带这项加成。价格与要求见[军团](/zh/database/units/legion/)、[弩炮](/zh/database/units/ballista/)和[文明条目](/zh/database/civilizations/rome/)。

## 适用局势：有质量的分城胜过单纯数量

罗马需要能工作的地块和足够快乐来支撑分城。分城只有 3 点生产力，即使提高 25%，仍不如先解决人口与矿井缺口来得有效。好首都则要有生产力，能在合理时间先完成多城共同需要的建筑。

扩张前列出各城用途：粮食核心、生产城、新奢侈品或军事要道。不要把所有城都排成相同建筑长龙；罗马加成只应帮助完成本来就有用的项目。安全内陆城没有必要为了同步而与前线同时修城墙。

## 开局分支：和平复制，还是有限战争

安全且有可守城址时，让首都先造各城都需要的粮食、文化或科研建筑，分城利用已完成的项目加速。首都正在造开拓者、工人或急需的军队时，不要因追求完美同步让分城空等；选择已可享受加成的有用项目，或者直接修当前瓶颈。

若近邻威胁核心，先看[铁器](/zh/database/technologies/iron-working/)是否能揭示可靠铁源，工人是否有时间接入，以及升级和维护预算。没有铁就不要把全军计划押在军团上；以现有弓箭与前排守住边界，或等待资源交易有保障后再决定。

计划主动战争时，在开战前选一个明确目标：解除边境威胁、取得关键资源或夺取必需的原始首都。距离过远、道路不通、地形难以架设弩炮，都可能使特色窗口耗在路上。研究[数学](/zh/database/technologies/mathematics/)解锁弩炮时，也要为护卫和补员留下生产。

## 中期关键节点：首都与分城不要相互等待

把“首都完成回合”写在分城共同建筑旁。首都领先一点时，分城可先补粮食或工人，再转入加速建筑；分城有紧急防守需求时则直接开工，不为 25% 加成让城市多暴露几回合。

[图书馆](/zh/database/buildings/library/)是典型同步项目，但[国立研究院](/zh/database/buildings/national-college/)仍要求各非傀儡城先有图书馆。无限扩张会不断推迟这个节点。自主适合有土地、工人和资源接入计划的扩张；传统适合先养强首都。罗马没有强制政策树，具体前置见[政策规划](/zh/mechanics/policies/)。

军团适合保护弩炮、挡住骑兵并最终占城。修道路或堡垒时它仍有位置与行动成本，不要在敌军接近时全军一起开工。道路能改善后续增援，但维护会累积。弩炮优先稳定的架设格和护卫，不要因看到城市残血就让军团先承受多面夹击。



<figure class="guide-figure guide-battle">
<div class="visual-heading"><span>图解</span><strong>先排好职责，再看具体交战地形</strong></div>
<div class="battle-board"><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="后排火力地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/archer.png" alt="后排火力单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>后排火力</strong><span>先削弱单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="近战前排地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/legion.png" alt="近战前排单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>近战前排</strong><span>保护射手，保留占城单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/city-center.png" alt="目标城市地块" width="128" height="128" loading="lazy" decoding="async" /></div><strong>目标城市</strong><span>占领后仍要能守住</span></div></div><p class="visual-callout">跨河近战通常 −20%：开打前检查出发格、河流和战斗预览。</p>
<figcaption>攻城分工示意，非对局截图；位置仅表示职责，不给出固定伤害。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>

## 战争后恢复与胜利收尾

每夺取一座城市后先检查快乐、金币、资源和下一回合反击。吞并会增加治理负担；计划吞并的城市要评估抵抗结束后的[法庭](/zh/database/buildings/courthouse/)建设。不要假设罗马加成能消除所有占领惩罚。

如果目标已达成、军团窗口正在过去，停战整顿通常比拖着残兵继续追更有价值。修复资源，补粮食和科研，缩短危险战线。[征服胜利](/zh/strategies/domination-victory/)要求同时控制所有主要文明的原始首都，包括自己的；不必为了这个目标占领地图上每座城。

和平罗马也可走[科技胜利](/zh/strategies/science-victory/)，将加速建设用于人口和科研体系，后期再组织生产。首都复制能力不直接加速飞船单位，必须另算部件生产。

## 教学情境一：首都图书馆已完成

**条件：** 一座分城有 8 基础生产力，计划建基础造价 75 的图书馆；首都已完成同名建筑。假设标准造价且没有其他修正、溢出或人口变化。

**选择：** 罗马加成后投入为 8 × 1.25 = **10 生产力／回合**。从零开始约需向上取整 75 ÷ 10，即 8 回合；无加成为向上取整 75 ÷ 8，即 10 回合。

**代价：** 这是简化工期，并不意味着每座城都固定省两回合。如果首都还需很久才建好，分城等待期间损失的科研可能超过加成收益。

**复查：** 打开分城生产明细，检查当前项目和罗马来源是否生效，再看实际工期。若首都正在造军队，分城按自己需求建图书馆，不把“等待加成”变成长期停工。

## 教学情境二：有军团，却攻不动第二座城

**条件：** 第一目标已经拿下，金币转负、铁源附近被骚扰；军团受伤，弩炮落后，下一座城隔河且有树林阻挡视线。

**选择：** 停止推进，保护并修复铁源，撤回军团治疗，让弩炮与护卫重组。重新评估是否用停战巩固已有目标，先恢复快乐和维护预算。

**代价：** 对手得到喘息，部分特色单位优势可能随科技进步缩小；继续渡河硬打则可能损失整支主力和已夺城市。

**复查：** 按[战斗与晋升](/zh/mechanics/combat-promotions/)查看跨河、视线和资源短缺修正；只有补给、架设位置与战后快乐都可承受时，再选择下一目标。军团战斗力 17 不会自动抵消这些条件。

## 失败补救

分城建设慢：先查是否真的在复制首都建筑，再查工作人口与[改良](/zh/mechanics/resources-improvements/)。首都所有任务都排满：把它只做必要先导建筑，分城各自生产工人或军队。战后亏钱：停止不必要路网和新部队扩张，修复资源、恢复经济，再决定是否继续征服。

可对照[希腊](/zh/strategies/greece/)的城邦保护战争，理解另一种使用早期军队的目的；更多路线见[攻略目录](/zh/strategies/)。
