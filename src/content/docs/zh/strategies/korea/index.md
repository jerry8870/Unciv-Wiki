---
{
  "title": "朝鲜：用食物支撑专家，用首都建设推动科研",
  "description": "安排专家与粮食，核对首都科研建筑奖励，发挥火厢车和龟船的防御窗口，并完成科技收尾。",
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

本文以 **Gods & Kings、标准速度、无模组、单人王子至国王难度** 为教学基线。以下情境是根据规则构造的决策练习，不是真实战报或胜率验证。

[朝鲜](/zh/database/civilizations/korea/)的科研来自已工作的专家、伟人改良和首都科研建设。与[通用科技路线](/zh/strategies/science-victory/)相比，你需要更仔细地控制专家分配，并单独安排首都建设节点；把每个城市同时塞满专家，往往先耗尽粮食。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>科研加成与特色防守单位</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/nation/korea.png" alt="朝鲜图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>朝鲜</strong><span class="visual-metric">每名专家 +2 科研</span><p>需要实际分配市民；首都建设另有奖励。</p></li>
<li><span class="visual-image is-pixel"><img class="visual-art" src="/game-assets/sprite/hwach-a.png" alt="火厢车图标" width="96" height="96" loading="lazy" decoding="async" /></span><strong>火厢车</strong><span class="visual-metric">远程 26</span><p>清理单位；没有抛石机的对城 +200%。</p></li>
<li><span class="visual-image is-pixel"><img class="visual-art" src="/game-assets/sprite/turtle-ship.png" alt="龟船图标" width="96" height="96" loading="lazy" decoding="async" /></span><strong>龟船</strong><span class="visual-metric">战斗力 36</span><p>守住近海；不能进入海洋地块。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>


## 能力解释：三种科研不能混算

| 来源 | 效果 | 兑现条件 |
| --- | --- | --- |
| 专家 | 所有城市每名专家 +2 科研 | 实际占用槽位；不仅限于科学家 |
| 伟人改良 | 每个伟人改良地块 +2 科研 | 改良未被劫掠且有市民工作，不能只拥有地块 |
| 首都科研建设 | 首都建成与科研相关的建筑或奇观，获得一次科研奖励 | 引擎检查科研关联和首都；不是所有奇观，也不是所有城市建造 |
| 火厢车 | 近战 11、远程 26；替代抛石机，但没有普通抛石机的 +200% 对城攻击 | 适合打单位和守阵地；需要架设，没有地形防御加成 |
| 龟船 | 战斗力 36、移动 4；替代轻帆船，但不能进入海洋地块 | 近海防御强，不能承担跨海洋探索与远征任务 |

基础[科学家](/zh/mechanics/resources-improvements/)提供 3 科研，朝鲜科学家因此为 **5 基础科研**；工程师或艺术家也得到额外 2 科研，但仍产生各自类型的伟人点数。朝鲜能力没有给所有专家增加大科学家点数。

## 适用局势与开局分支

首都粮食足、生产力够，才能把专家和科研建筑串起来。先侦察粮食地块、淡水农场位置与可守城市圈，不为海滨开局倾向强行追求海军战。靠海但缺粮的首都依然需要改良与粮食建筑。

安全开局按粮食、工人、图书馆和扩张需要安排，尽早形成能够承担大学专家的核心。若粮食不足，先增加工作农场和人口，再考虑多开槽位；若邻军逼近，优先普通防御部队，不要等待尚未解锁的特色单位。

[国立研究院](/zh/database/buildings/national-college/)的全城图书馆门槛仍适用。新城有价值时可以扩张，但要明确它何时补齐图书馆。首都科研奖励让首都的对应建设更有吸引力，不代表任何时候都该停下军队抢科研奇观。

## 中期关键节点：大学和首都奖励

[大学](/zh/database/buildings/university/)提供 33% 科研加成和两个科学家槽位。先安排一名，观察食物、人口增长和项目工期，再决定第二名。一个能长期养活专家的城市，通常比连续饿掉人口的“全槽科研城”更可靠。[世俗主义](/zh/mechanics/policies/)另给每位专家 +2 科研；拥有该政策的朝鲜科学家基础科研为 3 + 2 + 2 = **7**，城市百分比另算。

首都建成科研相关建筑或奇观时，引擎取 **当前可研究科技实际成本的中位数的一半，再四舍五入** 作为科研奖励；不是最便宜科技的一半，也不是固定送一项科技。可研究列表随前置变化，实际成本也受当局规则影响。检查科技树和建设完工时机，不把一张固定基础造价表当作奖金表。

正常情况下，首都先完成有实际持续收益的图书馆、大学等项目，比为提高一次奖励而故意长期拖延更稳。分城的大学没有这项首都一次性奖励，但其百分比、专家槽位与人口科研仍有价值。

## 特色单位窗口：防守分工

[火厢车](/zh/database/units/hwach-a/)的高远程值适合清理陆军；它不继承普通抛石机的对城加成。让近战单位守住接近路线，先看架设位置和视线，再清前排。不要在没有护卫时把它推到敌城旁边。

[龟船](/zh/database/units/turtle-ship/)可保护近海资源、沿岸城市和运输线，但无法进入海洋。需要跨洋任务时另行检查能走该路线的单位和技术，不把“替代轻帆船”理解为所有海域能力都相同。陆地战争也不必为了特色单位把有限生产力大量转到海上。

## 胜利收尾与失败补救

按[科技胜利](/zh/strategies/science-victory/)把科研转换成阿波罗计划、六个部件和首都装配。最后一轮研究接近完成时，重新分配一部分专家到高生产地块，可以缩短部件等待；以实际损失科研和节省工期比较，不要一直锁死专家。

粮食见底时减少一两个槽位，修复农场和快乐。首都被围时先保城与改良，暂缓奇观；分城仍能支撑人口与专家科研。发现火厢车攻城慢，应补足正确的攻城组合或停战，而非靠多造同一单位硬追进度。



<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>专家占用的是已有市民</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/food.png" alt="农民留在两块农场图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>农民留在两块农场</strong><span class="visual-metric">+6 食物盈余</span><p>8 人、22 总食物、消耗 16；两个槽位空着。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/population.png" alt="只安排一名科学家图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>只安排一名科学家</strong><span class="visual-metric">+3 食物盈余</span><p>移出一名 3 食物农场市民；基础 3 科研、3 点数。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/science.png" alt="安排两名科学家图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>安排两名科学家</strong><span class="visual-metric">0 食物盈余</span><p>移出两名农民；基础 6 科研、6 点数，城市停止成长。</p></li>
</ol>
<figcaption>简化教学计算：未计文明、政策与城市百分比；朝鲜每名专家另有 +2 科研。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>

## 教学情境一：两个科学家是否值得立即上岗

**条件：** 8 人城市总食物 22、消耗 16，两名市民各工作 3 食物农场；大学两个槽位空着，没有世俗主义和其他额外修正。

**选择：** 全部转为科学家，盈余由 +6 降为 0，新增 2 × (3 + 2) = **10 基础科研**，大科学家基础点数为 6。只转一人则新增 5 科研、3 点数，并保留 +3 食物盈余。

**代价：** 全填停止这项简化条件下的成长。与巴比伦不同，朝鲜此处不会把 6 点数变成 9；优势在专家科研，不能混用文明能力。

**复查：** 如果第九人口能很快到来并工作好地块，先一槽可能更合算。下一次成长、农场完成或失去外部粮食时，重新查看[市民分配](/zh/mechanics/resources-improvements/)和最终科研。

## 教学情境二：首都大学还差一回合

**条件：** 假设完工时当前可研究科技成本为 100、200、300、500；首都大学下一回合完成。这是为解释公式而构造的成本列表。

**选择：** 中位数是 (200 + 300) ÷ 2 = 250，一次奖励为 250 × 0.5 = **125 科研**。把奖励与大学持续收益一起评价，按正常有用的建设节奏完工。

**代价：** 若故意拖延，既损失大学持续收益，也可能推迟专家和下一项关键科技。另一个城市建大学并不触发同一奖励；建成无科研关联奇观也不能照套公式。

**复查：** 完工前记录可研究科技和当前进度，完工后看科研变化。实际列表不等于这个例子时重新计算；不要因为一次奖励没直接跳科技就判断能力失效。

可对照[巴比伦](/zh/strategies/babylon/)选择另一种科研文明，或用[战斗与晋升](/zh/mechanics/combat-promotions/)处理火厢车的目标选择。更多路线见[攻略目录](/zh/strategies/)。
