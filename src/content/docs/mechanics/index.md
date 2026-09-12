---
{
  "title": "Game mechanics: decisions and base costs",
  "description": "Practical guides to policies, citizens, resources, combat and religion, with the original research and production cost reference.",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293"
  ],
  "lastUpdated": "2026-09-12"
}
---

The database uses **Gods & Kings base values**. It does not calculate a live game's final price. This explanation follows the pinned engine's technology loading and building-cost rules.

## Practical mechanics guides

Four guides for Standard-speed, unmodded Prince–King single-player learning. Each has rule comparisons and two constructed teaching situations.

- [Policy planning](/mechanics/policies/)
- [Citizens, resources and improvements](/mechanics/resources-improvements/)
- [Terrain, combat modifiers and promotions](/mechanics/combat-promotions/)
- [Belief effects and religious returns](/mechanics/religion-beliefs/)

[Civilization and victory guides](/strategies/) apply these rules to a complete game. The original cost reference follows.


## Technology: a column supplies the default

A technology with no cost, or a cost of zero, inherits `techCost` from its technology column. An explicit nonzero value overrides that default. For example, [Writing](/database/technologies/writing/) inherits a base research cost of **55**.

The price shown during play can also reflect game speed, difficulty and civilization/game-state modifiers. Use the in-game technology panel for the current research target's actual remaining cost.

## Buildings and wonders: use the appropriate column value

A building's default source cost is −1. When that default is present and the building is not marked unbuildable, the engine uses the latest required technology column. Ordinary buildings inherit `buildingCost`; world and national wonders inherit `wonderCost`.

| Example | Base value | Why |
| --- | --- | --- |
| [Library](/database/buildings/library/) | 75 | Inherits Writing's building cost |
| [Great Library](/database/buildings/the-great-library/) | 185 | Inherits Writing's wonder cost |
| [Shrine](/database/buildings/shrine/) | 40 | Explicit source value |
| [Palace](/database/buildings/palace/) | 0 | Explicit zero is preserved |
| [Cathedral](/database/buildings/cathedral/) | 0, not directly buildable | Explicit zero plus an Unbuildable rule; not free city production |

## Why the city panel can show another price

The building calculation can add per-city or previously-built costs, apply unique rule percentages, distinguish human and AI difficulty modifiers, and scale with game speed. World-wonder and ordinary-building modifiers need not be identical. Purchasing is also a different operation from spending production.

A base value is useful for comparison, but do not subtract it from your current production and call the result an exact completion time. Read the city panel and its active effects. [Browse the database](/database/) to follow a building's requirements and replacements.
