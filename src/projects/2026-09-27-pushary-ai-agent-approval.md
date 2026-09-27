---
layout: project-layout.njk
title: "Pushary — AI Agent 锁屏审批系统，让 Agent 不再卡住等你"
date: 2026-09-27
category: 工具
businessModel: SaaS 订阅（$9.99/月）+ 企业版
monetization: 个人版 $9.99/月，企业版按需定价，按 Agent 数量或审批数计费
barrier: 中等，需要开发移动端 App 和后端服务
skills: Flutter/React Native 开发、Node.js/TypeScript、AI Agent 集成
paybackPeriod: 3-6 个月（冷启动期）
investment: 前期开发成本约 ¥10000-30000
feasibility: 3
effortScore: 3
barrierScore: 3
monetizationEase: 4
source: "Product Hunt / 官网"
sourceUrl: "https://pushary.com"
summary: "AI Agent 审批中间件，当 Claude Code/Codex/Cursor 等 Agent 需要决策时，推送通知到手机锁屏，用户一键审批继续运行"
tags: [AI Agent, 开发者工具, SaaS, 移动App]
---

## 项目是什么

**Pushary** 解决了 AI 编程 Agent 的一个核心痛点：**Agent 运行时会停下来等待人类审批**，而用户往往不在电脑前。

Pushary 的工作流程：
1. 用户在电脑上运行 `npx @pushary/agent-hooks setup` 配对手机
2. 启动 Claude Code/Codex/Cursor 等 Agent
3. Agent 需要审批时，Pushary 推送通知到用户手机
4. 用户在锁屏界面直接按「Yes/No」或输入文字
5. 决策返回给 Agent，继续运行

支持平台：iOS、Android、Web Push、Slack
支持 Agent：Claude Code、Codex、Cursor、Gemini CLI、Hermes、OpenClaw

## 商业模式

**SaaS 订阅模式**：
- 个人版：$9.99/月（3 天免费试用）
- 企业版：按 Agent 数量或审批量计费

## 变现方法

| 路径 | 具体做法 | 预估收入 |
|------|----------|----------|
| **个人订阅** | 开发者按月付费 | $9.99 × 1000 用户 = $10k/月 |
| **企业订阅** | 团队多 Agent 审批 | $50-500/月/团队 |
| **API 集成** | 为其他 Agent 框架提供审批 SDK | 按调用量计费 |

## 门槛分析

- **技术门槛**：较高（需要开发 iOS/Android App + 后端 + Agent 集成）
- **资金门槛**：中等（服务器成本 + 应用商店费用）
- **资质门槛**：无特殊要求，需要技术能力

## 所需技能

- Flutter 或 React Native（移动端开发）
- Node.js/TypeScript（后端服务）
- Push Notifications（APNs、FCM）
- AI Agent SDK 集成（Claude Code、Codex 等）

## 变现周期

- **冷启动**（1-3 个月）：开发 MVP，获取首批 100 用户
- **增长期**（3-6 个月）：通过 Product Hunt、Twitter、GitHub 推广
- **成熟期**（6-12 个月）：达到 500-1000 付费用户

## 投入成本

- 时间：全职 2-3 个月或兼职 6 个月
- 资金：$500-2000（服务器、应用商店、营销）

## 实操步骤

### 方案 A：模仿者路径（推荐）
1. 研究 Pushary 的产品设计和技术架构
2. 选择自己熟悉的技术栈重新实现（如用 Flutter + Firebase）
3. 聚焦细分市场（如只支持某个特定 Agent）
4. 定价略低于 Pushary，快速获客

### 方案 B：差异化竞争
1. 找到 Pushary 的痛点（如不支持某些 Agent）
2. 针对痛点开发特色功能
3. 免费开源核心功能，收费高级功能

### 方案 C：集成而非替代
1. 学习 Pushary 的 API 设计
2. 开发自己的 Agent 框架，集成 Pushary 的审批能力
3. 作为增值功能出售

## 风险与坑

⚠️ **风险提示**：
1. 市场已被 Pushary 占领，直接进入竞争压力大
2. 需要持续维护多个平台的 App（iOS/Android/Web）
3. Agent 生态变化快，需要频繁适配新工具

## 证据/验证

- ✅ 官网 HTTP 200：https://pushary.com
- ✅ Product Hunt 页面：https://www.producthunt.com/products/pushary
- ✅ 移动应用商店：App Store + Google Play
- ✅ 定价透明：$9.99/月，3 天试用
- ✅ 技术文档完整

## 结论

**这是当前 AI 开发工具领域的热门方向**，但直接进入竞争压力大。更聪明的做法是：
1. 作为集成方，学习其产品设计和定价策略
2. 针对细分市场需求（如特定 Agent、特定行业）
3. 或开发互补工具（如审批日志分析、审批策略优化）

**信心指数：62**（变现路径清晰，但竞争已激烈）
