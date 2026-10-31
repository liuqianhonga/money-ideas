---
layout: project-layout.njk
title: "Overtone - 多屏适配字幕工具（一键生成横竖屏字幕，创作者必备）"
date: 2026-10-31
category: 工具
businessModel: CLI工具+SaaS服务
monetization: 开源免费 + 企业版API调用收费
barrier: 技术中等
skills: TypeScript、视频处理、CLI开发
paybackPeriod: 0-3个月
investment: 时间投入为主，服务器成本极低
feasibility: 4
effortScore: 2
barrierScore: 2
monetizationEase: 4
source: Show HN
sourceUrl: "https://github.com/lonthq/overtone-captions"
summary: 开源字幕切割工具，一文件适配16:9和9:16，CLI+video.js插件，MIT协议，视频创作者痛点明确
tags: [字幕工具, 视频创作, CLI, 开源, 创作者工具]
---

## 是什么

**Overtone** 是一个开源字幕工具，核心创新在于「一文件多屏适配」——同一个 `.overtone.json` 文件，自动切割出适合 16:9 横屏和 9:16 竖屏的字幕格式。

- **CLI工具**：命令行直接处理字幕文件
- **video.js插件**：Web端播放器自动适配
- **多模型转录**：支持 OpenAI、Azure STT、Elevenlabs
- **MIT开源协议**：可自由商用

## 商业模式

**Freemium + API调用收费**
- 基础功能开源免费（CLI工具）
- 企业API调用按量收费（转录服务）
- 高级功能（自定义主题、批量处理）订阅制

## 变现方法

1. **API服务收费**：转录服务按分钟计费，$0.002-0.01/分钟
2. **企业版订阅**：批量处理、自定义主题、团队协作
3. **插件/模板市场**：售卖高级字幕样式包
4. **SaaS托管**：在线编辑器+自动发布工作流

## 门槛

| 维度 | 评估 |
|------|------|
| 技术门槛 | 中等（TypeScript + 视频处理） |
| 资金门槛 | 低（开源起步，API调用成本可控） |
| 资质门槛 | 无特殊要求 |

## 所需技能

- TypeScript/JavaScript 开发
- 视频处理基础（ffmpeg/ WebCodecs）
- CLI 工具开发经验
- API 集成能力（OpenAI/Azure）

## 变现周期

**预计 0-3 个月**
- 第1个月：开源发布，积累 star 和用户反馈
- 第2-3个月：推出企业版 API，开始变现
- 长期：订阅收入 + API调用费

## 投入成本

- **时间**：1-2周开发 MVP
- **资金**：几乎为零（开源+自托管API）
- **服务器**：可选云托管，月成本 $10-50

## 可行性评分：4/5

**优势**：
- 痛点真实：视频创作者需要同时维护横竖屏字幕
- 开源策略正确：降低获客成本
- MIT协议无法律风险
- 已有完整实现可参考

**劣势**：
- 市场竞争（Submagic、Descript 等）
- API成本需要控制

## 实操步骤

1. **研究现有实现**：克隆 https://github.com/lonthq/overtone-captions 理解架构
2. **本地运行**：安装依赖，跑通演示
3. **差异化定位**：
   - 聚焦中文市场（中文字幕适配）
   - 或聚焦特定平台（抖音/小红书/B站专用格式）
4. **MVP开发**：
   - 核心功能：SRT转overtone.json + 横竖屏切割
   - CLI工具 + 简单Web界面
5. **发布开源**：GitHub + Hacker News Show HN
6. **变现路径**：
   - 免费版：CLI工具
   - 付费版：在线编辑器 + 批量处理
   - 企业版：API服务

## 风险与坑

1. **市场竞争**：Descript、Submagic 已有类似功能
2. **API成本**：转录服务成本可能侵蚀利润
3. **用户习惯**：创作者可能已习惯现有工具
4. **盗版风险**：开源代码可能被直接抄袭

## 证据/验证

- GitHub: https://github.com/lonthq/overtone-captions ✅ HTTP 200
- Demo: https://overtone.lont.ai/ ✅ HTTP 200
- Show HN 讨论: https://news.ycombinator.com/item?id=50293115 (19 points, 2 comments)

---

**💰 搞钱建议**：这类工具类项目最适合「开源引流 + 付费增值」模式。先免费积累用户，再通过企业级功能变现。建议聚焦中文短视频市场（抖音/快手/小红书），这是 Overtone 的空白市场。
