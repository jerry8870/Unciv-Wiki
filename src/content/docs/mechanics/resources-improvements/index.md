---
{
  "title": "Citizens, resources and improvements: connect, then work",
  "description": "Separate worked-tile yields from resource access, calculate specialist food tradeoffs, and prioritize Workers, Academies and roads.",
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

Good terrain does not produce everything shown merely because it lies inside your borders. Conversely, an unworked resource can still supply your empire. Check assignments in the city screen and availability in the resource overview before deciding what a Worker should do next.


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>One tile, two different benefits</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/unit/worker.png" alt="Complete the improvement icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Complete the improvement</strong><span class="visual-metric">Connect the resource</span><p>Check ownership, reveal, technology and pillaging.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/population.png" alt="Assign a citizen icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Assign a citizen</strong><span class="visual-metric">Collect tile yields</span><p>Food and Science from the tile normally need a worker.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/science.png" alt="Specialist tradeoff icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Specialist tradeoff</strong><span class="visual-metric">What work is displaced?</span><p>Leaving a Farm loses food; it does not add population.</p></li>
</ol>
<figcaption>Reading map; see the text for triggers, numerical limits and tradeoffs. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>


## Separate three kinds of availability

| Object | Requirement for the benefit | Important distinction |
| --- | --- | --- |
| Ordinary tile yields | A citizen works an eligible city tile; the city center is counted separately | Owning land does not collect every tile's yields |
| Domestic luxury or strategic resource | Owned, revealed, appropriately improved and unpillaged, with required technology | Resource access does not require a citizen working it or a road to the deposit |
| Resource under a city center | Revealed, with technology for an eligible extraction improvement | Settlement does not bypass reveal and extraction technology |
| Strategic resource under a Great Improvement | Revealed, with an unpillaged Great Improvement | This exception does not automatically connect luxuries |
| Specialist slot | The building exists and a citizen is assigned | An empty slot gives neither specialist yields nor great-person points |
| Road | A useful connection or movement route, with segment maintenance | Roads do not provide food or serve as a prerequisite for mining resources |

Trades, allies and unit consumption also affect available resources; this table concerns domestic tiles. If Iron exists but a unit cannot be built, distinguish total connected supply from the remainder after consumption, then check technology and replacement requirements.

## Useful tile and specialist comparisons

| Object | Base effect or prerequisite | Practical meaning |
| --- | --- | --- |
| Grassland Farm | 2 Food from Grassland plus 1 from Farm; Agriculture | 3 Food without other effects, useful for growth and specialists |
| Hill Mine | 2 Production from Hill plus 1 from Mine; Mining | 3 Production without resources or other effects, normally no food |
| Later Farms | Civil Service adds 1 Food to fresh-water Farms; Fertilizer adds 1 to non-fresh-water Farms | These are different conditions, not two bonuses on every Farm |
| Scientist | 3 Science and 3 Great Scientist points | Needs a slot; the citizen still consumes food |
| Engineer / Artist / Merchant | 2 Production / 2 Culture / 3 Gold, plus 3 corresponding great-person points | Compare against the tile that citizen would otherwise work |
| Academy | 8 base Science; Scientific Theory and Atomic Theory each add 2 | Must be worked; placement removes removable features |
| Road | 1 base Gold maintenance per segment per turn | Build when connection or military value justifies upkeep |

Covering features can replace terrain yields; resources can add more. Check the actual tile and improvement preview rather than applying the simple Grassland and Hill examples everywhere. Iron is revealed by Iron Working and connected by a Mine; Horses by Animal Husbandry and a Pasture. Wheat is a bonus resource improved with a Farm, not a strategic stockpile.



<figure class="guide-figure guide-land">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>Inspect the tiles actually being worked</strong></div>
<ul class="visual-flow visual-terrain"><li><img class="terrain-art" src="/game-assets/tile/grassland-farm.png" alt="Grassland Farm tile" width="112" height="112" loading="lazy" decoding="async" /><strong>Grassland Farm</strong><span class="visual-metric">3 Food</span><p>Grassland 2 + Farm 1, before other effects.</p></li><li><img class="terrain-art" src="/game-assets/tile/hill.png" alt="Hill tile" width="112" height="112" loading="lazy" decoding="async" /><strong>Hill</strong><span class="visual-metric">2 Production</span><p>A Mine can add 1; check food support first.</p></li><li><img class="terrain-art" src="/game-assets/tile/academy.png" alt="Academy tile" width="112" height="112" loading="lazy" decoding="async" /><strong>Academy</strong><span class="visual-metric">+8 base Science</span><p>Work it consistently and account for the displaced improvement.</p></li></ul>
<figcaption>Tile comparison; base values exclude resources and later technologies. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>

## Worker priorities follow the bottleneck

First ensure a safe route and retreat. Repair pillaged tiles causing supply or yield losses, then compare a new luxury, an immediately needed strategic resource, and worked tiles short of food or production. An ordinary improvement that nobody will work soon can usually wait.

A new luxury that resolves unhappiness can precede a second Farm. Duplicate luxuries may support trade, but each copy is not another distinct luxury type for happiness. Travel is also a cost: group jobs locally instead of marching one Worker repeatedly across the empire.

Before laying roads, count missing segments, confirm the completed route will connect the cities, and budget maintenance. Military roads can justify a financial loss if they solve a specific reinforcement delay. An unfinished route is not a completed city connection.

## Specialists are existing citizens

Population normally consumes 2 Food per person, including specialists. Moving a farmer into a Scientist slot does not add another person's food consumption; it removes the former tile's food. Effects such as Freedom's Civil Society can separately change specialist food use.

Record total food and consumption, move one citizen, then compare food surplus, science and essential construction time. Automatic assignments, locked tiles and specialist controls can affect the result. Recheck after growth, improvements or starvation. Sustainable staffing is more useful than filling every available slot.

## Teaching situation one: two University Scientists

**Conditions:** An eight-population city produces 22 Food and normally consumes 16, leaving +6. Two citizens each work a 3-Food Farm. A [University](/database/buildings/university/) has two empty slots. Ignore other food and science modifiers.

**Choice:** Assign both as Scientists: food falls to 16, consumption stays 16, and surplus becomes zero. They add **6 base Science** and 6 base Great Scientist points per turn. Assigning one instead retains +3 surplus and adds 3 Science and 3 points.

**Cost:** Full staffing stops growth under these simplified conditions and may delay the ninth citizen. The 6 Science is not free.

**Recheck:** Staff one slot first if growth matters soon or external food may disappear. Read the final science breakdown. [Korea](/strategies/korea/) changes specialist Science while [Babylon](/strategies/babylon/) changes Great Scientist points, so their final figures differ.

## Teaching situation two: an Academy and resource access

**Conditions:** An early Great Scientist can create an Academy on safe Grassland or a frontier Iron tile. A citizen can keep working the Grassland; the border is frequently pillaged.

**Choice:** Favor the safe, continuously workable candidate. Counting only the Academy's new science, 25 worked turns yield 25 × 8 = **200 base Science**, before percentages, later technologies and the opportunity cost of displaced improvements.

**Cost:** The Scientist is consumed and the tile cannot retain an ordinary improvement alongside the Academy. Replacing a Farm also sacrifices food. A frontier Academy can connect revealed strategic resources yet lose its science contribution if unworked or pillaged.

**Recheck:** Inspect feature removal and resource warnings before placement; afterward confirm the assignment and resource overview. Do not extend the strategic-resource exception to an Academy replacing a luxury's Plantation.

Growth bonuses generally apply to food available for growth, not every unit of gross food. Science, construction and great-person points use separate accounts; Settler food conversion needs its own production breakdown. Continue with [expansion and economy](/strategies/expansion-economy/), [policies](/mechanics/policies/), [beliefs](/mechanics/religion-beliefs/) and [Rome's construction schedule](/strategies/rome/). The [mechanics hub](/mechanics/) retains the base-cost reference.
