---
{
  "title": "战斗与攻城：站位、集火、轮换和占领",
  "description": "从防守阵型到攻城回合顺序，解释远程与近战分工、攻城器械部署、残血撤退及战后处理。",
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

本篇面向 **Gods & Kings** 的常规陆战。单位能力、晋升与地形会改变可执行动作，因此行动前应查看战斗预览。这里的编队是练习方案，不是保证战胜同等或高科技敌人的固定配方。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>攻城的三个职责</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/archer.png" alt="远程部队图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>远程部队</strong><span class="visual-metric">先削弱</span><p>集中火力，先消除危险反击。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/catapult.png" alt="投石车图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>投石车</strong><span class="visual-metric">安全架设</span><p>视线、射程和护卫缺一不可。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/warrior.png" alt="近战部队图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>近战部队</strong><span class="visual-metric">占领并守住</span><p>保留能进城且能存活的单位。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>


## 先定义一次战斗的目的

防守是保护城市、资源与有经验的单位；攻城是清除守军后，让能够占领的单位接管城市。若你的目的只是解除入侵，就不必为了追击一个残血敌兵离开防线。如果目的是占首都，也不必顺路攻下每一座偏远城市。

开战前看三件事：敌我主要单位的科技代差，敌军能从哪些方向到达，受伤单位有没有后退位置。面板里的总兵力无法替代局部判断；远在另一片大陆的军队不能帮你挡住本回合的进攻。

## 用角色组织编队

| 角色 | 主要工作 | 常见失误 |
| --- | --- | --- |
| 近战前排 | 挡住敌军、保护远程、最后占城 | 满血时也连续撞高防御城市，失去占领单位 |
| 远程单位 | 集火清除敌人，在安全位置削城 | 没有视野或射线，进入位置后才发现不能打 |
| 攻城器械 | 对城市提供集中火力 | 脱离护卫、忘记架设要求 |
| 机动单位 | 侦察、阻断援军、侧翼和追击 | 为击杀一个目标冲进数个敌人的攻击范围 |
| 预备队 | 换下受伤前排、补缺口 | 所有单位同时压上，下一回合无人接替 |

古典时代可用“两名前排、数个弓系单位，条件允许再加攻城器械”练习分工。实际数量由道路宽度、敌军规模和预算决定。狭窄山口容不下的多余前排，可能不如后方一支预备队有用。

## 防守：让敌人先进入你能集火的位置

把前排放在适合防守的地形或城市附近，远程放在可以攻击、又不容易被近战接触的位置。保留一条退路，不要把工人或其他单位堵在撤退格上。遇到河流、丘陵和森林时，分别确认移动消耗、攻击修正和视线；“看起来只隔两格”不保证能射击。

敌人进入射程后，优先处理能在下一回合杀伤你关键单位的威胁，例如贴近弓兵的近战或危险攻城器械。能安全消灭一个敌人时，集中火力通常比把多名敌人都打成轻伤更容易减少反击。若某个残血目标需要你暴露整条阵线才能击杀，就放弃追击。

一次攻击会改变后续预览。先用可安全输出的远程火力，再决定是否值得用近战补刀；不要在行动前一次性假定所有结果。

## 攻城前先赢野战

如果敌人的野战军还完整，就让攻城器械先到城下，往往只是给对方送经验。先在有利地形削减援军，侦察城市另一侧，确认没有敌人能突然接触你的脆弱部队。受伤的军队应该先轮换治疗，而不是因为已经走到城边就必须继续打。

[投石车](/zh/database/units/catapult/)拥有对城市攻击加成，但需要架设才能远程攻击，而且没有防御地形加成。出发前就规划安全部署格；移动、架设、射击能否在同一回合完成，要看剩余移动与单位规则。攻城器械不是普通弓兵的直接替代，也需要前排与视野。



<figure class="guide-figure guide-battle">
<div class="visual-heading"><span>图解</span><strong>先排好职责，再看具体交战地形</strong></div>
<div class="battle-board"><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="后排火力地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/archer.png" alt="后排火力单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>后排火力</strong><span>先削弱单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="近战前排地块" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/legion.png" alt="近战前排单位" width="80" height="80" loading="lazy" decoding="async" /></div><strong>近战前排</strong><span>保护射手，保留占城单位</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/city-center.png" alt="目标城市地块" width="128" height="128" loading="lazy" decoding="async" /></div><strong>目标城市</strong><span>占领后仍要能守住</span></div></div><p class="visual-callout">跨河近战通常 −20%：开打前检查出发格、河流和战斗预览。</p>
<figcaption>攻城分工示意，非对局截图；位置仅表示职责，不给出固定伤害。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>

## 一个攻城回合的行动顺序

1. **确认退路与威胁。** 先检查新出现的援军、受伤单位和城市周围的空位。若阵型已被突破，优先撤退或修补。
2. **清理能反击的敌军。** 用远程与其他安全攻击处理贴近阵线的目标，避免只顾打城。
3. **用已就位的火力削减城市。** 逐次查看城市剩余生命，给最后行动留出判断空间。
4. **重新检查占领预览。** 普通远程轰击无法完成占领；需要本身能够占领的单位发起合适的近战攻击。
5. **占城后立即考虑防守。** 占领单位通常已受伤，城市也可能遭到反扑。让支援部队准备拦截，而不是全部远离。

这个顺序可以根据敌军布局变化。关键是始终保留一个能完成占领且能承受后果的单位；如果它已经濒死，推迟一回合通常比强行接管后立刻丢城更合理。

## 轮换比反复补兵更能保持战力

在受伤单位仍有安全退路时撤下它，用预备队顶上。治疗速度与所在地、动作和能力有关，不应假设任何单位移动后都能正常治疗。结束回合前检查实际状态，尽量让治疗单位远离下一轮集火。

升级前确认科技、资源、金币和单位位置满足条件；最好在发动下一轮攻势前完成，而不是在敌方城市火力下临时等待升级。高级晋升单位难以快速替补，保护它们有时比多杀一个普通敌兵更有价值。

## 教学情境：城市只剩少量生命，为什么还不占

假设弓兵已将城市打到低生命，你唯一能占领的战士也已重伤，城后又出现一个敌方近战单位。直接冲进去可能触发占领，却在下一回合被夺回。

更稳妥的处理是：先攻击接近的援军，让另一支前排靠近；如果来不及，保持安全火力、撤回战士治疗，等能够守住的回合再接管。城的生命数字只是一个条件，部队存活和敌方反攻能力同样重要。这是构造情境，没有预设伤害数值或固定胜率。

## 战后检查与停止条件

检查抵抗与快乐、资源是否恢复、补给路线是否通畅，再决定傀儡或兼并等城市处理。若科技落后、补兵速度跟不上损失，或另一侧出现威胁，应寻求停战与整备。不要因为已经宣战就把全部经济投入无止境的消耗。

下一步阅读[征服胜利的战役规划](/zh/strategies/domination-victory/)。若在收集战斗成就，战术成功与成就判定是两件事，另看[成就排查](/zh/guides/achievement-troubleshooting/)。

## 相关机制与文明决策

- [地形、战斗修正与晋升](/zh/mechanics/combat-promotions/)
- [罗马：建设与军事窗口](/zh/strategies/rome/)
- [朝鲜：专家与首都建设](/zh/strategies/korea/)
