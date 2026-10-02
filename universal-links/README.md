# HTTPS 多人游戏邀请部署

博客地址和现有内容保持 `https://jerry8870.github.io/Unciv-Wiki/`。
新的分享/复制链接格式：

```
https://jerry8870.github.io/Unciv-Wiki/invite.html?gameId=<UUID>&server=<URL-encoded HTTPS server>
```

邀请只包含存档标识和服务器地址，不包含密码、玩家身份或席位授权。网页不请求游戏服务器，不收集邀请参数，不自动跳转；可以复制链接、手动粘贴到游戏，或打开 TestFlight 安装入口。中文系统显示中文，其他语言显示英文。

## 1. 博客仓库

- `public/invite.html` 和 `public/invitation/invite.mjs` 随现有 Astro 构建发布。
- 固定 HTML 路径无需为每个 Game ID 生成页面，也不依赖 404 跳转。
- `pnpm check:invitation` 验证参数、服务器地址和关联规则；`pnpm validate` 包含此检查。
- 邀请页面不进入搜索索引或站点地图，不影响博客现有导航。

## 2. 同一个仓库发布根站点与博客

现有博客仓库已改名为 `jerry8870/jerry8870.github.io`，本地目录仍为 `Unciv4iOS-Blog`。
`universal-links/root-site/` 保存根站点文件，博客源码与 `site.config.json` 的
`/Unciv-Wiki/` 路径保持不变。无需另建仓库。

`pnpm validate` 构建并校验博客后，执行 `pnpm prepare:pages`：将根站点文件放入
`.pages-dist/`，将 `dist/` 放入 `.pages-dist/Unciv-Wiki/`，核对邀请页面和关联规则。
现有 GitHub Actions 工作流发布 `.pages-dist/`。仓库 Settings → Pages 的 Source
应保持 GitHub Actions。`.nojekyll` 和 `.well-known` 随发布包保留。
关联文件必须最终位于：

```
https://jerry8870.github.io/.well-known/apple-app-site-association
```

不能只发布在 `/Unciv-Wiki/.well-known/`。AASA 的应用标识
`ZHMX53WRKQ.com.aishuati.unciv` 来自已签名 IPA 的 application-identifier。
只关联 `/Unciv-Wiki/invite.html`，不关联整个博客。

发布前遵守项目的 Git 推送确认规则。本地准备文件不等于远端发布。

## 3. Apple 和 App 配置

- 为 `com.aishuati.unciv` 开启 Associated Domains，并更新开发和发行描述文件。
- App 签名 entitlements 必须包含 `applinks:jerry8870.github.io`。
- 新版 App 接收 Scene 冷启动与运行中 `NSUserActivity`，读取 `webpageURL`，复用邀请下载流程。
- 分享、复制、手动粘贴统一使用新 HTTPS 链接；`unciv4ios://` 不再注册或接受。
- Android 上游 HTTPS 邀请仍可以手动粘贴。链接不改变当前玩家身份或全局服务器设置。

## 4. 发布后的验收

1. 用 HTTPS GET 检查根目录 AASA：HTTP 200、有效 JSON、无重定向；检查 Content-Type，Apple 文档要求 application/json。GitHub Pages 的响应头由平台管理，必须实测，不能在 HTML 或 JS 中伪造。如果不能满足要求，需换到可控制响应头的域名/托管服务。
2. 检查 Apple CDN 是否返回相同规则：`https://app-site-association.cdn-apple.com/a/v1/jerry8870.github.io`。缓存更新可能需要等待。
3. 检查签名后的 App 和 embedded.mobileprovision 均允许 Associated Domains，且 Info.plist 无旧协议注册。
4. 安装新版 App，将真实邀请放入备忘录，长按检查是否出现用 Unciv4iOS 打开；验证游戏关闭、前台、后台、重复点击。
5. 验证邀请进入指定服务器的对局，错误/不存在的游戏有提示，未安装时显示网页。
6. 微信真机测试：点击收到的 HTTPS 链接；如停留在网页，验证复制→游戏内粘贴。若浏览器禁用剪贴板，显示可长按复制的文本框。

第三方浏览器是否交给系统唤起 App 由其自身决定。直接在 Safari 地址栏输入 URL，以及网页内同域导航，不保证打开 App；移除自定义协议后不提供自定义协议备用按钮。

参考：
- https://developer.apple.com/documentation/xcode/supporting-associated-domains
- https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
- https://developer.apple.com/documentation/technotes/tn3155-debugging-universal-links
- https://docs.github.com/en/pages/building-and-customizing-your-site-with-jekyll/about-github-pages-and-jekyll
