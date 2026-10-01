---
layout: project-layout.njk
title: "简历制作 SaaS 模仿（Standard Resume 模式）"
date: 2026-10-01
category: 工具
businessModel: 做国内版简历制作工具，支持 LinkedIn/脉脉导入，订阅制收费
monetization: 免费增值，高级功能 ¥9.9-29.9/月 或 ¥99-199/年
barrier: 需要 Web 开发能力（Next.js + React + Firebase/Supabase）
skills: 前端开发、PDF 生成、支付集成、SEO
paybackPeriod: 变现周期 3-6 个月
investment: 前期投入 ¥500-2000（域名 + 服务器 + Stripe/微信支付）
feasibility: 3
effortScore: 3
barrierScore: 3
monetizationEase: 4
source: Sideidea 案例研究
sourceUrl: "http://sideidea.com/article/57"
summary: "Standard Resume 五年前为找工作自建，Product Hunt 发布后成副产品，月入 $3K。支持 LinkedIn 导入是唯一差异化，零推广靠口碑增长"
tags: [SaaS, 简历, Product Hunt, 副业, 订阅制]
---

## 项目是什么

**Standard Resume** 是一个简历制作 SaaS，核心功能：
- 在线编辑简历，导出 PDF 或生成网页简历
- **唯一支持 LinkedIn 导入**的简历编辑器
- 多种专业模板
- 免费增值模式

**创始人背景**：Riley Tomasek，五年前为自己找工作自建，2015 年发布到 Product Hunt 成为当日 #1 产品。后来在 Dropbox 工作，把 Standard Resume 当副产品运营。2020 年全职投入，现在月入 $3K（约 ¥2W）。

## 怎么赚钱

### 变现路径拆解

| 层级 | 定价 | 功能 |
|------|------|------|
| 免费版 | ¥0 | 基础模板，PDF 导出，带水印 |
| 高级版 | ¥19.9/月 | 无水印、更多模板、网页简历 |
| 年度版 | ¥199/年 | 同上，省 2 个月费用 |
| 企业版 | 定制 | 团队协作、批量生成 |

### 为什么能赚钱

1. **刚需市场**：每年数千万毕业生 + 职场人换工作需要简历
2. **信息差**：国内没有成熟的在线简历制作工具（知页简历已过气）
3. **产品驱动增长**：Product Hunt / 知乎 / 即刻 发布即可获客
4. **低边际成本**：SaaS 模式，用户增长不增加成本

## 实操步骤

### 第 1 步：MVP 验证（2 周）
```
技术栈推荐：
- 前端：Next.js + Tailwind CSS
- 后端：Supabase（免费额度够用）
- PDF 生成：react-pdf 或 puppeteer
- 支付：Stripe 或 微信支付
- 部署：Vercel 免费额度
```

### 第 2 步：核心功能开发（2-3 周）
1. 简历编辑器（拖拽式）
2. 10-20 个专业模板
3. PDF 导出
4. 网页简历生成（SEO 友好）

### 第 3 步：差异化功能（1 周）
- **脉脉/LinkedIn 导入**（核心价值）
- AI 简历优化（调用 GPT API）
- 面试问题预测

### 第 4 步：发布获客
1. Product Hunt 发布（英文市场）
2. 即刻/V2EX 发帖（国内市场）
3. 知乎回答「怎么写简历」问题
4. 小红书发简历模板分享

## 风险与坑

| 风险 | 应对 |
|------|------|
| 竞争激烈 | 聚焦 LinkedIn/脉脉导入差异化 |
| 用户留存低 | 简历是低频需求，考虑扩展功能（如面试模拟） |
| 付费转化难 | 免费版要有足够价值，付费版要明显更好 |
| 技术维护 | 选择成熟技术栈，减少后期维护成本 |

## 证据/验证

- **Sideidea 案例**：Standard Resume 月入 $3K，零推广
- **用户基数**：中国每年应届生 + 职场人超过 5000 万
- **竞品现状**：知页简历已过气，超级简历有付费墙问题，市场有机会

## 信心指数

**75/100** — 市场需求真实，但竞争激烈，需要差异化定位。适合有前端开发能力的创业者。

---

**大司备注**：这个项目验证成本低，建议先用 No-code 工具（如 Softr + Airtable）做出 MVP，验证需求后再写代码。关键是找到差异化切入点。
