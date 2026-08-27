---
layout: project-layout.njk
title: "AI 内容协商服务：帮网站一行 Accept 头把 Markdown 喂给 AI Agent（acceptmarkdown 范式）"
date: 2026-08-27
category: 工具
businessModel: "技术服务 + 开源插件双轨——基于 acceptmarkdown.com 验证的「内容协商」范式（网站用 Accept: text/markdown 给 AI Agent 提供去导航/脚本/广告的纯 Markdown 版本），个人可做成 WordPress/静态站插件按站点授权售卖，或提供「网站 AI Agent 友好化改造」实施服务"
monetization: 付费插件（按站点/按年授权）、AI Agent 友好化改造实施服务费（改造一个站收 1-3k）、企业文档站内容协商迁移、连带提供 Markdown 渲染/缓存托管
barrier: 低中（核心是加一条响应头 + 输出简化版 HTML→Markdown，技术门槛不高；难点在于对不同 CMS/框架落地做产品化封装）
skills: HTML/CSS/HTTP 协议理解、前端构建、Markdown 处理、主流 CMS/静态站框架（WordPress/Next/Astro）任选其一、基本 Rails 或中间件能力
paybackPeriod: 1-2 个月可出第一版插件并签下首批改造客户（需求已被 acceptmarkdown 54 赞验证）
investment: <¥2000（域名 + 文档站/插件市场账号，以时间为主）
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 4
source: Hacker News
sourceUrl: https://acceptmarkdown.com/
summary: "HN 54 赞 acceptmarkdown 验证了「AI Agent 友好内容交付」需求——用 Accept: text/markdown 内容协商让网站给 AI Agent 提供去噪纯 Markdown（省 token、提检索信噪比、降延迟）。个人围绕此范式做插件化产品（按站点授权）+ AI 化改造服务，是 AI 基建工具的新变现点"
tags: [AI, AI Agent, Markdown, 内容协商, SEO, 工具, 独立开发, 插件]
---

# AI 内容协商服务：帮网站把 Markdown 喂给 AI Agent

