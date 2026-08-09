---
layout: project-layout.njk
title: "域名待售 DNS 信号服务（_for-sale 新标准商机）"
date: 2026-08-09
category: 服务
businessModel: 基于 RFC 10023 新标准的域名交易信号服务：监测/聚合/撮合待售域名，向买卖双方收费
monetization: 域名扫描 SaaS 订阅 / 交易撮合佣金 5-10% / 域名估值 API
barrier: 中低门槛：懂 DNS + 域名市场即可，个人或小团队可做，关键在跑得早
skills: DNS 技术、域名行业知识、爬虫/监控系统、Web 开发、交易撮合能力
paybackPeriod: 2-4 个月
investment: 前期 0-5000 元（域名、服务器、开发 40-80 小时）
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 4
source: Hacker News Front Page
sourceUrl: https://specification.website/spec/foundations/for-sale-dns/
summary: DNS 新标准允许域名用 TXT 记录声明「待售」（RFC 10023），296 分 HN 热帖验证需求，域名交易基础设施迎来新机会
tags: [域名, DNS, 交易, 新标准, 服务]
---

# 域名待售 DNS 信号服务（_for-sale 新标准商机）

## 是什么

2026-07 发布的 **RFC 10023** 定义了一个 DNS 新标准：域名主可以在自己域名的 `_for-sale.example.com` 叶节点发布 TXT 记录，**声明该域名待售**，可附上报价（furi 协商链接、ftxt 描述、fprice 要价）。

这解决了一个长期存在的「信号问题」：域名主想卖域名，但买家无从知道——WHOIS 隐私保护删掉了联系方式，冷邮件像垃圾邮件。现在**域名自己就能说「我在卖」**。

Hacker News 296 points、123 条评论（2026-08-08 首页），规范官网 [specification.website](https://specification.website/spec/foundations/for-sale-dns/) 同步上线。

## 商业模式

一句话：**做新标准的基础设施服务商——帮买家发现待售域名，帮卖家发布和卖出，两头收费。**

1. **扫描/监控 SaaS**：持续扫描热门域名库的 `_for-sale` TXT 记录，给域名投资者提供「新待售域名提醒」订阅（$29-99/月）
2. **交易撮合**：域名经纪人模式，撮合成功收 5-10% 佣金（域名市场惯例）
3. **估值 API**：结合 _for-sale 报价数据 + 成交数据，做域名估值 API 卖给出价工具/平台
4. **发布工具**：帮不懂 DNS 的域名主一键生成 _for-sale 记录（SaaS 后台 + 教程）

## 变现方法

1. **订阅制监控**：投资人最怕错过便宜好域名，「实时监控 + 提醒」是强付费点
2. **佣金**：大额域名交易（$10k+）佣金可观，一单顶一年订阅
3. **API 服务**：把扫描能力封装成 API，卖给域名市场（Sedo/Afternic 类平台）或 SEO 工具商
4. **增值服务**：交易保障（托管、过户服务），按单收费

## 门槛

- **技术门槛**：中低。DNS 查询（dig/API 批量查 TXT）、数据存储、Web 界面
- **行业门槛**：中。需要理解域名市场（买家/卖家/定价/过户流程），但这可以边做边学
- **资金门槛**：低。域名扫描成本低（一个 TXT 查询几乎免费），服务器月几十元
- **资质门槛**：交易撮合可能需要牌照（视地区），初期可只做「信息+工具」规避

## 所需技能

- DNS 基础（TXT 记录、批量查询、Rate limit 处理）
- 爬虫/调度系统（定时扫描、去重、增量更新）
- Web 开发（订阅后台、提醒系统）
- 域名行业知识（价值判断、交易流程）

## 变现周期

扫描工具 MVP **2-4 周** 可上线（核心就是批量 DNS 查询 + 提醒）。获取第一批域名投资人用户（他们聚集在 NamePros、域名论坛）后，**2-4 个月**可产生订阅收入。撮合佣金需要积累信任，周期更长。

## 投入成本

- 资金：0-5000 元（域名、服务器、可选收购种子域名做展示）
- 时间：MVP 40-80 小时，后续维护主要是扫描稳定性

## 可行性评分：4/5

理由：**新标准 = 信息差红利期**，目前做这个方向的人极少，先发优势明显；技术门槛低、成本低；域名交易市场成熟（年交易额数十亿美元），需求真实。扣分原因：标准刚发布（2026-07）实际采用率待验证，需赌早期采用曲线。

## 实操步骤

1. **读懂规范**：读 [RFC 10023 规范页](https://specification.website/spec/foundations/for-sale-dns/)（v=FORSALE1;ftxt/furi/fprice 字段格式）
2. **验证信号**：用 dig 手动查一批知名待售域名（如 sedo.com 挂售域名）看有多少已发布 _for-sale 记录，验证采用率
3. **做扫描器**：Python + dnspython 批量查询 TXT 记录，定时扫描（热门域名词库 10 万级），存数据库
4. **做提醒 SaaS**：用户订阅关键词（如「5 字母 .com 待售」），命中即推送（Telegram/邮件）
5. **发布获客**：HN 发帖 + NamePros/域名论坛分享 + 写「如何用 _for-sale 卖域名」教程（同时帮卖家普及标准）
6. **探索撮合**：积累到一定活跃卖家后，尝试做撮合（先做信息对接，佣金模式）

## 风险与坑

- **标准采用率不确定**：新标准可能普及慢，前期信号稀疏，需要耐心和营销推动（教程内容就是推动手段）
- **DNS 查询限流**：大规模扫描可能被 DNS 服务商限流，需要分布式/轮换策略
- **数据噪音**：域名主可能发布虚假报价或不及时更新，需要去重和状态验证
- **大厂跟进**：Sedo/GoDaddy 等域名巨头可能自己实现，个人靠「垂直 + 快速」建立 niche
- **法律边界**：撮合交易涉及合同和资金托管，前期只做信息层，避免合规风险

## 证据/验证

- 规范官网：[https://specification.website/spec/foundations/for-sale-dns/](https://specification.website/spec/foundations/for-sale-dns/) — **验证通过**（HTTP 200，含完整实现说明：TXT 记录格式、v=FORSALE1 字段定义）
- HN 讨论：[https://news.ycombinator.com/item?id=49221668](https://news.ycombinator.com/item?id=49221668) — 296 points，123 条评论（需求验证）
- 参考市场：Sedo、Afternic、GoDaddy 域名交易市场年交易额数十亿美元（行业成熟度证据）
