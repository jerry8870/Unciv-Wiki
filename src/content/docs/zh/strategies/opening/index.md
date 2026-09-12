---
{
  "title": "前 50 回合：从落地到稳定扩张",
  "description": "按探索、首都建设、第二城和防守窗口拆解开局，提供建造与科研分支、教学情境和回合检查表。",
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

这是一条面向单人练习局的开局路线：**Gods & Kings、远古开局、标准速度、无模组**，建议先在王子或更低难度使用。回合区间只是安排练习的参考；地图、遗迹、文明能力和邻国会改变节奏。先达成阶段目标，再进入下一阶段，不必追赶某个回合数字。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>先侦察，再兑现资源，最后扩张</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/scout.png" alt="斥候图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>斥候</strong><span class="visual-metric">看清局势</span><p>先确认城址、邻国与安全路线。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/worker.png" alt="工人图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>工人</strong><span class="visual-metric">让地块有用</span><p>优先资源接入和正在工作的地块。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/settler.png" alt="开拓者图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>开拓者</strong><span class="visual-metric">带着护卫落城</span><p>快乐、金币与防守允许时再扩张。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>



### 开局单位优先级速查

| 单位 | 什么时候优先 | 下一步复查 |
| --- | --- | --- |
| <img class="table-icon" src="/game-assets/unit/scout.png" alt="斥候图标" width="32" height="32" loading="lazy" decoding="async" /> 斥候 | 周边城址和邻国仍不清楚 | 先了解威胁，别盲目送出开拓者 |
| <img class="table-icon" src="/game-assets/unit/worker.png" alt="工人图标" width="32" height="32" loading="lazy" decoding="async" /> 工人 | 有安全的资源或工作地块等待改良 | 改良完成后复查市民分配与库存 |
| <img class="table-icon" src="/game-assets/unit/archer.png" alt="弓箭手图标" width="32" height="32" loading="lazy" decoding="async" /> 弓箭手 | 敌军已靠近核心 | 保护工人和城市，再恢复发展 |
| <img class="table-icon" src="/game-assets/unit/settler.png" alt="开拓者图标" width="32" height="32" loading="lazy" decoding="async" /> 开拓者 | 已有可守城址与快乐、金币余量 | 派护卫，并安排新城的资源接入 |

## 开局先回答三件事

第一，你附近有什么可以尽快改良并实际工作的食物地块？第二，哪一种奢侈资源能支持下一轮人口和城市增长？第三，敌军从哪个方向接近？这三件事分别决定人口、扩张上限和防守开支。

建首都时，优先比较眼前可用的食物与生产力、淡水、奢侈资源和防守地形。为了已经看到的明显收益移动一次可以考虑；为了寻找未知的“完美位置”连续游荡，通常只会延迟所有建设。山地可为以后符合条件的[天文台](/zh/database/buildings/observatory/)提供机会，但不能代替开局的食物与生产。

## 约第 1–15 回合：建立信息和生产循环

用初始军事单位绕首都侦察，确认周边城址和蛮族来路，再逐步扩大探索范围。新造[斥候](/zh/database/units/scout/)去较远方向，避免所有单位同路行进。工人、移民经过黑暗地带时要有人探路。

可把“斥候 → 纪念碑 → 工人”作为第一条练习队列，但每完成一个项目都重新判断：

| 看到的局势 | 优先调整 | 为什么 |
| --- | --- | --- |
| 蛮族靠近，首都周围没有能回援的部队 | 提前弓箭手或其他可用守军 | 工人被抓后，早造出的优势会消失 |
| 可改良资源就在市民工作范围内，所需科技即将完成 | 提前工人 | 工人到位后能立即产生收益 |
| 暂时没有合适改良或资源科技未到 | 先纪念碑、粮仓或守军 | 避免让工人空等或暴露在外 |
| 首都食物不足，新增人口很慢 | 检查工作地块，再考虑粮仓 | 建筑不能修复错误的市民分配 |

研究顺序也从土地出发。需要开矿就准备采矿，需要种植园就沿科技树走向历法，需要猎场就看捕猎；不要因为指南提到[文字](/zh/database/technologies/writing/)就跳过眼前能解决快乐和食物的科技。[图书馆](/zh/database/buildings/library/)值得规划，但没有人口和生产力时，过早排队可能拖延基本建设。

## 约第 15–30 回合：为第二城准备一整套条件

生产移民前，先在地图上选定目的地并写下用途，例如“拿到第二种奢侈品、守住东侧河谷”。只说“多一座城”不够具体。再检查护送单位、道路上的蛮族、建城后的快乐余量，以及工人是否能跟进。

新城不需要离首都最远。较近的城市容易支援，连接成本较低，也更容易分享已有改良；过远的资源点可能要求额外军队和很长的道路。看工作范围内有多少早期可用地块，比只看最终边界能圈住多少资源更有帮助。

政策可先在两种思路中选一条：**传统政策**适合优先养好首都和少数城市；**自主政策（Liberty）** 适合有扩张空间，并能承受新城成本的局面。自主政策中的免费移民、工人有实际帮助，但免费单位不等于免费城市。第一次学习时，集中推进一条分支，观察其完成奖励，再考虑跨分支选择。



<figure class="guide-figure guide-land">
<div class="visual-heading"><span>图解</span><strong>先看正在工作的地块</strong></div>
<ul class="visual-flow visual-terrain"><li><img class="terrain-art" src="/game-assets/tile/grassland-farm.png" alt="草原农场地块" width="112" height="112" loading="lazy" decoding="async" /><strong>草原农场</strong><span class="visual-metric">3 食物</span><p>草原 2 + 农场 1，未计其他修正。</p></li><li><img class="terrain-art" src="/game-assets/tile/hill.png" alt="丘陵地块" width="112" height="112" loading="lazy" decoding="async" /><strong>丘陵</strong><span class="visual-metric">2 生产力</span><p>矿井可再加 1；先看粮食能否支持。</p></li><li><img class="terrain-art" src="/game-assets/tile/academy.png" alt="学院地块" width="112" height="112" loading="lazy" decoding="async" /><strong>学院</strong><span class="visual-metric">+8 基础科研</span><p>需要持续工作，并扣除被替代改良的机会成本。</p></li></ul>
<figcaption>地块对照示意；基础值不含资源与后续科技修正。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>

## 约第 30–50 回合：让新城开始回报投入

新城优先解决食物、文化扩地、可用资源与最低防御，而不是复制首都全部建筑。工人先改良马上能工作的高价值地块；奢侈资源提供的帝国资源用途，也要单独考虑。确认人口增长后新市民没有被分配到低效地块。

如果继续和平发展，规划图书馆和[国立研究院](/zh/database/buildings/national-college/)的节奏。国立研究院要求所有非傀儡城市建有图书馆，刚建的低产城市可能拖住它。可以先完成一轮扩张再补齐图书馆，也可以先完成国立研究院再扩张；取舍取决于好城址会不会被占走、下一城能多快建成图书馆。不要把“永远先国立研究院”当成规则。

这时至少确认一个可靠防线：敌军接近时谁挡路、谁远程输出、受伤单位往哪里退。前线城市可以暂停经济建筑补兵，后方继续发展。若连续造移民导致快乐或财政紧张，先停下来修复，不必为了凑城市数量继续扩张。

## 教学情境：第三个生产项目怎么选

假设斥候和纪念碑已完成，西边发现可用奢侈品，东边有蛮族营地，现有战士离首都较远。这是构造的决策练习，不是实战战报。

1. 先判断营地是否能威胁工人路线；若能，第三项改为守军，并让战士回到可支援位置。
2. 科研准备奢侈品所需的改良科技，避免守军完成后工人仍然无事可做。
3. 营地威胁解除、资源能改良后再造工人；同时考察西侧第二城。
4. 第二城若与强邻接壤，把防御预算算进去；若因此无力维持，先选择更近的安全城址。

你推迟了一个经济项目，却保住了工人和扩张路线。判断这步是否值得，看后续是否恢复生产与改良，而不是只比较谁更早造出工人。

## 出现偏差时如何补救

- **人口不长：** 检查净食物和市民分配，确认是不是为了短期赶工长期占满矿山或专家槽。
- **总被蛮族抓工人：** 停止向未探明区域自动移动，先用军事单位建立安全通道。
- **第二城建好后全面缺钱：** 暂停长道路和额外军队，检查新建筑维护、单位维护及城市连接；见[扩张与经济](/zh/strategies/expansion-economy/)。
- **邻国提前进攻：** 暂停奇观和移民，利用城市与地形集中防守；不要让部队逐个赶到前线送掉。

结束本阶段的标准是：你知道下一座城为什么值得建，首都和新城都在做有用途的项目，军事单位能保护关键地块，下一项科技解决一个具体问题。达到这些标准后，从[攻略目录](/zh/strategies/)选择胜利路线。

## 相关机制与文明决策

- [市民、资源与改良](/zh/mechanics/resources-improvements/)
- [巴比伦：早期大科学家](/zh/strategies/babylon/)
- [罗马：建设与军事窗口](/zh/strategies/rome/)
