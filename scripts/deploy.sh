#!/usr/bin/env bash
# 每日赚钱项目站点部署脚本
# 用途：cron job 在写入新的项目 markdown 后调用，完成 构建→Git push→Vercel 部署
set -euo pipefail

PROJECT_DIR="/home/sxl/projects/money-ideas"
VERCEL_TOKEN="${VERCEL_TOKEN:-$(grep -oP '(?<=VERCEL_TOKEN=).*' /home/sxl/.hermes/.env | head -1)}"

cd "$PROJECT_DIR"

echo "=== 1. Eleventy 构建 ==="
npm run build 2>&1 | tail -5

echo "=== 2. Git 提交 ==="
git add -A
if git diff --cached --quiet; then
  echo "无变更，跳过提交"
else
  git commit -m "Auto update: 每日赚钱项目收集 - $(date +%Y-%m-%d)" 2>&1 | head -3
  git push origin main 2>&1 | tail -3
fi

echo "=== 3. Vercel 部署 ==="
npx vercel --prod --yes --token "${VERCEL_TOKEN}" 2>&1 | tail -5

echo "=== 4. 线上验证 ==="
URL=$(npx vercel ls money-ideas --token "${VERCEL_TOKEN}" 2>/dev/null | grep -oP 'https://[a-z0-9-]+\.vercel\.app' | head -1)
if [ -z "$URL" ]; then URL="https://money-ideas-six.vercel.app"; fi
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "https://money-ideas-six.vercel.app")
echo "线上状态: HTTP $HTTP_CODE (固定域名 money-ideas-six.vercel.app)"
if [ "$HTTP_CODE" = "200" ]; then
  echo "✅ 部署成功"
else
  echo "⚠️ 线上状态异常，请检查"
fi
