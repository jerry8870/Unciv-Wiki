---
{
  "title": "Belief effects and religious returns: count beneficiaries first",
  "description": "Compare Pantheon, Founder, Follower and Enhancer effects, including gold, happiness, growth, culture and the cost of spreading religion.",
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

This guide targets **Gods & Kings, Standard speed, no mods, single-player Prince–King**. The situations below are constructed teaching exercises based on the rules, not played-game reports or verified win rates.

Religion pays when enough cities or followers meet the chosen conditions at an affordable cost in Faith, production and time. Read the [religion route](/strategies/religion/) for founding and enhancement, then use this page to compare returns. Religion must be enabled; the default rules have no separate religious victory.


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>Identify the beneficiary before choosing</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/faith.png" alt="Local benefits icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Local benefits</strong><span class="visual-metric">Pantheon / Follower</span><p>Check majority religion, worked tiles and buildings.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/gold.png" alt="Founder returns icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Founder returns</strong><span class="visual-metric">Followers ≠ cities</span><p>Tithe and Church Property count different things.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/missionary.png" alt="Enhance and spread icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Enhance and spread</strong><span class="visual-metric">Range / pressure / cost</span><p>Compare these separately from spread charges.</p></li>
</ol>
<figcaption>Reading map; see the text for triggers, numerical limits and tradeoffs. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>


## Who receives each belief category?

| Category | Beneficiaries and scope | What to check |
| --- | --- | --- |
| Pantheon | Cities, buildings or worked tiles matching local religious state and the belief's conditions; once incorporated into a religion, it functions as a local effect | Actual assignments and matching resources or terrain; initial coverage is not permanent |
| Founder | The founding civilization, sometimes counting qualifying cities or followers worldwide | Majority-religion city counts differ from follower counts; foreign and non-enemy filters matter |
| Follower | Qualifying cities following the religion, including other civilizations' cities | A foreign religion can provide local benefits, but buildings, follower thresholds and purchases still matter |
| Enhancer | The founder's religious effects, improving spread, units or other specified abilities | Inspect each target and condition; accepting a foreign religion does not grant all its Enhancer abilities |

The pinned engine groups Founder and Enhancer beliefs as founder effects, and Pantheon and Follower beliefs as local effects. Individual conditions still determine the result; all four categories are not awarded to every civilization that accepts the religion.

## Compare concrete returns

| Belief | Effect and condition | Useful situation |
| --- | --- | --- |
| Tithe | Founder gains +1 Gold per 4 global followers in all cities | Large follower populations, including followers in cities without a majority |
| Church Property | Founder gains +2 Gold per global city following the religion | Many stable majority-religion cities |
| Initiation Rites | Founder gains 100 Gold when a city first adopts the religion, modified by speed | Immediate first-conversion income, not recurring income or repeated conversion rewards |
| Ceremonial Burial | Founder gains +1 Happiness per global city following the religion | Happiness tied to the majority-city network |
| Asceticism / Religious Center | At least 3 / 5 local followers; +1 Happiness from a Shrine / +2 from a Temple | Existing qualifying buildings and enough followers |
| Feed the World | +1 Food from each Shrine and Temple | Local growth or specialist support |
| Fertility Rites / Swords into Ploughshares | +10% local growth / +15% local growth while at peace | Cities with a food surplus; the latter stops applying during war |
| Religious Community | +1% Production per follower, capped at 15% | Populous religious cities; not a flat +1 Production per person |
| World Church | Founder gains +1 Culture per 5 followers in foreign cities | Stable foreign followers supporting policy progress |
| Pagodas | Allows Faith purchase of Pagoda buildings in cities following the religion | A purchase plan with available Faith, not free buildings |

Followers are not the same as total city population. After a majority religion changes, recheck local beliefs and purchase permissions. Existing buildings have their own attributes; their subsequent behavior cannot be inferred from the belief's title alone.

## Match spread to the map

Holy Order reduces Missionary and Inquisitor Faith purchase costs by 30%; it does not directly strengthen each spread. Itinerant Preachers extends natural spread by 3 tiles, useful for cities newly brought within reach. Religious Texts adds 34% natural spread, then another 34 percentage points after Printing Press. Range, pressure and active spread charges are different measures.

Inspect city spacing, existing pressure and safe routes before choosing an Enhancer. Repeatedly buying Missionaries for a city that stronger foreign pressure immediately reconverts may cost more than improving your core or saving Faith. Blocked travel and lost spread opportunities also belong in the budget.

## Put the alternatives on one worksheet

Record qualifying cities, followers, existing religious buildings and worked tiles. State the minimum purchases or construction required and when returns begin. Separate recurring Gold from one-time Gold. Happiness need not be reduced to a gold figure: record which settlement or growth step it makes possible.

A larger growth percentage is not automatically better. With no food surplus it does not fix a food shortage; frequent war makes Swords into Ploughshares unreliable. Tie Culture to the next useful policy instead of spreading to distant, unstable cities merely because World Church exists.

## Teaching situation one: Tithe or Church Property

**Conditions:** A plausible network has 40 followers but only three majority-religion cities. Compare recurring base Gold, ignoring other economic modifiers.

**Choice:** Tithe gives 40 ÷ 4 = **10 Gold per turn**; Church Property gives 3 × 2 = **6**. A different plan with six stable majority cities and the same 40 followers gives Church Property 12, exceeding 10.

**Cost:** The second plan requires more spreading and protection. Comparing 12 against 10 without those costs is incomplete. The engine uses a proportion of the global follower total rather than grouping each city's followers separately into fours and discarding remainders.

**Recheck:** After spreading, inspect both majority-city count and total followers, then the religion income breakdown. Losing a majority can reduce Church Property first; Tithe also changes as actual followers change.

## Teaching situation two: another Missionary or a local benefit?

**Conditions:** Feed the World is already selected. A core city follows the religion and has a Shrine but no Temple; food limits specialists. Alternatively, Faith could spread the religion to a border city under strong hostile religious pressure.

**Choice:** Compare building a [Temple](/database/buildings/temple/) locally. The existing Shrine contributes +1 Food from the belief and the new Temple another +1, for **+2 Food per turn together**; the increase over the current situation is only +1. Prioritize border spread when it can sustain a useful benefit, complete a key quest or support founder income.

**Cost:** A Temple takes production and maintenance and may be less urgent than a Farm. A Missionary costs Faith and travel time and may be quickly countered. The budgets differ, but both compete for development opportunities.

**Recheck:** Verify whether the extra Food supports another specialist and whether construction displaced essential defense. After spreading, watch whether the majority persists rather than merely recording the animation. If the core changes religion, recalculate the local Feed the World assumption.

Beliefs are candidates, not guaranteed available choices when you found. Check current city prices for Faith purchases. The Pagodas belief grants permission; the [Pagoda building](/database/buildings/pagoda/) supplies its own benefits after purchase. Religion does not automatically complete a victory. Continue with [citizens and improvements](/mechanics/resources-improvements/), [policy planning](/mechanics/policies/), [Greece's city-state network](/strategies/greece/), or the [mechanics hub](/mechanics/).
