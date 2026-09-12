---
{
  "title": "成就未解锁排查",
  "description": "检查 V3 成就资格、回合时机、战斗经验晋升、专属建筑以及 N32/N35 攻城窗口。",
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

本清单用于排查 **成就未解锁问题**，依据固定提交的规则及相关修复内容编写，不表示每项条件均已通过真实 iOS 自然对局验证。具体要求以[全部 40 项成就目录](/zh/achievements/)为准。


<figure class="guide-figure guide-flow">
<div class="visual-heading"><span>图解</span><strong>成就排查按这个顺序</strong></div>
<ol class="visual-flow">
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/building/palace.png" alt="对局资格图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>对局资格</strong><span class="visual-metric">先查开局</span><p>新局、规则、难度与对手数先满足。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/promotion/shock.png" alt="有效行为图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>有效行为</strong><span class="visual-metric">再查单项条件</span><p>免费晋升不能直接当作战斗经验晋升。</p></li>
<li><span class="visual-image "><img class="visual-icon" src="/game-assets/stat/gold.png" alt="检查时点图标" width="64" height="64" loading="lazy" decoding="async" /></span><strong>检查时点</strong><span class="visual-metric">最后查回合窗口</span><p>回合结束要求必须维持到检查时。</p></li>
</ol>
<figcaption>阅读路线示意；具体触发条件、数值边界与取舍见正文。 · <a href="/zh/credits/#攻略配图素材">素材来源</a></figcaption>
</figure>


## 1. 先查对局资格，再查单项条件

是否使用内置规则集新建单人对局、仅一名人类主要文明、生成地图、远古时代开局？模组、编辑器地图、上帝模式和调试行为可能使对局不合格。升级 App 不会让旧存档自动变成合格新局。V3 允许 AI 自动托管，但仍须满足其他规则。

再检查开局难度和 AI 数量：简单至少 1 个 AI；中等要求王子及以上、至少 3 个 AI；困难要求国王及以上、至少 3 个 AI；极难按每项条件执行。后续调整难度或击败对手不能替代开局要求。

## 2. 确认检查发生的时机

部分成就在行动后检查，部分要求回合结束时仍满足条件。如果文案要求单位存活、或回合结束时保有金币，较早时刻满足并不够。胜利或失败后，该对局停止继续记录。

城市上限包括历史上建立或占领过、后来又处置掉的城市。奇观须为自己建造的世界奇观，国家奇观不能代替。详见[通用规则](/zh/achievements/#合格对局与记录边界)。

## 3. N08、N31、N34：核对战斗经验晋升

[N08](/zh/achievements/#N08)要求单位在攻下城市**之前**已经获得至少 3 次战斗经验晋升，并在占领后存活。免费、训练提供以及混合来源支付的晋升不能直接当作有效次数。城市必须通过战斗占领，且由其他主要文明建立。

[N31](/zh/achievements/#N31)统计同一名存活单位的战斗晋升与主要文明军事单位击杀。防守反杀可以计入，蛮族不计入；单位升级保留记录。

[N34](/zh/achievements/#N34)要求中国的诸葛弩在两次击杀前已有至少 4 次战斗经验晋升，在己方同一回合主动攻击并消灭两支不同的主要文明军事单位，且活到回合结束。免费晋升与防守反杀不能替代这里的要求。

旧存档缺少新增战斗记录字段时，缺失数据从零开始，不会追溯推算无法确认的历史经验。

## 4. N11、N12：接受专属等价建筑

[N11](/zh/achievements/#N11)要求自己建立的城市在回合结束时至少 15 人口，并拥有图书馆和大学。游戏逻辑接受文明专属等价建筑，例如暹罗替代大学的经院。

[N12](/zh/achievements/#N12)要求回合结束时至少持有 1,000 金币，并有至少三座自己建立的城市，各自拥有市场与银行或认可的等价建筑。占领来的城市不同于自己建立的城市；在检查前把金币花到阈值以下，也会影响结果。

## 5. N32、N35：不要跨越攻城统计窗口

[N32](/zh/achievements/#N32)要求在己方同一回合，通过战斗攻下三座**不同**的城市，且其创始者为其他主要文明。重复攻占同一城市、交易获得城市或直接解放不计入要求的数量。

[N35](/zh/achievements/#N35)要求波斯在一次连续黄金时代内，攻下四座不同城市，创始者至少涉及两个其他主要文明。延长黄金时代仍属于同一窗口；黄金时代结束会重置计数。

## 6. 整理可复现的问题反馈

记录 App 版本与构建号、成就 ID、开局设置、操作顺序、是否已经结束回合，以及愿意分享的相关截图或存档。附件中有个人信息时先移除。可复现的问题提交到 [Unciv4iOS Issues](https://github.com/jerry8870/Unciv4iOS/issues)。

成就只记录在本机。登录 Game Center 或 iCloud 不会同步这一版 V3 目录；读取旧存档也不会抹去本机已经记录的勋章。

<a id="tf-troubleshooting-zh" href="https://testflight.apple.com/join/XSgMMQjt">查看 Unciv4iOS TestFlight 邀请</a> · [安装与版本说明](/zh/ios/)
