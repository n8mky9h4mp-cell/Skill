# 双端平台适配层

## 目标

玩法层只依赖稳定的业务语义，不关心全局对象是 `wx`、`tt` 还是编辑器模拟器。

## 建议接口

按 PRD 裁剪，不为未来能力创建空方法：

```typescript
export type PlatformKind = 'editor' | 'wechat' | 'douyin';

export interface PlatformResult<T> {
  ok: boolean;
  value?: T;
  reason?: 'unsupported' | 'unavailable' | 'cancelled' | 'failed';
  simulated?: boolean;
}

export interface RewardedAdResult {
  completed: boolean;
}

export interface PlatformService {
  readonly kind: PlatformKind;
  login(): Promise<PlatformResult<{ code: string }>>;
  getStorage<T>(key: string): Promise<PlatformResult<T | null>>;
  setStorage<T>(key: string, value: T): Promise<PlatformResult<void>>;
  share(payload: { title: string; imageUrl?: string }): Promise<PlatformResult<void>>;
  showRewardedAd(placement: string): Promise<PlatformResult<RewardedAdResult>>;
  showInterstitialAd(placement: string): Promise<PlatformResult<void>>;
  vibrateShort(): Promise<PlatformResult<void>>;
}
```

接口名称表达游戏需要的行为，不机械镜像所有平台 API。返回值明确区分不支持、不可用、取消和失败。

## 实现

```text
platform/
├── PlatformService.ts
├── PlatformFactory.ts
├── EditorPlatform.ts
├── WechatPlatform.ts
└── DouyinPlatform.ts
```

- `PlatformFactory` 只在一个位置检测环境。
- 平台全局对象采用安全检测，不在编辑器中直接引用不存在的变量。
- 平台回调转换为一次性 Promise 时要清理监听，防止多次完成。
- 平台不支持的能力返回 `unsupported`，不能静默成功。
- 编辑器模拟结果设置 `simulated: true`，不生成看似真实的登录 code。

## 生命周期

统一前后台、网络变化和安全区域事件，再通知游戏状态。重复进入场景时不能重复注册监听；销毁或退出时注销回调。

## 错误处理

- 业务层根据 `reason` 决定提示或降级。
- 日志不输出登录凭证、用户敏感数据或秘密。
- 广告、分享和振动失败不应破坏核心玩法。
- 需要平台专属 UI 或文案时封装在对应实现或配置中。
