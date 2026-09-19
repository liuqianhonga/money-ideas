---
layout: project-layout.njk
title: "Fudge Explorer — 给AI提供设计审美的截图数据库"
date: 2026-09-19
category: 工具
businessModel: "订阅制SaaS，按网站截图+设计元数据数据库收费，核心卖点是MCP集成让LLM有'设计品味'"
monetization: "月度订阅（$600+/月且环比接近翻倍增长），面向设计师/AI应用开发者/品牌团队"
barrier: "中 - 数据壁垒高（2年手工收集），但技术实现难度低"
skills: "Web爬虫/Chrome插件、数据库设计、MCP协议集成、前端展示"
paybackPeriod: "数据积累期6-12个月，见收入3-6个月"
investment: "中 - 服务器+带宽成本$200-$500/月，主要是数据冷启动时间成本"
feasibility: 3
effortScore: 3
barrierScore: 3
monetizationEase: 4
source: "Ask HN 宝藏线程"
sourceUrl: "https://explorer.withfudge.com"
summary: "2年手工收集的网站截图+排版元数据库，$600+/月且快速增长，差异化定位是给LLM提供设计审美"
tags: [设计数据, MCP, SaaS, 数据壁垒]
---

## 是什么

**Fudge Explorer** 是一个设计素材数据库，核心功能是：
- 收集网站各section的截图（非整站，而是section级别）
- 每个section附带完整排版元数据：字体（leading、weight、tracking、size）、foundry、设计师、色值、色彩系统
- 支持按风格/行业/排版类型筛选浏览
- **核心差异化：MCP集成**，让LLM能直接查询"什么样的设计好看"，给AI应用提供设计品味

**目标用户**：
- 设计师（灵感参考、竞品分析）
- AI应用开发者（给AI Agent提供设计审美参考）
- 品牌/营销团队（快速找参考）

**竞争格局**：Mobbin、Landbook、Refero都在做类似的事，但Fudge选择**不正面竞争**，而是定位"给LLM提供设计审美"（MCP集成），这是2026年新赛道。

## 商业模式

一句话说清怎么赚钱：
> **Freemium SaaS订阅** — 免费浏览基础功能，付费解锁高级筛选/导出/MCP API。

**收入结构**（来自HN线程自述）：
- 当前$600+/月，环比接近翻倍增长
- 核心用户是AI应用开发者（给Agent提供设计上下文）和设计师
- 按席位/用量订阅，企业版更贵

**护城河分析**：
- **数据壁垒**：2年手工收集+Chrome插件众包扩展，新站没有这个数据积累
- **元数据深度**：不只是截图，还有字体foundry/设计师等深层信息
- **MCP定位**：给LLM提供设计context是新赛道，先发优势明显

## 门槛

| 维度 | 难度 | 说明 |
|------|------|------|
| 技术门槛 | ⭐⭐ | Web爬虫+数据库+前端，1-2个月可MVP |
| 数据门槛 | ⭐⭐⭐⭐ | 高质量section截图+元数据需要长期积累，这是真正的壁垒 |
| 资金门槛 | ⭐⭐ | 服务器+带宽$200-$500/月 |
| 认知门槛 | ⭐⭐⭐ | 需要理解"设计元数据"的价值，不是拍脑袋能做出来的 |

## 所需技能

- Web爬虫/Chrome插件开发（数据收集）
- 数据库设计（截图+元数据关联）
- 前端展示（响应式截图画廊）
- MCP协议集成（2026年新技能）
- 设计知识（理解排版/字体/色彩系统）

## 变现周期

- **数据冷启动**：3-6个月（手工收集+众包插件）
- **MVP上线**：6-9个月
- **首批付费用户**：上线后1-3个月（HN/Product Hunt发帖）
- **稳定增长**：12-18个月后进入增长通道

## 投入成本

| 项目 | 金额/月 |
|------|------|
| 服务器（对象存储+计算） | $100-$300 |
| 带宽（截图下载） | $50-$200 |
| 域名+杂项 | $10-$50 |
| Chrome插件维护 | $0（自有） |
| **总计** | **$150-$550/月** |

时间成本：数据收集是主要成本，2年手工+众包

## 可行性评分

**feasibility: 3/5**

技术不难，但：
- 数据冷启动期长（3-6个月才有价值）
- 需要持续众包扩展（Chrome插件维护）
- MCP赛道还在早期，用户教育成本高
- 但一旦数据积累完成，护城河很深

## 实操步骤

1. **验证MCP需求**（1周）
   - 搜索"design MCP" "design system LLM context"
   - 找AI应用开发者访谈：你们给Agent提供设计参考吗？痛点是什么？
   - 确认MCP集成是真需求还是概念

2. **数据收集引擎**（2-4周）
   - 开发Chrome插件：用户浏览网站时自动截取section+提取元数据
   - 众包机制：插件用户贡献数据，积分/免费额度激励
   - 数据库设计：section_id, website, style_tags, typography_meta, color_system, font_foundry

3. **MVP上线**（4-8周）
   - 前端：响应式截图画廊 + 筛选器（行业/风格/排版）
   - 免费层：浏览+基础筛选
   - 付费层：高级筛选/导出/MCP API/团队功能
   - Stripe集成

4. **获客**（持续）
   - 发Show HN（"I built a design database for LLMs"）
   - Product Hunt
   - 写MCP集成教程（给AI开发者用）
   - 设计师社区（Dribbble/Behance）引流

5. **众包扩展**（持续）
   - 优化Chrome插件体验
   - 数据质量控制（去重/质量评分）
   - 定期发布"设计趋势报告"（数据洞察内容营销）

## 风险与坑

- **数据冷启动**：没有数据就没有价值，3-6个月可能零收入
- **爬虫合规**：网站section截图涉及版权，需只存元数据+低清预览
- **MCP赛道未成熟**：LLM设计context需求可能不如预期
- **竞品跟进**：Mobbin/Landbook可能快速加MCP功能
- **带宽成本**：截图存储+下载成本高，需CDN优化

## 证据/验证

- **产品官网**：https://explorer.withfudge.com （HTTP 200 ✅）
- **收入来源**：HN Ask HN线程自述"$600+/month, almost doubling since last month"
- **数据壁垒**：线程自述"collected for almost 2 years, crowdsourced via Chrome extension"
- **MCP定位**：线程自述"giving LLMs design taste"（2026年新差异化）

## 类似赛道延伸

| 方向 | 说明 |
|------|------|
| UI组件数据库 | 不只是截图，而是可复用的Figma组件+代码 |
| 品牌风格数据库 | 按品牌收集设计语言，AI生成品牌一致的设计 |
| 动效数据库 | 收集网站动效（Lottie/CSS animation），给AI提供动效参考 |
| 数据可视化参考库 | 收集优秀数据图表，按场景分类，AI生成交互式图表参考 |
