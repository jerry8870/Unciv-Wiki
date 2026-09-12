---
{
  "title": "Database",
  "description": "Explore civilizations, units, buildings and technologies in the 1293 Gods & Kings ruleset.",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293"
  ],
  "lastUpdated": "2026-09-12"
}
---

Use the database to check a rule before planning a turn. Values come from the pinned 4.21.20 (1293) **Gods & Kings** source snapshot.

- [Civilizations](/database/civilizations/): leaders, abilities and unique units or buildings.
- [Units](/database/units/): combat values, movement, upgrades and technology requirements.
- [Buildings and wonders](/database/buildings/): base production costs, yields and replacements.
- [Technologies](/database/technologies/): base research costs, prerequisites and unlocks.

## Reading the numbers

These are **ruleset base values**. A technology without an explicit nonzero cost inherits its column's research cost. A building with the default cost of −1 inherits the building or wonder cost of its latest required technology column, unless it is unbuildable. An explicit zero stays zero; a religious building marked unbuildable cannot be directly produced just because its listed base value is zero.

Read [cost mechanics](/mechanics/) for examples and the distinction between source values and prices in a real game. The [first-game guide](/getting-started/) shows how to use these entries while learning.
