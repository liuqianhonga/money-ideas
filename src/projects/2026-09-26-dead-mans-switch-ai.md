---
layout: project-layout.njk
title: "AI 死信开关（Dead Man's Switch）— 漏打卡就通知紧急联系人"
date: 2026-09-26
category: 工具
businessModel: SaaS 订阅，免费版引流 + 高级功能收费
monetization: 每月 $5-20 订阅费；企业版按需定制；一次性买断Lifetime license
barrier: 需要基础全栈开发能力（Node.js + PostgreSQL + 前端）
skills: Web 开发、定时任务调度、短信/邮件集成
paybackPeriod: 2-4 周可上线 MVP，1-3 个月达到首个付费用户
investment: 服务器 $5-10/月，域名 $12/年，短信 API（Twilio $0.007/条）
feasibility: 4
effortScore: 2
barrierScore: 1
monetizationEase: 4
source: Ask HN / Show HN
sourceUrl: https://news.ycombinator.com/item?id=47290413
summary: 借鉴 deadmansswitch.net 月入 $1K 的真实案例，做面向国内用户的 AI 增强版——定时提醒 + 多重告警渠道 + AI 内容生成。门槛极低，刚需场景明确。
tags: [SaaS, 个人安全, 自动化工具, 定时提醒, AI, MVP友好]
---

## 是什么

定期健康检查类工具：用户设置检查周期（每日/每周/自定义），如果在规定时间内没有手动签到，系统自动通过短信、邮件、Web Push 向预设的紧急联系人发送警报。

参考案例：
- **deadmansswitch.net**（2008 年创建，周末搭建，至今月入 ~$1,000）：邮箱通知型，已稳定运营 18 年
- **deadmansswitch.cloud**（2026-09 Show HN）：Node.js + PostgreSQL + PWA + Web Push，beta 期邀请制

## 商业模式

**免费版 + 付费订阅（Freemium）**

| 层级 | 价格 | 包含 |
|------|------|------|
| 免费 | $0 | 1 个检查项，邮件通知，最长 7 天周期 |
| 个人版 | $5/月 | 3 个检查项，短信+邮件+Push，自定义周期 |
| 家庭版 | $12/月 | 10 个检查项，无限联系人，AI 内容生成（自动生成检查报告） |
| 企业版 | 定制 | SSO、审计日志、多租户 |

**年收入潜力**：500 个付费用户 × $8 平均 = $4,800/月 × 12 = $57,600/年

## 变现方法

1. **订阅收入**：主要变现途径，按月付费
2. **增值服务**：短信套餐包（额外 100 条 $2）、优先客服
3. **企业定制**：为养老机构、独居老人监护做定制化部署，$500+/次
4. **白标授权**：把系统授权给养老院、健身工作室做内部工具

## 门槛

- **技术门槛**：低。Node.js + Express + PostgreSQL + Redis（可选），PWA 前端可用现成模板
- **资金门槛**：极低。服务器 $5/月，Twilio 按用量付费
- **资质门槛**：无特殊要求，隐私政策 + 服务条款即可

## 所需技能

1. Node.js / Express 后端
2. PostgreSQL 数据库设计
3. 定时任务（node-cron / Bull queue）
4. 邮件发送（Resend / SendGrid）
5. 短信集成（Twilio / 阿里云短信）
6. Web Push 通知（简单）

## 实操步骤

### Week 1：MVP 搭建
1. 注册 Twilio（$15 额度起步）+ Resend（免费额度）
2. 设计数据模型：User / CheckItem / Contact / AlertLog
3. 实现核心流程：创建检查项 → 设置周期 → 定时检查 → 未签到则告警
4. 部署到 Railway / Render（免费层）

### Week 2：前端 + 品牌
1. 用 Next.js + Tailwind 搭建 PWA（或直接复用 GitHub 开源方案）
2. 注册域名，配置 HTTPS
3. 添加仪表盘：查看检查状态、历史告警记录
4. 接入 Web Push（免费，无需付费）

### Week 3：增值功能
1. 添加 AI 内容生成：检查项描述自动优化（用智谱免费模型）
2. 添加多语言支持（中英双语）
3. 接入 Stripe / 支付宝订阅

### Week 4：推广获客
1. 在 Product Hunt 上线（免费）
2. 在 V2EX、即刻、Telegram 群推广
3. 写 SEO 文章："独居安全""远程监控""家庭紧急联系"

## 风险与坑

| 风险 | 应对 |
|------|------|
| 用户担心隐私（健康数据） | 端到端加密，最小化数据存储，明确的隐私政策 |
| 误报/漏报导致用户投诉 | 多重确认机制（先邮件再短信），可设置延迟阈值 |
| 短信成本不可控 | 限制免费版短信次数，超过后引导订阅 |
| 竞品复制 | 建立品牌和社区壁垒，专注本地化服务（中文+支付宝） |
| 法律责任 | 免责声明：仅供参考，不构成安全保障 |

## 证据/验证

- **deadmansswitch.net**：[官网](https://www.deadmansswitch.net/) HTTP 200 ✅，运营 18 年证明需求持续
- **deadmansswitch.cloud**：[Show HN 帖](https://news.ycombinator.com/item?id=47290413) HTTP 200 ✅，27 天前发布，邀请制验证市场兴趣
- **Ask HN $500/month 线程**：[帖文](https://news.ycombinator.com/item?id=49417766) 确认多人在做类似项目并盈利

> 💡 **搞钱启示**：这是一个「小而美」的长期订阅产品。不需要大规模增长，几百个付费用户就能实现稳定现金流。关键是把 Chinese user experience 做好（中文+支付宝+微信推送），这是国外产品做不到的。
