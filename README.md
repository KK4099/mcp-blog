# mcp-
搜集全网mcp 工具

## 自动采集 & 发布 MCP 教程

本仓库包含脚本 `scripts/mcp_collect_and_publish.py`，每天自动：

1. 搜索全网新发布的 MCP 工具  
2. 调用 GPT-4o 生成中文教程  
3. 把教程写入 `content/posts/`（Hugo Markdown）  
4. Git 提交 → 触发 GitHub Actions → Hugo 构建 → Pages 发布  

### 本地调试

```bash
python scripts/mcp_collect_and_publish.py --dry-run   # 只看将发布哪些条目
python scripts/mcp_collect_and_publish.py --initial   # 首次全量生成
```

环境变量

复制 .env.example → .env 并填入：

| 变量         | 说明                |
| ------------ | ------------------- |
| GPT_API_KEY  | 你的 GPT-4o Key     |
| GPT_API_URL  | 中转地址（默认已填）|
| GH_TOKEN     | PAT，Actions 用于推送|

GitHub Actions 请在仓库 Settings → Secrets → Actions 添加同名变量。
