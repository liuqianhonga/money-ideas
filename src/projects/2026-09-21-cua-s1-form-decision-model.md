---
layout: project-layout.njk
title: "CUA-S1 – 表单填写专用 AI 决策模型（706K 参数本地推理）"
date: 2026-09-21
category: 工具
businessModel: "开源模型 + 服务化部署，面向需要表单自动化场景的企业"
monetization: "API 调用收费 / 私有化部署授权 / 企业定制训练"
barrier: "中等（需要 AI 训练经验）"
skills: "Python、PyTorch、表单解析、小模型微调"
paybackPeriod: "3-6 个月"
investment: "前期训练成本约 ¥500-2000（GPU 时间），部署成本极低"
feasibility: 4
effortScore: 3
barrierScore: 3
monetizationEase: 4
source: "Show HN"
sourceUrl: "https://github.com/trycua/cua"
summary: "706K 参数的小型决策模型，专门用于 Computer Use 场景的表单填写，准确率 99.7%，本地推理仅需 7-9ms，比 GPT-4 快 30 倍"
tags: [AI Agent, Computer Use, 表单自动化, 小模型, 开源]
---

## 是什么

CUA-S1 是一个专为 Computer Use 场景设计的小型决策模型，706K 参数，2.8MB 模型文件。它不生成文本，而是对给定的选项进行概率打分，输出最可能的操作（CLICK、CHECK、SKIP 等）。

## 商业模式

**核心卖点**：在表单填写等窄场景中，用小模型替代大模型，降低 97% 的推理成本。

**变现路径**：
1. **API 服务**：按调用次数收费，¥0.01/次
2. **私有化部署**：企业内网部署授权，¥5000-20000/年
3. **定制训练**：根据客户表单类型微调模型，¥5000-10000/次

## 门槛分析

| 维度 | 评分 | 说明 |
|------|------|------|
| 技术门槛 | ⭐⭐⭐ | 需要 Python/PyTorch 基础，小模型微调 |
| 数据门槛 | ⭐⭐ | 需要合成数据或真实表单数据 |
| 资金门槛 | ⭐ | 训练成本约 ¥500-2000 |
| 资质门槛 | ⭐ | 无特殊资质要求 |

## 变现周期

- **MVP 验证**：1-2 周（用公开表单数据集测试）
- **最小产品**：2-4 周（封装成 API）
- **首单成交**：1-3 个月（找 1-2 个种子客户）
- **稳定收入**：3-6 个月

## 实操步骤

### 第一步：复现模型（1-2 天）
```bash
git clone https://github.com/trycua/cua
cd cua && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# 运行示例测试
python scripts/run_example.py
```

### 第二步：验证准确率（1 天）
用公开表单数据集（如 FormGAN、WebTS）测试模型表现，记录准确率。

### 第三步：封装 API（2-3 天）
用 FastAPI 封装成 REST API：
```python
from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
def predict(form_data: dict):
    # 调用 CUA-S1 模型
    result = model.predict(form_data)
    return {"actions": result}
```

### 第四步：部署上线（1 天）
- 方案 A：Vercel/Cloudflare Workers 部署（免费额度足够初期）
- 方案 B：自己买台 ¥200/月的轻量服务器

### 第五步：获客
1. **HN/Reddit**：发 Show HN 文章
2. **技术社区**：掘金、V2EX、知乎发教程
3. **直接联系**：找表单自动化需求的创业公司

## 风险与坑

1. **模型泛化能力**：不同表单格式差异大，可能需要针对每个客户微调
2. **竞争**：大模型厂商（OpenAI、Anthropic）可能内置类似功能
3. **数据隐私**：企业客户可能担心表单数据外泄，需要私有化部署方案
4. **维护成本**：表单 UI 经常改版，模型需要持续更新

## 证据验证

✅ **GitHub 仓库**：https://github.com/trycua/cua（MIT 许可证）
✅ **HN 讨论**：43 points, 4 comments（2026-09-19）
✅ **性能数据**：本地推理 7-9ms vs GPT-4 260ms
✅ **准确率**：99.7% vs Jev 83.6%

## 信心指数

**85/100**（变现 4 + 难度 3 + 门槛 3 = 0.4×4 + 0.3×(6-3) + 0.3×(6-3) = 1.6 + 0.9 + 0.9 = 3.4 → 85）

这是一个典型的"小而美"项目：**用最小模型解决最具体问题**，适合有 AI 背景的开发者快速落地。
