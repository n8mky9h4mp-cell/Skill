# 抖音小游戏适配

## 官方入口

- [Cocos Creator 3.8 发布到抖音小游戏](https://docs.cocos.com/creator/3.8/manual/en/editor/publish/publish-bytedance-mini-game.html)
- [抖音小游戏开发指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/)
- [抖音小游戏入门指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/)

实现前核对当前开发者工具、基础库、API、包体/分包、广告和审核要求。

## 构建准备

- 确认抖音开放平台主体、小游戏应用、App ID 和测试权限。
- 在 Cocos 构建面板选择抖音小游戏，检查方向、启动场景 Bundle 和远程资源设置。
- 将生成的抖音小游戏目录导入当前开发者工具验证。

## 运行环境

- `tt` 只出现在抖音平台实现和抖音专属模块中。
- 小游戏环境不是浏览器，不能依赖 DOM/BOM；使用 Cocos 导出适配和平台 API。
- 登录、分享、广告、存储、网络和生命周期都通过统一平台接口。
- 多宿主或 PC 场景可能缺少部分移动能力，执行时按目标宿主做能力检测和文案降级。

## 资源与弱网

- 根据当前官方规则配置代码包、分包、远程资源和缓存。
- 验证无网/弱网进入、资源下载失败和重试，不让核心游戏永久卡在加载页。
- 平台专属传播能力只有在 PRD 批准且双端体验可接受时接入。

## 验收

至少记录：开发者工具构建、预览/真机、登录、存储、分享、广告、前后台恢复、弱网和资源失败。不可用能力返回明确状态，不用微信行为代替抖音验证。
