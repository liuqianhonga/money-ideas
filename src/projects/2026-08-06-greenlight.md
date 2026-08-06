---
layout: project-layout.njk
title: "Greenlight：应用商店上架预检扫描器"
date: 2026-08-06
category: 开发者工具
businessModel: Freemium SaaS（待验证）
monetization: 免费基础扫描 + 订阅高级检查项；上架前扫描 App Store/Google Play 合规问题
barrier: 低 — API 检查 + 规则库
skills: 移动开发、应用商店政策知识
paybackCycle: 3-6 个月
cost: 低
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 4
source: HN Show HN
sourceUrl: https://github.com/RevylAI/greenlight
summary: 上架前自动扫描你的 App 有没有踩 App Store/Google Play 审核红线，避免「被拒后改两周」
tags: [开发者工具, SaaS, 海外, 移动应用, 审核, 开源]
---

## 是什么

Greenlight 是一个「上架预检扫描器」：开发者在提交 App Store / Google Play 之前，先用它扫描一遍，提前发现会被审核拒绝的问题（隐私清单缺失、权限滥用、元数据问题等）。

## 怎么赚

- Freemium：免费扫描基础项 + 订阅高级合规检查/自动修复建议
- 目标用户：独立开发者 + 中小团队（被拒一次损失两周发布时间）
- 开源版引流 + SaaS 变现（典型开发者工具路径）

## 核心打法

1. **痛点精准**：App 审核被拒是开发者的普遍噩梦，一次被拒 = 两周时间损失
2. **规则库化**：把审核规则整理成可检查清单（持续更新）
3. **开源引流**：GitHub 开源基础版 → 开发者试用 → 商业版转化

## 行动建议

- 开发者工具「规则库 + 自动化检查」是轻量好做的方向
- 紧跟平台政策更新（Apple/Google 每年多次改规则）建立护城河
- CI/CD 集成（GitHub Action）提升用户粘性

## 风险

- 规则变化快，需要持续维护
- 巨头（如 fastlane 生态）可能推出免费替代
