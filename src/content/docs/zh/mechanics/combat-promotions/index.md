---
{
  "title": "地形、战斗修正与晋升：先读预览再出手",
  "description": "用河流、丘陵、森林、移动与视野判断交战位置，核对晋升前置及单位类型，并练习进攻与撤退决策。",
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

面板上的基础战斗力只是一项输入。先看能否移动、能否看见与射击，再读战斗修正；最后才决定是否攻击。阵型和攻城流程见[战斗与攻城](/zh/strategies/combat-siege/)，本页解释如何读懂一次具体交战。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>一次攻击前的三次确认</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/scouting.png" alt="位置与视线图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>位置与视线</strong><span class="visual-metric">先确认能打</span><p>射程覆盖不代表有视线或足够行动。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/shock.png" alt="战斗修正图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>战斗修正</strong><span class="visual-metric">看被攻击格</span><p>河流、夹击、地形与伤势一起判断。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/logistics.png" alt="晋升路线图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>晋升路线</strong><span class="visual-metric">类型 + 任一前置</span><p>按单位类型走路线，不把所有前置都点完。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>


## 地形会改变哪些事情

| 条件 | 固定规则中的效果 | 操作检查 |
| --- | --- | --- |
| 普通草原／平原 | 基础移动成本 1，无地形防御加成 | 便于机动，但前排不能依赖额外掩护 |
| 丘陵、森林、丛林 | 基础移动成本 2；各自防御加成 25% | 检查移动后还剩多少行动；带“无地形防御加成”的单位不享受正加成 |
| 森林丘陵 | 地貌防御取相应最大值，常规为 25% | 不是把森林与丘陵加成相加成 50%；堡垒等改良另算 |
| 沼泽 | 基础移动成本 3，防御 −15% | 不要把所有看似复杂的地形都当作有利掩护 |
| 跨河近战攻击 | 通常攻击修正 −20% | 忽略跨河惩罚能力，或两端有效道路连接且具备跨河道路科技时，可免除此项 |
| 森林与丛林视线 | 可阻挡同高度地块的视线；丘陵影响视野高度计算 | 射程覆盖不等于有射击视线，必须检查实际可攻击目标 |
| 夹击 | 近战攻击时，每个额外相邻的己方近战单位基础提供 +10% | 不是任意远程单位靠近都算；移动友军后重新预览 |

移动成本会受道路、河流、单位能力、敌方控制区等影响，上表不是所有单位的最终移动价格。远程攻击不套用普通近战跨河攻击惩罚；攻城单位还要检查架设和射击行动条件。

## 读预览的顺序

先点计划攻击的目标，确认实际攻击出发格。再逐项看地形、河流、晋升、夹击、资源短缺等修正，并确认自己用的是近战还是远程战斗力。受伤会影响伤害输出；不要用满血单位的经验估算残血单位。

然后检查敌人下一回合的反击范围：击杀一个单位后，近战单位可能进入目标格，暴露在两支远程单位面前。撤回格也可能被友军占住。决定保留一个前排，比这回合多打一次伤害更重要时，就应调整位置或跳过攻击。

最后再执行。预览能解释当前交战，不保证下一回合的敌人行动；本页的算式只比较修正后的战斗力，不声称能预测固定伤害或必胜。

## 晋升路线：先分单位类型，再看目标地形

| 典型单位／职责 | 可考虑的路线 | 条件与边界 |
| --- | --- | --- |
| 剑系、火药近战、骑乘、装甲 | 冲击 I → II → III；或操练 I → II → III | 分别在开阔／崎岖目标地形战斗时每级 +15%；不是所有长矛单位都有这两条路线 |
| 弓箭、攻城、远程火药 | 精准 I → II → III；或弹幕 I → II → III | 分别针对开阔／崎岖目标格，攻击时每级 +15% |
| 能选隐蔽的前排或远程单位 | 隐蔽 I → II | 每级在防御远程单位时 +33%；不等于对一切伤害减免 33% |
| 弓箭／攻城等适用单位 | 精准 III **或** 弹幕 III → 后勤补给 | 每回合多一次攻击并可攻击后移动；还需行动力和合法目标 |
| 需要持续作战的适用单位 | 长途行军 | 弓箭／攻城可经精准 II 或弹幕 II；剑系可经冲击 III 或操练 III；允许行动后仍治疗，不是瞬间满血 |

引擎检查“适用单位类型”和“至少一个所列晋升前置”两个条件。后勤补给还有海空等其他前置，本页只列陆战相关路线，不要求把整份前置列表全部点完。政策的多个前置则是全部满足，见[政策规划](/zh/mechanics/policies/)。

“在开阔／崎岖地形战斗”看本次被攻击的地块。你在丘陵上向平原目标开火，弹幕不会因为射手站在丘陵而生效。冲击与操练适用攻防条件的写法，也不同于只在攻击时生效的精准与弹幕。



<figure class="guide-figure guide-battle">
<div class="visual-heading"><span>图解</span><strong>先排好职责，再看具体交战地形</strong></div>
<div class="battle-board"><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="后排火力地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/archer.png" alt="后排火力单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>后排火力</strong><span>先削弱单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="近战前排地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/legion.png" alt="近战前排单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>近战前排</strong><span>保护射手，保留占城单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/city-center.png" alt="目标城市地块" width="128" height="128" loading="lazy" decoding="async" /></div><strong>目标城市</strong><span>占领后仍要能守住</span></div></div><p class="visual-callout">跨河近战通常 −20%：开打前检查出发格、河流和战斗预览。</p>
<figcaption>攻城分工示意，非对局截图；位置仅表示职责，不给出固定伤害。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>

## 教学情境一：古罗马军团能否直接渡河

**条件：** 满血[古罗马军团](/zh/database/units/legion/)基础战斗力 17，准备跨河近战攻击，尚无免罚能力或有效桥路；忽略其他修正。

**选择：** 比较直接打与绕到同岸：直接跨河攻击力为 17 × (1 − 0.20) = **13.6**，同岸为 17。若另有一个己方近战单位相邻夹击，简化跨河值为 17 × (1 − 0.20 + 0.10) = **15.3**。

**代价：** 绕行耗时并可能暴露侧翼；为了凑夹击把另一个单位送进火力网，也可能得不偿失。战斗力变化不等于按同一比例直接改变最终伤害。

**复查：** 移动后重新打开预览，确认跨河项是否消失、夹击是否出现、击杀后的落点能否守住。若绕行会失去阵型，让远程先削弱目标，或守河等对方进攻。

## 教学情境二：火厢车打前排还是冲城

**条件：** [火厢车](/zh/database/units/hwach-a/)远程战斗力 26，敌军前排挡住一座城；目标区域以丘陵和森林为主，单位还没完成架设。

**选择：** 先保证架设位置、视线与护卫，用火厢车清理单位；晋升可沿弹幕走，若之后面临开阔目标则重新比较。它替代抛石机，却没有普通抛石机的 +200% 对城市攻击加成。

**代价：** 清理前排会延后打城，但能降低攻城单位被贴身摧毁的风险。不要拿 26 对 14 的远程面板比值，直接推导火厢车的攻城能力；普通抛石机的 14 在仅计其对城 +200% 时为 42，而火厢车不享受这一项。

**复查：** 分别预览单位目标和城市目标，确认可攻击、伤害与敌方反击；准备能占城的近战单位。若敌方骑兵绕后，先撤退重组，不把攻城单位的高远程值当作近身防御力。

## 常见误解与下一步

有晋升按钮不代表任何晋升都能选；有射程不代表能越过阻挡；有道路不代表本次跨河一定免罚。对城的基础特殊加成也不是所有攻城替代单位通用。遇到这些问题，先检查规则与预览，再投入升级金币。

文明应用见[罗马](/zh/strategies/rome/)、[朝鲜](/zh/strategies/korea/)、[希腊](/zh/strategies/greece/)；资源断供见[资源接入](/zh/mechanics/resources-improvements/)。完成战争后按[征服胜利](/zh/strategies/domination-victory/)判断下一座目标，或回到[机制首页](/zh/mechanics/)。
