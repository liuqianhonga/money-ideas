---
layout: project-layout.njk
title: "Launch：Mac 脚本启动器（$12 一次性买断）"
date: 2026-08-06
category: 独立开发
businessModel: 一次性买断制（$12）+ 7 天试用
monetization: 单次付费 $12，无订阅；可扩展通过付费脚本市场/Pro 版提价
barrier: 低 — 个人开发者 + macOS 开发能力即可；已有商业成品验证
skills: Swift/macOS 开发、JavaScript 脚本编写、产品发布（GitHub/开发者论坛）
paybackPeriod: 1-3 个月（作者已完成开发并上线）
investment: 时间为主（约 2-4 周开发）；Apple 开发者账号 $99/年
feasibility: 3
effortScore: 2
barrierScore: 2
monetizationEase: 3
source: Hacker News Show HN
sourceUrl: https://news.ycombinator.com/item?id=49162808
summary: 个人开发者做的 Mac 脚本启动器，卖 $12 买断，7 天试用
tags: [独立开发, Mac, 工具, 买断制, 海外]
---

## 项目是什么

Launch 是一个 macOS 原生脚本启动器（Script Launcher），作者独立开发。它运行 JavaScript 脚本，内置打开应用、找 emoji、cd 到目录、复制/移动/删除文件等脚本，用户可自定义脚本，支持 Git 同步。

**关键商业事实**：7 天免费试用 + **$12 一次性买断**（非订阅）。

来源：Hacker News Show HN（2026-08-04 发布），站点 https://staunchapps.com/launch/ 验证可访问，页面明确「There's a 7 day trial download or a $12 once off purchase.」

## 怎么赚钱

1. **$12 买断**：低成本决策，适合独立开发者第一桶金
2. **脚本生态**（可选扩展）：用户脚本分享市场，抽成或 Pro 版
3. 后续可迭代 Pro 版（$29）增加高级功能，保留买断制心理锚点

## 为什么能赚钱

- **「小工具卖钱」模式在海外成熟**：Mac 开发者社区（r/macapps、Indie Hackers）有大量 $10-20 买断小工具成功的案例
- **痛点真实**：开发者/重度用户日常重复操作（启动应用、跑脚本、管理文件），想要比 Raycast/Alfred 更轻的「纯脚本」方案
- **$12 价格点低**：冲动消费门槛低，试用 7 天后付费率不错
- **买断 vs 订阅**：2026 用户订阅疲劳，一次性买断反而成为差异化卖点（作者特意强调）

## 实操步骤（从零开始）

1. 用 Swift + AppKit/SwiftUI 做 macOS 原生应用，核心是「运行 JS 脚本」的引擎
2. 内置常用脚本库（文件操作、应用启动、Git），降低首次使用门槛
3. 做 7 天试用（StoreKit 或自家试用逻辑）
4. 定价 $12，发布到 Product Hunt + r/macapps + Show HN
5. 迭代：根据用户反馈加脚本，形成「脚本库 → 社区」飞轮

## 风险与坑

- 竞品强：Raycast（免费+订阅）、Alfred（$45 买断）、LaunchBar——差异化必须清晰（纯脚本化、轻量）
- 一次性买断收入天花板低：卖 1000 份才 $12,000；要靠量大或后续 Pro 版
- macOS 新系统 API 变动维护成本
- 中国市场定价要重估：$12 对国内用户偏贵，可考虑 ¥29-49

## 证据/验证

- 产品页真实可访问：https://staunchapps.com/launch/ （Title: "Launch - A Place for Your Scripts | Staunch Apps"）
- Show HN 讨论帖：https://news.ycombinator.com/item?id=49162808
- 商业事实来自作者 HN 原文：「7 day trial download or a $12 once off purchase」
- 模式对标：海外 Mac 小工具买断市场成熟（无数案例）
