---
layout: project-layout.njk
title: "AI 额度转售经纪：帮创业公司把用不完的 API 额度变现（token broker 套利）"
date: 2026-08-17
category: 服务
businessModel: 低买高卖 API 信用额度的中间商（broker）
monetization: 以 30-80% 折扣收购创业公司剩余 API 额度，再以低于官网价转售，赚差价
barrier: 中（需要资金池 + 信任背书 + 合规判断，属灰色地带）
skills: 销售/谈判、API 成本计算、风险识别、渠道运营（TG/Reddit/邮件）
paybackPeriod: 1-2 个月
investment: 低-中（启动资金 0.5-5 万用于收购额度；时间主要是获客）
feasibility: 3
effortScore: 2
barrierScore: 3
monetizationEase: 3
source: Hacker News
sourceUrl: https://vectoral.com/blog/who-are-the-token-brokers
summary: "HN 193 分：token broker 已成生态——有人批量收创业公司用不完的 API 额度再 30-80% 折扣转售，单 broker 声称日消费 $100k，市场量级千万级"
tags: [AI, API, 套利, 中间商, 灰色地带]
---

## 是什么

[《Who Are the Token Brokers?》](https://vectoral.com/blog/who-are-the-token-brokers)（HN 193 分 71 评论）揭示了一个正在快速商业化的市场：**AI 额度转售经纪**。

创业公司（尤其拿了 YC/加速器/云厂商赠金的）经常有大量用不完的 API 信用额度，而 token broker 就是专门收购这些「闲置额度」，再以 30-80% 折扣转售给需要 API 但嫌官网贵的团队。文中一位 broker 声称自己的账户每天能消费 $100k，直接给买家发代理 endpoint 而不是 API key，按用量里程碑结算。

生态已经成型：
- **信用交易市场**：AI Credits、AICreditMart（卖家列表从 MiniMax、ElevenLabs 到 OpenAI、Anthropic，折扣 30-80%）
- **批量折扣路由**：CheapCredits（自称 bulk pricing，全线模型 flat 40% off）、Tokvana、Neokens
- **地下渠道**：Telegram 频道（几百订阅者的 ai credits 交易频道）、Reddit r/saasforsale、r/indiehackers（有人卖 $10k OpenAI credits、$2,500 YC Startup School credits）

## 商业模式

**低买高卖信息差**：收购端拿到创业公司折扣额度（成本价甚至更低），销售端以下面两种方式变现：
1. 直接转售额度：买家拿到你的 endpoint/proxy，按用量付费（省 40-80%）
2. 批发路由：以「批量采购协议」名义做聚合网关，赚每 token 差价

## 变现方法

1. **收购-转售差价**（核心）：找到有闲置额度的公司（加速器毕业公司、融到钱的 AI 团队），谈折扣收购，再在渠道/私域转售
2. **代理抽成**：做中间人撮合，成交抽取 5-15% 佣金
3. **聚合网关订阅**：把多个廉价额度池整合成一个 OpenAI/Claude 兼容 API 端点，按会员订阅收费
4. **额度代销分成**：帮额度持有方代销，赚分成

## 门槛

- **资金门槛**：中。收购需要垫资，起步 0.5-5 万人民币可以滚动
- **信任门槛**：高。买卖双方都要信任你——需要长期经营口碑、可验证交易记录
- **合规门槛**：高。低价转售违规获取的额度有欺诈风险；供应商 TOS 通常禁止转售；涉灰产时可能触发风控甚至法律问题
- **技术门槛**：低。proxy 搭建有现成方案，不需要自己训练模型

## 所需技能

- 销售和谈判（主动触达创始人、处理 inbound）
- 渠道运营（Telegram/Reddit/邮件 list）
- API 成本核算（了解各模型定价、峰值/非峰值价差）
- 风险识别（分辨来源是否合规、额度是否真实有效）

## 变现周期

**1-2 个月**：联系 10-20 个潜在卖家 + 建立买家渠道，第一笔撮合或转售即可见钱。规模化需要 3-6 个月积累信任。

## 投入成本

- 资金：垫资收购 0.5-5 万（可先用「佣金撮合」模式零成本试水）
- 时间：早期全职 2-4 周做渠道建设中，后期每周 10-15 小时维护
- 工具：TG 频道/社群、邮件、API 测试工具，几乎零成本

## 可行性

**3/5**。市场真实存在（量级千万级）、需求验证过（买家对 40-80% 折扣没有抵抗力），但合规和信任风险不可忽视，不适合没有风险承受能力的人。

## 实操步骤

1. **验证市场**：去 r/indiehackers、r/saasforsale 搜 "API credits for sale"，TG 搜 "ai credits"，看真实成交帖和报价
2. **建立侧供给**：从你认识的融过资/拿过赠金的团队确认是否有闲置额度（YC Startup School 每年发 $2,500 OpenAI credits 只是其中一种）
3. **先做撮合佣金**：不垫资，帮买家找到卖家，成交抽 5-10%——零风险验证
4. **测试结算模式**：用小额（几百美元）跑通「收购→测试额度→转售→收款」闭环
5. **做渠道**：开一个 TG 频道或邮件 list，持续发布库存和报价，积累信任
6. **合规化升级**：有体量后做正规 DPA、明确免责条款（参考 CheapCredits 的 GDPR Data Processing Agreement）

## 风险与坑

- ⚠️ **灰色地带**：多数供应商 TOS 禁止转售，被查到会封号、冻结额度
- ⚠️ **来源不干净**的额度可能来自盗刷/欺诈账号，买家出事你先背锅
- ⚠️ 供应商涨价/改条款会瞬间吃掉你的价差（DeepSeek 2026-08 涨价就是例子）
- ⚠️ 结算是先款后货还是先货后款？收货后被跑单风险要自己扛
- ⚠️ 别碰信用卡盗刷、注册机、风控欺诈等明显违法供给——这不是「套利」是「犯罪」

## 证据/验证

- 出处：[向量研究文章 Who Are the Token Brokers?](https://vectoral.com/blog/who-are-the-token-brokers)（2026-08-10）+ [HN 讨论 193 分](https://news.ycombinator.com/item?id=49320611)
- 平台验证：AI Credits / AICreditMart / cheapcredits.ai（HTTP 200）/ Tokvana / Neokens
- 个人建议：**先做撮合佣金模式**验证，不要一上来就垫资，这个市场水深，谨慎入局