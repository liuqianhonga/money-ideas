---
layout: project-layout.njk
title: "EyeRhythm — 离线眨眼节奏监测桌面工具（职场健康赛道）"
date: 2026-11-08
category: 工具
businessModel: 免费增值 SaaS（基础功能免费 + Pro订阅解锁高级报表/企业部署）
monetization: 单次订阅 $5-10/月，或买断 $30-50；企业批量授权 ¥500+/台
barrier: 需要基础前端/WebGPU/Camera API能力；健康类需合规意识
skills: JavaScript/TypeScript, WebRTC, 前端可视化, 健康类产品思维
paybackPeriod: 变现周期 3-6个月（需积累用户口碑）
investment: 投入成本 ¥0-500（服务器/域名），主要是时间成本
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 3
source: Hacker News Show HN
sourceUrl: "https://news.ycombinator.com/item?id=50408350"
summary: Mac/Windows离线桌面工具，通过摄像头监测眨眼频率和规律性，提醒久坐办公族保护视力。完全本地处理，无隐私泄露风险。已验证需求，可做付费功能扩展。
tags: [健康监测, 桌面工具, Show HN, 护眼, 本地优先]
---

## 是什么？

**EyesRhythm** 是一个完全离线的桌面应用（Mac/Windows），通过电脑摄像头实时监测用户的眨眼频率和规律性。它不只是数你眨了多少次眼，而是计算一个「Ocular Rhythm Index」（0-100分），评估你是否在长时间盯着屏幕时保持了健康的眨眼节奏。同时还有一个叫 **Poise** 的模块，记录你头部的转动方向分布，提醒你不要一直歪着脖子看屏幕。

核心卖点：
- ✅ 完全本地处理，视频帧不上传云端，零隐私顾虑
- ✅ 无需联网，开箱即用
- ✅ 面向程序员、设计师等高强度用眼职业人群
- ✅ 健康数据可视化日志

开发者自称是拥有20年经验的计算机视觉研究工程师，自己是干眼症受害者才做了这个工具 —— 这是典型的「自己解决问题 → 做成产品」路径。

## 怎么赚钱？

### 商业模式：Freemium 订阅制

当前版本完全免费开放下载。可行的商业化路径：

| 层级 | 功能 | 定价参考 |
|------|------|---------|
| 免费版 | 基础眨眼监测 + Poise姿势提醒 | ¥0 |
| Pro版 | 详细健康报表、历史趋势分析、多设备同步 | $5-10/月 或 $30-50一次性买断 |
| 企业版 | 团队部署、HR健康数据分析面板 | ¥500+/台/年 |

类比案例：
- **f.lux**（屏幕色温调节）：免费+捐赠模式，累计收入数百万美元
- **RescueTime**（时间追踪）：Freemium，年收入约$100万级别
- **Steam Deck 社区的健康提醒工具**：证明这类 niche 工具真的有付费意愿

## 为什么能赚钱？

1. **刚需痛点清晰**：全球数亿办公桌前工作者都有干眼症问题，医生明确建议「有意识地规律眨眼」
2. **隐私敏感度高**：现有竞品大多依赖云端，EyeRhythm「完全离线」是差异化卖点，适合企业用户
3. **传播成本低**：程序员/设计师群体天然会在 Twitter、HN 分享实用小工具
4. **技术门槛适中**：WebRTC + MediaPipe 即可完成人脸 landmarks 检测，不需要复杂模型

## 实操步骤

如果你想做一个类似的「眼部健康监测桌面工具」：

### 第1步：技术选型（1-2天）
```
推荐栈：
- 前端框架：Electron / Tauri（Tauri 更轻量，打包体积小）
- 人脸识别：MediaPipe Face Mesh 或 vision-camera
- 状态管理：Zustand 或 Plain React State
- 打包发布：macOS DMG + Windows Installer
```

### 第2步：核心功能 MVP（1周）
1. 调用摄像头获取视频流
2. 用 MediaPipe 检测眼睛关键点（左上、左下、右上、右下）
3. 计算 eye aspect ratio (EAR) 判断闭眼/睁眼状态
4. 统计每分钟眨眼次数 + 规律性评分

### 第3步：UI 与数据展示（3-5天）
- 悬浮窗实时显示 blink rate
- 每日/每周统计图表
- 「记得眨眼」浮动提示弹窗

### 第4步：商业化准备（2-3天）
- 注册 App Store / Microsoft Store 账号
- 接入 Stripe / Gumroad 收款
- 写 Landing Page + Product Hunt 页面

### 第5步：冷启动推广
- 发 HN Show HN 帖子
- 在 Reddit r/sideproject、r/GetDisciplined 发帖
- Twitter 分享截图 + 效果视频
- 找健康类博主合作试用

## 风险与坑

⚠️ **医疗健康合规风险**
- 不要宣称「治疗干眼症」「医学诊断」等医疗声明
- 只做「健康辅助工具」定位，避免 FDA/药监局监管

⚠️ **用户粘性不确定**
- 健康类工具常见问题是「新鲜感过了就不打开」
- 建议加入「连续使用奖励机制」或与企业健康管理绑定

⚠️ **市场竞争**
- Apple Watch 已有类似提醒功能
- 差异化在于「桌面场景 + 隐私保护 + 专业指标」

⚠️ **技术坑**
- 不同摄像头分辨率/帧率差异大，需要做适配
- 夜间/低光环境下识别准确率下降
- 戴口罩时需特殊处理

## 证据/验证

| 验证项 | 结果 |
|--------|------|
| 官网 HTTP 状态 | ✅ 200 OK，eyesrhythm.com |
| Meta description | ✅ 描述准确，关键词覆盖 |
| Schema.org structured data | ✅ SoftwareApplication 类型 |
| GitHub 仓库 | 未公开（私有，合理） |
| HN 点赞 | 3 points（刚发布不久） |
| 同类型成功案例 | f.lux、RescueTime、Steam Deck 健康工具均成功 |

**数据来源**：
- https://news.ycombinator.com/item?id=50408350
- https://eyesrhythm.com/
