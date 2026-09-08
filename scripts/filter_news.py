#!/usr/bin/env python3
"""两阶段过滤 biz_opportunity 新闻数据"""
import json
import sys

# 阶段一：黑名单机械排除
exclude_kw = [
    '美联储','欧洲央行','特朗普','拜登','普京','俄乌','乌克兰','俄罗斯',
    'IPO','上市','融资丨','SPAC','涨停板','跌停板','股票','基金市场','公募',
    '央行','券商','债券','外汇','原油','油价','SpaceX','Agility',
    '英伟达','宁德时代','蔚来','理想','茅台','安踏',
    'A轮融资','B轮融资','C轮融资','近亿元',
    '教育','高考','文凭','就业','下沉',
    '手机','耳机','耳夹','体验',
    '茶饮','冰淇淋','世界杯','梅西',
    '战争','疫情','选举','空袭','埃博拉','扎波罗热',
    '医院','导弹','邮轮','石化','国有化',
    '华为','腾讯','阿里','字节','美团',
]

# 阶段二：白名单精筛
keep_articles = [
    'Show HN','Product Hunt','AI Agent','微信AI','小程序','Figma','MCP',
    'Computer use','Obsidian plugin','CLI工具','预测市场','PPT','代写','副业','创业',
    'Alternative to','Has anyone deployed','How did you set up','Have you ever given',
    'What surprised you about','Quickbooks','e-Residency','Estonia',
    'redesign','redesigned','search box','开屏广告','下架',
    'AI','GPT','Claude','LLM','Agent','RAG','个人','独立开发','SaaS','API','变现',
    '收入','赚钱','付费','订阅','SEO','营销','推广','替代','平价替代','开源替代',
    'workflow','零代码','低代码','无代码','Prompt','MCP Server',
]

# 读取数据
data = json.load(sys.stdin)
items = data.get('result', {}).get('structuredContent', {}).get('items', [])

print(f"原始数据: {len(items)} 条\n")

# 阶段一：黑名单过滤
stage1 = []
for item in items:
    title = item.get('title', '')
    if any(kw in title for kw in exclude_kw):
        print(f"❌ 排除: {title}")
        continue
    stage1.append(item)

print(f"\n阶段一后: {len(stage1)} 条\n")

# 阶段二：白名单精筛
stage2 = []
for item in stage1:
    title = item.get('title', '')
    summary = item.get('summary', '')
    text = f"{title} {summary}".lower()
    
    # 检查白名单关键词
    if any(kw.lower() in text for kw in keep_articles):
        stage2.append(item)
        print(f"✅ 保留: {title}")
    else:
        print(f"⬜ 过滤: {title}")

print(f"\n阶段二后: {len(stage2)} 条")

# 输出结果
result = {
    "stage1_count": len(stage1),
    "stage2_count": len(stage2),
    "filtered": stage2
}
print("\n\n=== JSON OUTPUT ===")
print(json.dumps(result, ensure_ascii=False, indent=2))
