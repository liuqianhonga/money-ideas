#!/usr/bin/env python3
"""两阶段过滤 news-service 输出"""
import json, sys

items = json.load(sys.stdin)["structuredContent"]["items"]

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
    '埃博拉','沉船','选举','空袭','战争','疫情','国有化',
    '扎波罗热','乌方','伊朗','哥伦比亚','刚果','以色列','捷克','斯塔默','导弹','医院',
    '华为','腾讯','阿里','字节','美团','京东','百度','小米','OPPO','VIVO',
]

keep1 = [i for i in items if not any(kw in i.get('title','') for kw in exclude_kw)]
print(f"阶段一后剩余: {len(keep1)}/{len(items)}")

# 阶段二：白名单精筛
keep_kw = ['Show HN','Product Hunt','AI Agent','微信AI','小程序','Figma','MCP',
    'Computer use','Obsidian plugin','CLI工具','预测市场','PPT','代写','副业','创业',
    'Alternative to','Has anyone deployed','How did you set up','Have you ever given',
    'What surprised you about','Quickbooks','e-Residency','Estonia',
    'redesign','redesigned','search box','开屏广告','下架','关停','裁员',
    'AI','GPT','Claude','LLM','Agent','RAG','个人','独立开发','SaaS','API','变现',
    '收入','赚钱','付费','订阅','SEO','营销','推广','替代','平价替代','开源替代',
    'workflow','零代码','低代码','无代码','Prompt','OpenAI','DeepSeek','Qwen',
    'side project','self-hosted','selfhosted','local-first','model','deployment',
    'Open-source','open source','github','git','Docker','rust','go language',
    'independent developer','solo founder','bootstrapped','profitable','revenue',
    'tailwind','shopify','ecommerce','ecom','saas',
    'syntax highlighter','WebGPU','quantum','satellite','radio',
    'DDoS','read the docs','macbook','printer',
]

keep2 = []
for i in keep1:
    title = i.get('title','').lower()
    summary = i.get('summary','').lower()
    combined = title + ' ' + summary
    if any(kw.lower() in combined for kw in keep_kw):
        keep2.append(i)

print(f"阶段二后剩余: {len(keep2)}/{len(keep1)}")
print(json.dumps(keep2, ensure_ascii=False, indent=2))