> **Hacker News 54 赞项目 [acceptmarkdown.com](https://acceptmarkdown.com/)**：当一个 AI Agent 抓取你的网站时，它并不需要导航栏、脚本、弹窗和广告布局——它只想要正文。acceptmarkdown 展示了用 **HTTP 内容协商（`Accept: text/markdown`）** 来实现这一点的标准做法：**你的站本来就有内容，只是再提供一个 Markdown 变体，让 Agent 客户端跳过 nav/scripts/layout，直接读正文。** 这不是一个赚大钱的产品本身，但它验证了一个正在快速增长的刚需——**「我的网站对 AI Agent 友好吗？」**，这正是可以产品化、可以收服务费的入口。

## 是什么

「AI 内容协商」是指网站根据 HTTP `Accept` 头，给抓取它的客户端返回不同格式：普通浏览器得到完整 HTML 页面（带导航、样式、交互），而 AI Agent（声明 `Accept: text/markdown`）得到干净、无干扰的 Markdown 正文。

核心价值三点：
1. **省 token**：去掉导航/样式/脚本/布局包裹后，Agent 的上下文预算全部花在正文上，字节量大幅下降。
2. **检索信噪比高**：没有广告、相关推荐栏、弹窗污染，RAG 流程 embed 的内容更干净、检索更准。
3. **延迟低**：抓到的东西更少，首个 token 更快。

官方给的标准做法：`curl -sI -H "Accept: text/markdown" <URL>` 看源站返回什么，然后让中间层/框架在识别到该 Accept 头时输出简化版 HTML→Markdown。

## 商业模式

**技术服务 + 开源插件双轨**，两条腿走路：

- **插件产品化**：做成 WordPress 插件 / Next/Astro 中间件 / Cloudflare Worker 改造脚本，按站点或按年授权收费（$29-99/站/年）。套用「模板工具 (2,1,4) ≈ 84 分」的变现路径，一次性开发、大量分发。
- **实施服务**：帮企业/内容站/文档站做「AI Agent 友好化改造」，一个站收 1000-3000 元，顺带交付性能报告（改造前后 token 数对比）增强说服力。

## 变现方法

1. 付费插件授权（一次开发 N 次销售，边际成本趋零）
2. 网站 AI 化改造实施服务（按站收费）
3. 企业知识库/文档站内容协商迁移（B 端大单）
4. 附带 Markdown 缓存/渲染托管订阅
5. 写「How I made my site AI-friendly」教程/AI 内容交付报告引流（SEO Acquire）

## 门槛

技术门槛低中：核心是加响应头 + 输出简化 Markdown 变体。真正的门槛在于**产品化封装**——针对主流 CMS/框架做开箱即用的插件，保证不同站点都能一键启用。会 HTML/CSS + 任一框架 + HTTP 协议即可起步。

## 所需技能

- HTTP 协议/响应头理解（Accept、Vary 头需要一起配）
- HTML → Markdown 转换（用 turndown 等现成库）
- 一门后端/中间件能力（Node/Rails/Cloudflare Worker 均可）
- 一个 CMS 或静态站框架（WordPress/Next/Astro 选一）
- 基本营销：能在 HN/WordPress 生态/Twitter 铺开

## 变现周期

1-2 个月出第一版插件 + 签首批实施客户（需求已由 acceptmarkdown 54 赞验证，非拍脑门）。工具型产品一旦在 WordPress/静态站生态铺开，可做成长尾订阅收入。

## 投入成本

<¥2000：域名 + 文档站 + 插件市场账号（WordPress.org 免费）。主要成本是时间——大约 3-6 周开发 + 2 周落地首批客户。

## 可行性

**4/5**。理由：需求已验证（acceptmarkdown 高赞证明「给 AI Agent 做内容交付」是真实痛点）、技术门槛低、变现路径清晰（工具+服务双轨）、且与当前 AI 基建趋势强相关。扣 1 分因为需要一定的产品化能力和营销渠道，不是「写个脚本就躺赚」。

## 实操步骤

1. 通读 acceptmarkdown.com 的 Quick start 与 Recipes，理解内容协商 + Vary 头标准
2. 选一个你最熟的生态（推荐 WordPress 或 Next.js）做参考实现
3. 写一个插件/中间件：识别 `Accept: text/markdown` → 输出简化 Markdown 正文
4. 把这个插件开源一个精简版（积累口碑 + 扒 Hacker News 流量）
5. 做付费 Pro 版（多站点管理、缓存、分析面板），上 WordPress.org/插件市场
6. 同时对外提供「AI Agent 友好化改造」实施服务，用改造前后 token 对比做案例
7. 在 HN/IndieHackers/Twitter 发「Why your site isn't AI-readable」（同类项目 54 赞验证了话题热度）

## 风险与坑

- **实施服务偏一次性**：改造完就结束，复购弱（要靠插件订阅对冲）
- **生态碎片化**：WordPress/Next/Astro 各有实现，要克制别一下铺太多框架
- **与 CDN/缓存的兼容**：Vary 头没配好会被缓存混着返回，需测试
- **需求还在早期**：AI Agent 抓取的量目前还不稳定，付费意愿在早期客户（AI 创业者、文档站）里更强
- **别把它做成纯技术教程**：要落到「能卖的产品/服务」而不是「能看的博客」

## 证据/验证

- 来源：Hacker News 54 赞 [Serve Markdown to AI Agents with Accept Headers](https://news.ycombinator.com/item?id=49454764)
- 验证：`curl -sI -o /dev/null -w "%{http_code}" https://acceptmarkdown.com/` → **HTTP 200** ✅
- 官方正文透出三价值点（tokens / retrieval / latency）与标准做法（`Accept: text/markdown` + RFC 7763/8288/9110）