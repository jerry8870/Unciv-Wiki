---
{
  "title": "Terrain, combat modifiers and promotions: read the preview first",
  "description": "Use rivers, terrain, movement and visibility to choose engagements, verify promotion prerequisites, and practice attack or retreat decisions.",
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

Base strength is one input. Check movement, visibility and firing access before reading combat modifiers and committing to an attack. Use [combat and sieges](/strategies/combat-siege/) for formations; this page explains an individual engagement.


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>Three checks before attacking</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/scouting.png" alt="Position and sight icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Position and sight</strong><span class="visual-metric">Check a legal attack</span><p>Range alone does not guarantee sight or actions.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/shock.png" alt="Combat modifiers icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Combat modifiers</strong><span class="visual-metric">Read the target tile</span><p>Evaluate rivers, flanking, terrain and wounds.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/logistics.png" alt="Promotion route icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Promotion route</strong><span class="visual-metric">Type + any prerequisite</span><p>Follow an eligible route, not every listed branch.</p></li>
</ol>
<figcaption>Reading map; see the text for triggers, numerical limits and tradeoffs. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>


## What terrain changes

| Condition | Pinned rule | Practical check |
| --- | --- | --- |
| Ordinary Grassland / Plains | Base movement cost 1, no terrain defense bonus | Easy movement does not give the front line extra protection |
| Hill, Forest, Jungle | Base movement cost 2; each has 25% defense | Check remaining movement; units with no defensive terrain bonus do not receive the positive bonus |
| Forest on Hill | The relevant maximum feature defense is used, normally 25% | Forest and Hill do not add to 50%; improvements such as Forts are separate |
| Marsh | Base movement cost 3, −15% defense | Visually complex terrain is not necessarily protective |
| Melee attack across a river | Normally −20% attack modifier | A river-attack exception, or effective connections on both ends plus bridge technology, can remove it |
| Forest / Jungle sight | Can block sight at the same elevation; Hills affect elevation calculations | Being inside range does not guarantee line of sight |
| Flanking | Each additional adjacent friendly melee unit provides a base +10% to a melee attack | A nearby ranged unit is not automatically a flanker; preview again after moving support |

Roads, rivers, unit abilities and enemy zones of control can change movement; these are not final costs for every unit. Ranged attacks do not inherit the ordinary melee river-attack penalty. Siege units may also need setup and sufficient actions to fire.

## Read the preview in order

Select the intended target and verify the actual attack origin. Inspect terrain, river, promotion, flanking and missing-resource modifiers. Confirm whether the attack uses melee or ranged strength. Wounds affect damage output, so a damaged unit should not be evaluated like a healthy one.

Next inspect enemy retaliation. A melee kill may move the attacker onto the target tile, exposing it to two ranged units. Friendly units may block the planned retreat. If preserving the front line matters more than this turn's damage, reposition or decline the attack.

Execute only after that review. The preview describes the current exchange, not the enemy's next decisions. The calculations below compare modified strength; they do not promise fixed damage or victory.

## Promotion routes depend on unit type and target terrain

| Typical unit or job | Candidate route | Conditions and limits |
| --- | --- | --- |
| Sword, Gunpowder, Mounted, Armored | Shock I → II → III, or Drill I → II → III | Each tier gives +15% fighting on open or rough target terrain respectively; not every spear unit has these routes |
| Archery, Siege, Ranged Gunpowder | Accuracy I → II → III, or Barrage I → II → III | Each tier gives +15% when attacking open or rough target terrain respectively |
| Eligible front-line or ranged units | Cover I → II | Each tier gives +33% strength defending against ranged units, not a universal 33% damage reduction |
| Eligible Archery / Siege units | Accuracy III **or** Barrage III → Logistics | One additional attack and movement after attacking; legal targets and movement still matter |
| Eligible sustained-combat units | March | Archery / Siege can approach through Accuracy II or Barrage II; Sword units through Shock III or Drill III; permits healing after actions, not instant full health |

The engine requires an eligible unit type and **at least one** listed promotion prerequisite. Logistics has other naval and air routes outside this land-combat table; you do not need every listed prerequisite. This differs from [policies](/mechanics/policies/), whose multiple prerequisites must all be satisfied.

Open or rough combat terrain means the attacked tile. Firing from a Hill at a Plains target does not activate Barrage just because the shooter stands on rough ground. Shock and Drill also have different attack/defense applicability from attack-only Accuracy and Barrage.



<figure class="guide-figure guide-battle">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>Assign roles, then inspect the actual terrain</strong></div>
<div class="battle-board"><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="Rear-line fire tile" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/archer.png" alt="Rear-line fire unit" width="80" height="80" loading="lazy" decoding="async" /></div><strong>Rear-line fire</strong><span>Soften enemy troops</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/grassland.png" alt="Melee screen tile" width="128" height="128" loading="lazy" decoding="async" /><img class="piece" src="/game-assets/sprite/legion.png" alt="Melee screen unit" width="80" height="80" loading="lazy" decoding="async" /></div><strong>Melee screen</strong><span>Protect shooters and preserve a capturer</span></div><div class="battle-position"><div class="tile-stack"><img class="ground" src="/game-assets/tile/city-center.png" alt="Target city tile" width="128" height="128" loading="lazy" decoding="async" /></div><strong>Target city</strong><span>Plan to hold after capture</span></div></div><p class="visual-callout">Melee river attacks normally incur −20%: check the origin, river and preview first.</p>
<figcaption>Siege-role illustration, not a match screenshot; positions show jobs, not fixed damage. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>

## Teaching situation one: should a Legion cross the river?

**Conditions:** A healthy [Legion](/database/units/legion/) has 17 base strength and would attack across a river without a relevant exemption or effective bridge connection. Ignore other modifiers.

**Choice:** Compare a direct attack with reaching the same bank: crossing gives 17 × (1 − 0.20) = **13.6**, versus 17 on the same bank. With one additional adjacent friendly melee flanker, the simplified crossing value is 17 × (1 − 0.20 + 0.10) = **15.3**.

**Cost:** Detouring takes time and may expose a flank. Moving support into danger just to create flanking can also be a losing trade. Strength changes do not translate directly into proportional final damage.

**Recheck:** Preview after movement. Verify whether the river modifier disappears, flanking appears, and the post-kill tile is defensible. If detouring breaks formation, soften the target at range or defend your bank instead.

## Teaching situation two: Hwach'a versus troops or a city

**Conditions:** A [Hwach'a](/database/units/hwach-a/) has 26 ranged strength. An enemy front line screens a city in mostly Hills and Forests; your unit has not set up.

**Choice:** Secure a firing position, sight and escorts, then clear units. Barrage fits rough target tiles; reconsider if subsequent targets are open. Hwach'a replaces Trebuchet but lacks the ordinary Trebuchet's +200% city-attack bonus.

**Cost:** Clearing troops delays city attacks but protects your siege unit from close assault. Do not infer city performance from 26 versus 14 ranged strength: an ordinary Trebuchet's 14 becomes 42 when counting only its +200% city bonus, while Hwach'a lacks that modifier.

**Recheck:** Preview both troop and city targets, legal attacks, damage and retaliation. Keep a melee unit able to capture the city. If cavalry penetrates the rear, retreat and reform; ranged strength is not close-defense strength.

A promotion notification does not unlock every promotion. Range does not bypass sight blockers, and a road does not always remove a river penalty. Check rules and previews before paying for upgrades. See [Rome](/strategies/rome/), [Korea](/strategies/korea/) and [Greece](/strategies/greece/) for applications, [resource access](/mechanics/resources-improvements/) for supply problems, and [domination victory](/strategies/domination-victory/) for the next objective. Return to the [mechanics hub](/mechanics/) for costs.
