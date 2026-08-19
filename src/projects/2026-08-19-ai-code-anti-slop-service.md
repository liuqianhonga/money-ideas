---
layout: project-layout.njk
title: "AI 代码『反注水』质量门禁服务（接住 AI 写码质量困局）"
date: 2026-08-19
category: 服务
businessModel: B2B 服务——帮团队搭 anti-AI-slop 代码质量规则/CI 门禁 + AI 代码审查
monetization: 一次性搭建费 + 订阅（规则库更新/持续审查）+ 咨询
barrier: 低中（懂 Lint/CI 即可，工具已现成）
skills: 前端/后端工程、Lint 规则配置、CI/CD、代码评审
paybackPeriod: 1-2 个月
investment: 时间为主，约 ¥200-1,000
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 4
source: GitHub Trending
sourceUrl: https://github.com/dmmulroy/anti-slop
summary: "AI 写代码越来越快，但『AI 注水代码』（低证据、凑数、复制粘贴的 TS/JS/其他）成了团队共痛。anti-slop 把『反注水』做成 Oxlint 规则，avouch 用『只审你改的代码』做本地免费审查——需求明确、工具现成，帮团队搭质量门禁是最快到手的服务单"
tags: [AI, 代码质量, Lint, CI, 开发工具, 服务]
---

## 是什么

AI 生成代码有个共性痛点：**外观正常、逻辑注水**——没证据就下结论、凑数重复、克隆他人的低质量模式。这种代码过了编译、能跑，但经不起长期维护。随着 AI 占代码比例上升，这个"质量负债"成了团队真实烦恼。

两个项目精准戳中它：
- [anti-slop](https://github.com/dmmulroy/anti-slop)（2.6k 星）：把"反注水"写成 Opinionated Oxlint 规则，自动**拒绝低证据的 TS/JS 模式**——让 AI 写的"样子货"在 CI 阶段就被拦下
- [avouch](https://github.com/mukundzha/avouch)（Show HN）：作者"取消了付费 AI code reviewer，自己写了个免费的本地版"，只审你**改过的那部分**而不是继承下来的旧代码

两个信号指向同一结论：**AI 时代的代码质量审查是刚需，且从"人工审"转向"规则引擎 + 本地审查"**。对个人服务商来说，这是门槛低、需求明确的接单入口。

## 商业模式

**B2B 服务：给团队搭'反 AI 注水'质量体系**。工具免费开源帮你验证需求，你卖的是"搭建/定制/持续维护"这个工程能力，而不是工具本身。

## 变现方法

1. **一次性搭建费**：帮团队把 anti-slop/Oxlint 接入 CI，定制针对他们技术栈的规则集（见 Code 的单、几千到几万元不等）
2. **订阅式规则/审查服务**：持续更新规则库、定期 AI 代码审计，按月收费
3. **模板/规则包售卖**：把通用反注水规则集打包成"企业版规则包"多次售卖
4. **配套咨询**：AI 代码规范的培训 + 落地辅导
5. **私有化审查**：企业不想用云审查，做本地/私有部署的 AI 代码审查

## 门槛

- **技术门槛低中**：核心是 Lint 规则 + CI 集成，属工程常用技能，一线工程师即可
- **需求已验证**：anti-slop 2.6k 星 + avouch 上 HN → 需求真实
- **工具免费**：无需自研核心，站在开源工具之上

## 所需技能

- 工程能力：Lint/静态分析、CI/CD（GitHub Actions 等）
- 逻辑：能把"注水代码"特征转成可配置规则
- 售前：能跟技术负责人讲清 ROI（省多少 Review 工时/少多少坑）

## 变现周期

1-2 个月。第一单从"帮一个认识的团队搭起来"开始，1-2 周可交付；转订阅后形成经常性收入。

## 投入成本

几乎全时间成本。初期 ¥200-1,000（域名/示例服务器），规则引擎全部开源免费。

## 可行性

**4/5**。AI 代码占比注定持续上升，"谁给 AI 代码把关"的问题只会更痛；工具链已现成，个人即可交付首单，无需重资源。

## 实操步骤

1. 本地跑通 anti-slop + avouch，理解"注水代码"典型模式（高置信断言无依据、重复克隆块、过量 TODO/FIXME）
2. 搭一个公开 demo 仓库：展示"一条 AI 注水代码 → 规则拦截 → 报错信息"
3. 写 2-3 篇短文："AI 写的 JavaSc/TS 为什么又慢又脆——反注水规则实战"，发技术社区
4. 找到 1 个在用 AI 编程的团队（大概率周围就有），免费帮他们在 CI 接上规则集，换取 case study + 转介绍
5. 把通用规则包产品化，开始按项目/按月收费
6. 扩展到其它语言栈和框架（Go/Python/前端框架规则）

## 风险与坑

- **规则误伤**：规则太激进会误拦正常代码，惹恼团队——先从小步、白名单开始
- **需求被大厂抢**：GitHub/Cursor 可能在编辑器里内置反注水——锁定"On-Prem + 定制"护城河
- **度量难证明**：要能量化"拦截了多少坏代码/省了多少审阅"，否则客户难续费
- **别只卖工具**：卖免费工具不赚钱，一定要走到"搭建/订阅/定制"的服务层

## 证据/验证

- anti-slop：https://github.com/dmmulroy/anti-slop（HTTP 200，2.6k 星）
- avouch：https://github.com/mukundzha/avouch（HTTP 200，Show HN）
- 数据来源：GitHub API + Hacker News Show HN，2026-08-19 验证
