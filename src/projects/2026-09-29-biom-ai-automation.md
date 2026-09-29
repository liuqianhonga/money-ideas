---
layout: project-layout.njk
title: "Biom - AI自动化工作空间（代理即服务潜力）"
date: 2026-09-29
category: 工具
businessModel: SaaS订阅 + 托管服务（模型费用另计）
monetization: ①订阅费：团队使用费；②托管模式：抽成20-30%模型费用；③企业定制
barrier: 中等（需AI Agent开发经验）
skills: AI Agent开发、Next.js/React、向量数据库、API集成
paybackPeriod: 3-6个月（冷启动期）
investment: 时间投入为主，服务器成本约$50-100/月
feasibility: 3
effortScore: 4
barrierScore: 3
monetizationEase: 3
source: Show HN
sourceUrl: "https://www.biom.dev/"
summary: "面向初创团队的AI自动化可视化工作空间，支持Hermes/Claude Code，24/7托管或自带Agent。已通过Emma的帖子获得11个付费客户，团队正在迭代。"
tags: ["AI Agent", "SaaS", "自动化", "初创工具", "Show HN"]
---

## 是什么

Biom 是专门为AI原生团队设计的自动化工作空间。核心价值：
- **单一事实来源**：团队所有决策、文档、上下文集中在一个地方
- **可视化自动化**：用自然语言描述，自动生成工作流
- **双模式运行**：可托管（24/7跑，含模型费）或自带Agent（用你自己的key）

**已验证数据：**
- 第一周31个注册，前一周仅9个
- 11个付费客户（全部来自Emma的帖子，非广告投放）
-  churn 2/11（同一原因，已在roadmap修复）
- Runway 14个月（当前burn rate）

## 商业模式

**三层收入：**
1. **订阅费**：团队按月付费使用平台
2. **托管抽成**：选择托管模式，抽取20-30%模型调用费用
3. **企业定制**：私有化部署+定制开发（高客单价）

## 变现方法

| 模式 | 定价假设 | 备注 |
|------|---------|------|
| 基础订阅 | $29-99/月/团队 | 参考同类工具定价 |
| 托管抽成 | 模型费的20-30% | 用户付API费+Biom抽成 |
| 企业定制 | $5k-20k/项目 | 需销售跟进 |

## 门槛分析

- **技术门槛**：高（需熟悉AI Agent框架、向量检索、工作流引擎）
- **资金门槛**：中（需要初期服务器+API额度投入）
- **时间门槛**：6个月+才能验证PMF

## 实操步骤（如果你要做类似产品）

1. **MVP阶段**（4-6周）
   - 核心功能：可视化工作流编辑器 + 1个Agent模板
   - 技术栈：Next.js + LangChain/LlamaIndex + Supabase
   - 目标：做出能跑的demo，找10个种子用户测试

2. **验证阶段**（2-3个月）
   - 在HN/PH发布，收集反馈
   - 访谈10个目标用户，确认付费意愿
   - 调整定价和功能优先级

3. **增长阶段**（3-6个月）
   - 完善Agent库（覆盖常见场景）
   - 建立社区/Discord
   - 考虑Product Hunt冲刺

## 风险与坑

- **用户获取成本高**：B2B工具需要销售周期，Emma的帖子是偶然成功
- **模型依赖风险**：API价格上涨会压缩利润空间
- **竞合关系**：用户可能直接用Cursor/Claude Code自己搭，不买单
- **churn风险**：工具类SaaS churn通常10-15%/月

## 证据/验证

- ✅ 网站已上线：https://www.biom.dev/（HTTP 200）
- ✅ 有定价页：https://www.biom.dev/pricing.html
- ✅ 真实客户数据（创始人公开分享：11付费客户，churn分析，runway计算）
- ✅ GitHub开源部分代码：https://github.com/jesse51002/Biom
- ✅ Discord社区活跃

## 启发点

Biom 的成功模式值得学习：
1. **从个人需求出发**：创始人自己需要这个工具
2. **极简MVP**：没有admin后台，先跑通核心流程
3. **诚实沟通**：公开churn原因、未 shipping 的功能
4. **社区驱动**：通过Discord和发帖获取早期用户

**如果你不是技术出身**，可以考虑做 Biom 的**实施服务**——帮startup搭建AI自动化系统，按项目收费。

---

**信心指数：54/100**（effort=4, barrier=3, monetization=3）
公式：100 × (0.4×0.6 + 0.3×0.25 + 0.3×0.25) = 54

⚠️ 这个项目的可行性评分较低，主要是因为：
- 技术门槛高（需AI Agent开发能力）
- 市场已有巨头（Linear、Notion等可能跟进）
- 需要销售能力获客，非纯产品驱动

但如果你是开发者，这是一个值得关注的方向——**代理即服务（Agent-as-a-Service）** 是新兴赛道。
