---
{
  "title": "游戏机制：实操决策与基础花费",
  "description": "政策、市民与资源、战斗与晋升、宗教信条四篇机制实操，并保留原科研和生产花费说明。",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293"
  ],
  "lastUpdated": "2026-09-12"
}
---

数据库使用 **Gods & Kings 规则集基础值**，不计算实时对局中的最终价格。本页依据固定提交中的科技加载与建筑花费逻辑。

## 机制实操目录

四篇面向标准速度、无模组、单人王子至国王玩家的机制实操；每篇包含规则对照与两个构造的教学情境。

- [政策选择与分支规划](/zh/mechanics/policies/)
- [市民、资源与改良](/zh/mechanics/resources-improvements/)
- [地形、战斗修正与晋升](/zh/mechanics/combat-promotions/)
- [信条效果与宗教收益](/zh/mechanics/religion-beliefs/)

[文明与胜利攻略](/zh/strategies/)把这些规则接入完整对局。以下保留原基础花费说明。


## 科技：科技列提供默认花费

科技没有写花费，或花费为零时，继承所在科技列的 `techCost`；显式非零值则覆盖默认值。例如，[文字](/zh/database/technologies/writing/)继承基础科研花费 **55**。

实际研究价格还可能受到游戏速度、难度、文明及对局状态修正。当前科技还需多少科研点，以游戏内科技面板为准。

## 建筑与奇观：选择对应的科技列价格

建筑在源码中的默认造价是 −1。保留默认值且没有不可建造标记时，引擎选择其所需科技中最新的一列：普通建筑继承 `buildingCost`，世界奇观和国家奇观继承 `wonderCost`。

| 实例 | 基础值 | 原因 |
| --- | --- | --- |
| [图书馆](/zh/database/buildings/library/) | 75 | 继承文字所在列的建筑造价 |
| [大图书馆](/zh/database/buildings/the-great-library/) | 185 | 继承文字所在列的奇观造价 |
| [神社](/zh/database/buildings/shrine/) | 40 | 使用显式数值 |
| [宫殿](/zh/database/buildings/palace/) | 0 | 显式零值保持为零 |
| [大教堂](/zh/database/buildings/cathedral/) | 0，不可直接建造 | 显式零值加不可建造规则，不表示能在城市中免费生产 |

## 为什么城市界面显示不同价格

建筑花费可能先加上按城市数或已建数量计算的成本，再应用规则百分比、人类或 AI 的难度修正，以及游戏速度倍率。世界奇观与普通建筑的修正并不总是相同；购买也不同于投入生产力建造。

基础值适合比较，但不能直接减去当前生产力就当作精确完工回合。请查看城市面板及当前效果，再通过[数据库](/zh/database/)追踪建筑的需求与替代关系。
