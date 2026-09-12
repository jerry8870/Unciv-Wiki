---
{
  "title": "数据库总览",
  "description": "查询 Gods & Kings 规则集的文明、单位、建筑、奇观和科技。",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293"
  ],
  "lastUpdated": "2026-09-12"
}
---

在规划下一回合前，先查清规则。本数据库使用固定的 **Gods & Kings** 源码快照。

- [文明](/zh/database/civilizations/)：领袖、能力以及专属单位和建筑。
- [单位](/zh/database/units/)：战斗力、移动力、升级与科技要求。
- [建筑与奇观](/zh/database/buildings/)：基础生产造价、产出和替代关系。
- [科技](/zh/database/technologies/)：基础科研花费、前置科技与解锁内容。

## 怎样理解数值

页面列出的是**规则集基础数值**。科技没有显式非零花费时，继承所在科技列的科研花费。建筑默认造价为 −1 时，除不可建造项目外，继承其所需科技中最新一列的建筑或奇观造价。显式零值保持为零；标记不可建造的宗教建筑不能因为显示零值就直接生产。

[花费机制](/zh/mechanics/)用实例解释基础值和实际对局价格的差别。[新手第一局指南](/zh/getting-started/)介绍如何边玩边查。
