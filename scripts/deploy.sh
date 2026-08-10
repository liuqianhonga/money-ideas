#!/usr/bin/env bash
# 每日赚钱项目站点部署脚本
# 用途：cron job 在写入新的项目 markdown 后调用，完成 构建→Git push→重启本地 systemd 服务
set -euo pipefail

PROJECT_DIR="/home/sxl/projects/money-ideas"

cd "$PROJECT_DIR"

echo "=== 1. Eleventy 构建 ==="
npm run build 2>&1 | tail -5

echo "=== 2. Git 提交 ==="
git add -A
if git diff --cached --quiet; then
  echo "无变更，跳过提交"
else
  git commit -m "Auto update: 每日赚钱项目收集 - $(date +%Y-%m-%d)" 2>&1 | head -3
  git push origin main 2>&1 | tail -3 || echo "⚠️ git push 失败（不影响本地服务）"
fi

echo "=== 3. 重启本地 systemd 服务 ==="
systemctl --user restart money-ideas-web.service
sleep 1
systemctl --user is-active money-ideas-web.service

echo "=== 4. 本地验证 ==="
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "http://localhost:8100/")
echo "本地服务状态: HTTP $HTTP_CODE (http://localhost:8100)"
if [ "$HTTP_CODE" = "200" ]; then
  echo "✅ 部署成功，服务运行中"
else
  echo "⚠️ 本地服务异常，请检查 systemctl --user status money-ideas-web"
  exit 1
fi
