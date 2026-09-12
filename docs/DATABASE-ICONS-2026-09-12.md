# 数据百科图标补齐

截图中指出的文明、单位、建筑、科技数据百科已补齐源码图标，覆盖 8 个中英文分类列表和 730 个中英文详情页。

| 类别 | 条目及对应图标 |
| --- | ---: |
| 文明 | 34 |
| 单位 | 127 |
| 建筑 | 124 |
| 科技 | 80 |
| 合计 | 365 |

列表名称旁显示 32px 图标，详情页正文前显示 80px 图标与署名入口。原始素材中的黑白图形通过 CSS 统一显示为白色，并配深绿色底；PNG 原字节保留。手机表格保持区域内横向滚动。此次不改变侧栏文字标签，也不改变数据库数值和规则。

图标来自固定源码提交 `5fa2f57457755c403ea82cc21fec9e617feaf2d0`。复用已有攻略图标，新增 341 个 PNG；攻略和百科合计 393 个素材，737,802 字节（约 721 KiB）。逐文件来源、校验、尺寸和百科映射见 [素材清单](../data/guide-assets.json)，原作者及各作品许可见 [上游署名](../public/game-assets/UPSTREAM-CREDITS.md)。

生成入口为 [generate.py](../scripts/generate.py)。`databaseIcons` 按源码名称匹配四类条目；生成和构建只使用本站保存的文件。已有恢复脚本同时恢复攻略和百科素材，维护方法见 [维护手册](MAINTENANCE-AND-LAUNCH.md)。

## 验证

- 主目录 `pnpm validate` 通过：8 组 Python 回归、统计开关检查、构建、链接／图片／双语／索引检查；796 内容页、794 可索引页、2 页排除，错误为空。
- 新增覆盖回归逐项检查四类图标映射、所有中英文列表及详情页。全部 PNG 保持固定来源 SHA-256、尺寸与公开清单一致。
- 连续生成两次保持结果一致；54 个非百科、非署名内容页面哈希与本轮开始时一致，包括上一轮攻略图解。
- 独立目录离线冻结安装后完整验证通过；复制时补齐 `site.config.json`，最终构建输入与主目录逐文件哈希一致。
- 浏览器检查单位、科技、建筑和英文文明页面，覆盖 390px 手机、1280px 桌面与深浅主题。抽查图标加载成功；大学详情 80px，列表 32px；手机页面无横向溢出，宽表格仅在表格区域滚动。
- `git diff --check` 通过。仅本地交付，未提交、推送或部署。

证据：[主目录日志](validation/database-icons/validate.log)、[独立目录日志](validation/database-icons/independent-validate.log)、[独立输入清单](validation/database-icons/independent-build.json)、[浏览器记录](validation/database-icons/browser-checks.json)、[修改前哈希](validation/database-icons/before-sha256.json)。

本地预览：[单位](http://127.0.0.1:4321/Unciv-Wiki/zh/database/units/) · [建筑](http://127.0.0.1:4321/Unciv-Wiki/zh/database/buildings/) · [科技](http://127.0.0.1:4321/Unciv-Wiki/zh/database/technologies/)。
