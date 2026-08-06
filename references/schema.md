# 项目数据 Schema（frontmatter 规范）

每个项目是一个 Markdown 文件，放在 `src/projects/YYYY-MM-DD-<slug>.md`。
文件名 = 收集日期 + slug，天然可回溯。

## 必填字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `title` | 项目名称 | "AI 宠物摄影服务" |
| `date` | 收集日期 (YYYY-MM-DD) | 2026-08-06 |
| `category` | 分类：工具/内容/电商/服务/流量/教育/其他 | 服务 |
| `businessModel` | 商业模式一句话 | 按次收费的本地服务 |
| `monetization` | 变现方法详细说明 | 单次拍摄 ¥199-399，可卖套餐 |
| `barrier` | 门槛 | 需要基础摄影 + AI 工具使用 |
| `skills` | 所需技能能力 | 摄影、Prompt 工程、小红书运营 |
| `paybackPeriod` | 变现周期 | 1-2 个月 |
| `investment` | 投入成本 | 前期 ¥2000 设备+素材 |
| `feasibility` | 可行性评分 1-5 | 4 |
| `effortScore` | 实施难度 1-5（1=易做 5=难做） | 2 |
| `barrierScore` | 门槛 1-5（1=低门槛 5=高门槛） | 2 |
| `monetizationEase` | 变现难易 1-5（5=极易变现） | 4 |
| `source` | 出处名称 | Hacker News Show HN |
| `sourceUrl` | 出处链接（可验证） | https://news.ycombinator.com/item?id=... |
| `summary` | 一句话摘要 | 用 AI 给宠物做写真，本地服务 |
| `tags` | 标签数组 | [AI, 摄影, 本地服务] |

> **信心指数（confidence）**：由 `effortScore`/`barrierScore`/`monetizationEase` 三个子维度自动合成 0-100（权重 变现40% + 难度30% + 门槛30%），无需手写。计算逻辑见 `references/confidence-score.md`。
> 新项目**必须填写**三维评分字段，否则指数默认按中间值 3 计算。

## 正文内容要求

正文用 Markdown 详细拆解，至少包含：
1. **项目是什么** — 做什么，解决什么问题
2. **怎么赚钱** — 变现路径拆解
3. **为什么能赚钱** — 市场需求/差异化
4. **实操步骤** — 从零开始的行动清单
5. **风险与坑** — 需要注意的地方
6. **证据/验证** — 出处、案例、数据支撑

## 质量原则

- **重质不重量**：每天 2-5 个高质量项目，不做数量填充
- **可行可落地**：个人或小团队能复制的项目
- **注明出处**：sourceUrl 必须真实可访问
- **诚实评估**：可行性评分要保守，不吹不黑
