---
layout: project-layout.njk
title: "Keet：AI 视频课程生成器（YC S24 验证的教育 AI 赛道）"
date: 2026-08-12
category: 工具
businessModel: 订阅制（Suno 式按学分付费）
monetization: 月订阅给生成学分，学分兑换课程生成；3 次免费试用引流
barrier: 中（需接入 LLM+视频生成 API，有 API 成本，无资质要求）
skills: LLM 应用开发、Manim/Remotion 视频渲染、移动端开发
paybackPeriod: 3-6 个月
investment: 前期以 API 费用为主（千元级），时间投入 2-3 个月
feasibility: 4
effortScore: 3
barrierScore: 2
monetizationEase: 4
source: Launch HN
sourceUrl: https://news.ycombinator.com/item?id=49259309
summary: YC S24 团队用 LLM+Manim/Remotion 生成结构化视频课程，Suno 式订阅变现，验证「AI 自动生成教育内容」赛道
tags: [AI工具, 教育, 订阅制, 视频生成, YC]
---

## 是什么

Keet 是一个 AI 课程生成 App（[trykeet.com](https://www.trykeet.com/)），输入任何主题（如"中世纪工程"、"咖啡冲煮"），自动生成**结构化视频课程**：短讲解视频 + 测验 + 互动练习，并模仿真实课程大纲排课。

两位创始人 Zack 和 Tommy（YC S24）发现自学最大的痛点是**缺少课程结构**：YouTube 视频、ChatGPT 对话、书堆在一起，学不连贯。Keet 补上这个结构层——先按 Biglan 学科分类（数理化/人文/应用），再定制讲解方式（数学用推导、人文用史料叙事），用 Manim 渲染数学可视化、Remotion 做动画讲解。

HN 评分 36 分、39 条评论，属于 Launch HN 中等热度，但 YC 背景 + 产品完成度值得关注。

## 商业模式

**Suno 式订阅**：每月订阅给用户「课程生成学分」，用学分兑换课程。免费用户送 3 次生成（TestFlight 里给了 3 次免费生成 + 邀请码 KEETHN），完成"免费体验→付费订阅"转化漏斗。

## 变现方法

1. **订阅制**（核心）：月度订阅卖学分，Suno 已验证这种模式在生成类产品可行
2. **免费额度裂变**：3 次免费生成让用户尝到甜头，付费转化
3. **后续可扩展**：企业培训定制（B2B 版课程生成）、学校/教育机构批量授权

## 门槛

- **技术门槛**：中等。LLM 出大纲 + Manim/Remotion 渲染视频 + 移动端 App，2-3 个月可做出 MVP
- **资金门槛**：低-中。API 成本是主要开销（视频生成+LLM），前期千元级可跑
- **资质门槛**：无

## 所需技能

- LLM 应用开发（Prompt 工程、结构化输出）
- 视频渲染（Manim 数学动画 / Remotion 动态图形）
- 移动端或 Web App 开发

## 变现周期

3-6 个月可看到第一笔订阅收入（参考：ScreenshotAPI 3 个月 20 个付费用户；Keet 团队已做一年迭代）。

## 投入成本

- 资金：API 费用为主，月几百元起
- 时间：2-3 个月 MVP（核心是课程生成 pipeline）

## 可行性：4/5

赛道验证充分：教育内容生成是 AI 确定性方向，Keet 用 YC 团队一年验证了「结构化课程」这个差异化点。个人可做**垂直领域**版本（如只做编程课程/考研课程/乐器教学），避开与 YC 团队正面竞争。

## 实操步骤

1. 选垂直领域（如：Python 入门、中考数学、吉他教程）
2. 搭课程生成 pipeline：LLM 出大纲 → 按章节生成讲解文案 → Manim/Remotion 渲染短视频
3. 做 Web/Mobile 端播放器 + 测验互动
4. 免费送 3 次生成，引导注册
5. 定价：月订阅 ¥30-60 或按课程买断
6. 发布到 Product Hunt / V2EX / 小红书（教育类目流量大）

## 风险与坑

- ⚠️ **API 成本失控**：视频生成贵，需限流+缓存，避免免费用户刷爆
- ⚠️ **内容质量质疑**：AI 生成课程可能被批评"浅"，垂直领域+人工审校兜底
- ⚠️ **大厂下场**：OpenAI/Google 可能直接做课程生成（ChatGPT 桌面版刚发布），小团队必须靠垂直深耕
- ⚠️ 移动端上架审核（教育类目）时间不可控

## 证据/验证

- Launch HN 原文：https://news.ycombinator.com/item?id=49259309（36 分 / 39 评论）
- 官网 HTTP 200 已验证：https://www.trykeet.com/
- 竞品信号：OpenAI 同日发布 ChatGPT Linux 桌面版（https://techcrunch.com/2026/08/11/openai-launches-chatgpt-desktop-app-for-linux/），教育 AI 赛道热度上升
