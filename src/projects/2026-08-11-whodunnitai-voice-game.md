---
layout: project-layout.njk
title: "WhoDunnitAI（用语音审讯 AI 嫌疑人的推理游戏，AI 娱乐新品类）"
date: 2026-08-11
category: 工具
businessModel: 免费试玩引流 + 捐赠/付费解锁案例 + 后续订阅制 AI 互动娱乐
monetization: 单案例付费解锁、Stripe 捐赠打赏、后续可转订阅制（$5-15/月解锁全部案例）
barrier: 中门槛：需 OpenAI Realtime API（gpt-realtime-2.1）+ WebRTC 语音流，单用户语音时长有成本
skills: Next.js、WebRTC、OpenAI Realtime API、MongoDB、Clerk 认证、Prompt 工程
paybackPeriod: 1-3 个月（开发 2-4 周 + 冷启动引流）
investment: 前期 0-3000 元（API 调用成本为主，代码全开源可抄架构）
feasibility: 4
effortScore: 3
barrierScore: 2
monetizationEase: 3
source: Show HN
sourceUrl: https://news.ycombinator.com/item?id=49238851
summary: 语音驱动谋杀推理游戏——用 GPT Realtime 语音审讯 AI 嫌疑人、抓矛盾破案，Show HN 136 分验证了「AI 互动娱乐」新品类
tags: [AI, 游戏, 语音, 互动娱乐, 独立开发, Show HN]
---

# WhoDunnitAI：语音审讯 AI 嫌疑人的推理游戏

## 是什么

[WhoDunnitAI](https://www.whodunnitai.com/) 是一个**语音驱动的谋杀推理游戏**：玩家扮演侦探，用语音直接"审讯"AI 扮演的嫌疑人。每个嫌疑人由 OpenAI gpt-realtime-2.1 驱动（语音转语音，WebRTC 实时对话），玩家通过提问、施压、抓矛盾来破案。系统内置一个 gpt-5-mini 裁判，判断玩家是否真正陈述了案件关键证据——**转述算、模糊怀疑不算**。

技术栈：Next.js + MongoDB + Clerk（认证）+ OpenAI Realtime API。作者单人开发（Chase Myers），Show HN 获得 136 分 / 54 评论。

## 怎么赚钱

1. **免费试玩引流**：首个案例免费开放，体验语音审讯的新奇感
2. **付费解锁案例**：更多案件按个付费或打包解锁
3. **捐赠打赏**：目前用 Stripe 捐赠支付实时 AI 语音成本（作者自述"每次审讯都烧钱"）
4. **升级订阅制**：AI 娱乐内容天然适合订阅——月费解锁全部案例 + 新案件持续更新

## 为什么能赚钱

- **市场验证**：Show HN 136 分说明开发者社区认可；AI 语音互动是 2026 年明确增长赛道
- **品类空白**：市面 AI 游戏多是文字/图片，**语音实时对话审讯**几乎没有竞品
- **内容可复制**：写新案件 = 写剧本 + 配置嫌疑人 Prompt，边际成本极低
- **病毒传播**：推理游戏天然适合直播/短视频传播（主播玩推理 = 免费广告）

## 实操步骤

1. 用 Next.js 搭 WebRTC 语音流（OpenAI Realtime API 有官方 demo 可抄）
2. 设计 1 个高质量案件剧本（5 个嫌疑人、每人 3-5 个隐藏矛盾点）
3. 加 gpt-5-mini 裁判逻辑：判定玩家是否收集到关键证据
4. 接 Clerk 认证 + MongoDB 存档 + Stripe 支付
5. 免费放 1 个案例上 Show HN / Reddit r/SideProject 冷启动
6. 根据反馈迭代 2-3 个新案件，上付费解锁/订阅

## 风险与坑

- ⚠️ **API 成本不可控**：Realtime 语音按分钟计费，免费用户滥用会烧钱——必须设时长限制（作者就加了 30 分钟计时器）
- ⚠️ 语音交互延迟/识别错误影响体验，需要精心调 Prompt
- ⚠️ 游戏品类生命周期短，需要持续出新案件维持用户
- ⚠️ 单纯捐赠模式难持久，尽早转订阅/买断

## 证据/验证

- Show HN 原帖：https://news.ycombinator.com/item?id=49238851（136 分）
- 产品官网：https://www.whodunnitai.com/（curl 验证 HTTP 200）
- 作者主页：https://chasem.dev/
