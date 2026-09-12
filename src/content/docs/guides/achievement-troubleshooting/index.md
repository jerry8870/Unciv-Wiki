---
{
  "title": "Why did my achievement not unlock?",
  "description": "Troubleshoot achievement eligibility, timing, combat-earned promotions, unique buildings and capture windows.",
  "gameVersion": "4.21.20",
  "appBuild": 1293,
  "ruleset": "Civ V - Gods & Kings",
  "sources": [
    "snapshot:4.21.20-1293"
  ],
  "lastUpdated": "2026-09-12",
  "article": true,
  "publishedAt": "2026-09-12"
}
---

Use this checklist to troubleshoot **locked achievements**. It describes the pinned rules and the relevant fixes; it does not claim that every condition has been verified in a natural iOS playthrough. Read the [full 40-achievement catalogue](/achievements/) for exact conditions.


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>VISUAL GUIDE</span><strong>Check achievements in this order</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/building/palace.png" alt="Game eligibility icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Game eligibility</strong><span class="visual-metric">Check the setup</span><p>Verify a new game, rules, difficulty and opponents.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/shock.png" alt="Qualifying action icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Qualifying action</strong><span class="visual-metric">Check the achievement</span><p>Free promotions are not combat-earned promotions.</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/gold.png" alt="Check timing icon" width="64" height="64" loading="lazy" decoding="async" /></span><strong>Check timing</strong><span class="visual-metric">Check the turn window</span><p>End-turn requirements must persist until the check.</p></li>
</ol>
<figcaption>Reading map; see the text for triggers, numerical limits and tradeoffs. · <a href="/credits/#guide-illustration-assets">Asset credits</a></figcaption>
</figure>


## 1. Check the game before the medal

Was this a new single-player game with a built-in ruleset, one human major civilization, a generated map and an Ancient-era start? Mods, editor-created games, god mode and debug actions can invalidate eligibility. Old saves do not become qualifying games just by updating the app. AI autoplay is permitted, subject to the remaining rules.

Check the starting difficulty and AI count. Easy requires at least one AI opponent; Intermediate requires Prince and at least three; Hard requires King and at least three. Extreme medals have their own requirements. Raising difficulty later or defeating more opponents does not replace the starting conditions.

## 2. Check when the condition is evaluated

Some medals are checked after an action; others require the condition at turn end. If the text says a unit must survive or gold must still be available at turn end, an earlier snapshot is insufficient. Victory or loss stops further recording for that game.

City caps count cities ever founded or captured, including those later disposed of. Wonders must be self-built world wonders; national wonders do not substitute. See [the shared rules](/achievements/#eligible-games-and-recording).

## 3. N08, N31 and N34: count combat-earned promotions

[N08](/achievements/#N08) requires at least three combat-earned promotions **before** the unit captures the city; it must survive. Free, training-provided and mixed-funded promotions do not automatically qualify. The capture must be in battle and the city must have been founded by another major civilization.

[N31](/achievements/#N31) uses one surviving unit's combat promotions and major-civilization military kills. Defensive kills can count; Barbarians do not. Unit upgrades preserve its record.

[N34](/achievements/#N34) requires China's Cho-Ko-Nu to have four combat-earned promotions before the two active-attack kills, against different major-civilization military units during the same own turn, and survive to turn end. A free promotion or a defensive kill is not a substitute for those conditions.

Older saves lacking the new combat accounting fields initialize the missing data to zero. Unknown historical experience is not reconstructed retroactively.

## 4. N11 and N12: equivalents count

For [N11](/achievements/#N11), the qualifying city must be one you founded, have at least 15 population, and have a Library and a University at turn end. The game logic accepts civilization-specific equivalents, such as Siam's Wat replacing the University.

[N12](/achievements/#N12) checks at least 1,000 gold and three self-founded cities, each with Market and Bank or their accepted equivalents, at turn end. Owning a captured city is different from having founded it. Spending below the gold threshold before the check can change the result.

## 5. N32 and N35: respect the capture window

[N32](/achievements/#N32) requires three **different** cities captured in battle during the same turn of your own. Their founders must be other major civilizations. Capturing the same city repeatedly, trading for a city or directly liberating it does not satisfy the count.

[N35](/achievements/#N35) requires Persia to capture four different cities, founded by at least two other major civilizations, during one uninterrupted Golden Age. Extending that Golden Age preserves the window; ending it resets the count.

## 6. Collect a useful bug report

Record achievement ID, game-start settings, action sequence, whether the check reached turn end, and any relevant screenshot or save you are comfortable sharing. Remove personal information before attaching files. Report reproducible problems through [Unciv4iOS issues](https://github.com/jerry8870/Unciv4iOS/issues).

Achievements are local to the device. Game Center or iCloud sign-in will not synchronize this achievement catalogue. Reloading an old save also does not erase medals already recorded locally.

<a id="tf-troubleshooting-en" href="https://testflight.apple.com/join/XSgMMQjt">Check the Unciv4iOS TestFlight invitation</a> · [Installation notes](/ios/)
