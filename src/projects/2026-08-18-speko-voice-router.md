---
layout: project-layout.njk
title: "Speko 模式：语音 AI「模型路由层」服务（YC S26 已验证）"
date: 2026-08-18
category: 服务
businessModel: B2B SaaS——语音 Agent 的模型路由 API，按调用量/订阅收费
monetization: 托管路由器订阅 + 统一计费（多供应商合并账单赚差价）+ 开源网关 BYOK 免费引流
barrier: 中高（多模型集成、公开评测体系、客户信任）
skills: 语音技术（STT/TTS）、LLM 应用工程、评测方法论、B2B 销售
paybackPeriod: 3-6 个月
investment: 前期 API 消耗 + 服务器约 $500-2,000
feasibility: 3
effortScore: 3
barrierScore: 3
monetizationEase: 4
source: Launch HN (Hacker News)
sourceUrl: https://news.ycombinator.com/item?id=49332751
summary: "YC S26 项目 Speko 把‘该用哪套语音模型组合’变成 API：自动从 STT/LLM/TTS 三层选最优，带公开盲评。语音 Agent 爆发+模型每月上新，垂类模型路由/迁移服务有窗口"
tags: [AI, 语音, 模型路由, B2B SaaS, API, Launch HN]
---

## 是什么

[Speko](https://speko.ai/)（YC S26，HN 80 分 50 评论）是一个**语音 AI 模型路由器**——解决语音 Agent 的选型困境：

一个生产级语音 Agent 是三段式组合：语音识别（STT）→ 大模型（LLM）→ 语音合成（TTS）。每一层都有十几个供应商，而且**每月都有新模型**。绝大多数团队只在上线时选一次栈，之后再也不换，结果就是「跑着上个季度的模型，而更便宜更好的已经出了」。

Speko 的做法：你提交约束（准确率/延迟/成本/平衡 + 语言 + 地区），它从自己公开基准过的模型库中筛选、盲评打分、选最优，返回结果时在响应头里告诉你用了哪家模型和分数。还训练了 TTS 自然度的自动评分器，评测面板完全公开（包括自己选错的案例）。

**关键细节**：他们开源了网关（[github.com/SpekoAI/gateway](https://github.com/SpekoAI/gateway)，MIT，单 Go 二进制作为 sidecar 跑在 Agent 容器里），BYOK 模式下完全不上报；收费靠**托管路由 + 统一计费**。接近 4 周时间里外部用量每周增长约 25%。

## 商业模式

**B2B SaaS：托管路由器 + 统一计费**（和 OpenRouter 被 Stripe 以 $7B 收购验证的是同一个形态，只是切到语音赛道）：
- 托管路由 API：按调用量/订阅收费，自动选模型+自动切换
- 统一计费：多供应商账单合并，赚取聚合差价/服务费
- 开源网关免费 → 铺量获客 → 升级到托管版

## 变现方法

1. **托管路由器订阅**：按分钟/调用量计费，客户越用越贵
2. **统一计费 markup**：代付各供应商账单，收加价
3. **评测报告/选型咨询**：替企业做语音模型基准评测（创始人创业前就是干这个的）
4. **开源版引流**：MIT 网关免费，企业自托管后采购托管服务

## 门槛

- 技术上要能接 10+ 供应商 + 建公开评测集，有一定工程量
- 语音运营商（LiveKit 等）生态熟悉度是加分项
- 客户信任：必须证明评测中立（不卖模型才能中立）

## 所需技能

STT/TTS 技术理解、LLM 工程、Go/Python、评测方法论（盲评设计）、B2B 销售或找到渠道

## 变现周期

3-6 个月：先写评测集 + 面板（1-2 月），找 3-5 个语音 Agent 团队内测（2-3 月），转付费（3-6 月）

## 投入成本

- 资金：各供应商 API 测试费用 + 服务器约 $500-2,000
- 时间：前 1-2 个月密集开发，之后维护为主

## 可行性：3/5

市场方向已被双重验证：① OpenRouter 被 Stripe $7B 收购=模型路由是真实刚需；② 语音 Agent 是 2026 最热应用方向，团队普遍「选型疲劳」。但技术门槛和销售周期都不低，适合有语音/LLM 工程背景的人复制。

## 实操步骤

1. 选一个垂直场景（中文客服、医疗口语、教育评测、出海多语言），范围越小越好
2. 建评测集：用同输入跑各家 STT/TTS/LLM，盲评打分（Speko 已经公开了这套方法论可参考）
3. 做最小路由器：按约束过滤 + 打分 + 选优，先不用全自动
4. 开源一个精简版网关/评测脚本，HN/Product Hunt 发帖积攒信任
5. 找 3-5 个正在跑语音 Agent 的团队做免费评测换案例
6. 转托管订阅，按量计费

## 风险与坑

- **模型厂商自建路由**：OpenAI/Anthropic 若推自家全家桶，第三方路由价值被挤压
- **巨头下场**：OpenRouter/Stripe 随时扩展语音层
- **评测争议**：打分不中立会被社区反噬（Speko 主动公开失败案例来对冲）
- **获客周期长**：B2B 决策链长，前期现金流吃紧

## 证据/验证

- Launch HN 原文（含创始人背景、成长数据）：https://news.ycombinator.com/item?id=49332751
- 官网 https://speko.ai/ 已验证 HTTP 200（TITLE: The router for voice models | Speko）
- 开源网关：https://github.com/SpekoAI/gateway（MIT）