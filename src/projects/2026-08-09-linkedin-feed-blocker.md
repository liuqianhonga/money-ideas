---
layout: project-layout.njk
title: "LinkedIn Feed Blocker（社交信息流屏蔽工具）"
date: 2026-08-09
category: 工具
businessModel: 免费开源浏览器扩展引流，向「多平台专注工具」升级后走付费订阅
monetization: 免费开源（Chrome 扩展）+ 增值付费（多平台支持、自定义规则、团队版）
barrier: 低门槛：Chrome 扩展开发基础即可，个人可做
skills: JavaScript/TypeScript、Chrome Extension API、DOM 操作、基础 UI 设计
paybackPeriod: 1-3 个月（开发一周，变现需扩展功能后）
investment: 前期 0-500 元（Chrome Web Store $5 开发者注册费 + 1-2 周时间）
feasibility: 3
effortScore: 1
barrierScore: 1
monetizationEase: 3
source: Hacker News Front Page
sourceUrl: https://github.com/andrewpollack/linkedin-feed-blocker
summary: HN 141 分的 Chrome 扩展，屏蔽 LinkedIn 首页信息流保留其余功能，验证了「社交平台信息流疲劳」的工具需求
tags: [Chrome扩展, 效率工具, 开源, 浏览器]
---

# LinkedIn Feed Blocker（社交信息流屏蔽工具）

## 是什么

[LinkedIn Feed Blocker](https://github.com/andrewpollack/linkedin-feed-blocker) 是一个极简 Chrome 扩展：**隐藏 LinkedIn 首页 feed（信息流），但保留个人资料、职位、搜索、消息、通知等所有其他功能**。

创始人不想看 LinkedIn 上的「社交狂欢信息流」，但需要用它找工作、联系招聘官。于是花少量时间做了这个扩展，2026-08-08 发布到 Hacker News 后**拿下 141 points、81 条评论**（HN 首页），GitHub 一天内 74 stars。

核心功能：
- 隐藏 `/feed` 主信息流
- 拦截无限滚动分页
- 其余 LinkedIn 功能完全正常
- 浏览器端本地实现，无数据上传

## 商业模式

一句话：**用免费开源扩展验证「信息流疲劳」需求，升级为多平台专注工具后通过订阅变现。**

1. **免费开源**：GitHub + Chrome Web Store 免费发布，快速积累用户和口碑
2. **Pro 版**（付费 $2-5/月或买断 $19）：多平台支持（LinkedIn/Instagram/X/YouTube 首页推荐流）、自定义屏蔽规则、统计「今天为你省了多少时间」
3. **企业版**：给注重员工专注力的团队提供预配置版本

## 变现方法

1. **Chrome Web Store 免费版引流**：用户搜索「linkedin feed blocker」等关键词自然获客
2. **Pro 订阅**：从免费版升级按钮转化，多平台支持是最有说服力的付费点
3. **同类扩展矩阵**：做出「X 信息流屏蔽」「YouTube 推荐流屏蔽」系列，每个都是独立入口
4. **捐赠/Buy Me a Coffee**：开源项目常见补充收入，忠实用户会支持

## 门槛

- **技术门槛**：低。Chrome 扩展 = HTML/CSS/JS + manifest.json，MVP 一个周末能做出来
- **资金门槛**：几乎为零（Chrome Web Store 开发者一次性 $5）
- **资质门槛**：无

## 所需技能

- 基础 JavaScript（DOM 操作、MutationObserver 监听动态内容）
- Chrome Extension Manifest V3 开发
- 基础 UI（开关设置页）

## 变现周期

MVP 开发 **3-7 天**，免费版上线后 1-2 周可验证需求（看安装量）。付费功能从开发到产生收入 **1-3 个月**。注意：纯免费工具的收入天花板低，必须做 Pro 升级路径。

## 投入成本

- 资金：$5（开发者注册费）+ 域名/落地页可选
- 时间：MVP 10-30 小时，维护每月 2-5 小时（应对 LinkedIn 页面改版）

## 可行性评分：3/5

理由：开发门槛极低、HN 已证明需求真实（141 points 且评论热烈）、Chrome 扩展分发渠道成熟。扣分原因：单一平台免费工具变现弱，需要扩展为多平台套件才有稳定收入；且 LinkedIn 改版可能导致维护频繁。

## 实操步骤

1. **clone 学习**：把 [andrewpollack/linkedin-feed-blocker](https://github.com/andrewpollack/linkedin-feed-blocker)（74 stars）源码 clone 下来读懂核心逻辑
2. **自己做一版**：仿照做「X/Twitter 信息流屏蔽」扩展（X 用户抱怨更多，需求更大）
3. **上架分发**：Chrome Web Store 发布 + GitHub 开源（开源能快速积累 stars 和 PR）
4. **打透一个平台**：先专注一个平台，靠 HN/Reddit/r/productivity 发帖获第一波用户
5. **加 Pro 功能**：多平台支持 + 自定义规则 + 使用统计，设置付费墙
6. **做系列扩展**：按同样的模板复制到 YouTube/Instagram/Reddit，形成「专注工具」品牌

## 风险与坑

- **平台改版**：LinkedIn/X 改版可能让扩展失效，需持续维护（这是扩展类工具的宿命）
- **Chrome 政策**：2024 年起强制 Manifest V3，旧扩展不迁移会被下架
- **变现天花板**：用户预期这类工具免费，付费转化率低，Pro 功能必须足够有吸引力
- **不要过度**：如果做「隐藏所有社交平台」的激进版，可能触发平台投诉
- **竞品多**：News Feed Eradicator 等同类扩展已有用户基础，需差异化定位

## 证据/验证

- GitHub：[https://github.com/andrewpollack/linkedin-feed-blocker](https://github.com/andrewpollack/linkedin-feed-blocker) — **验证通过**（74 stars，MIT，2026-08-08 创建）
- HN 讨论：[https://news.ycombinator.com/item?id=49223475](https://news.ycombinator.com/item?id=49223475) — 141 points，81 条评论，评论里大量用户表达对社交信息流的厌倦（需求信号强）
- Chrome Web Store 上架中：[https://chromewebstore.google.com/detail/likdkcmiigfdfpkkecbcephijdfbegcf](https://chromewebstore.google.com/detail/likdkcmiigfdfpkkecbcephijdfbegcf)
