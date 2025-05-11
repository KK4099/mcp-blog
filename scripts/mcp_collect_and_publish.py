#!/usr/bin/env python3
"""
抓取 MCP 工具 → GPT-4o 生成中文教程 → 写入 Hugo Markdown → Git push
@author: KK4099
"""
import os, json, time, re, subprocess, hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Set

import requests
from tqdm import tqdm
import typer
from dotenv import load_dotenv

# ---------- 环境变量 ----------
load_dotenv()
GPT_API_KEY  = os.getenv("GPT_API_KEY")
GPT_API_URL  = os.getenv("GPT_API_URL", "https://www.manusn.com/v1/chat/completions")
GPT_MODEL    = os.getenv("GPT_MODEL", "gpt-4o")
GH_TOKEN     = os.getenv("GH_TOKEN")             # Optional，加速 GitHub API
MAX_ITEMS    = int(os.getenv("MAX_ITEMS", "100"))
HEADERS_GH: Dict[str, str] = {"Accept":"application/vnd.github+json"}
if GH_TOKEN: HEADERS_GH["Authorization"] = f"Bearer {GH_TOKEN}"

REPO_ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = REPO_ROOT / "content" / "posts"
TRACK_FILE  = REPO_ROOT / "tracked_tools.json"

INCLUDE_KEYWORDS = [
    r"modelcontextprotocol", r"model context protocol",
    r"mcp-server", r"\\w+-mcp", r"browser-tools-mcp", r"mcp-sdk"
]
EXCLUDE_KEYWORDS = [
    r"minecraft", r"coder pack", r"minecraft protocol",
    r"minecraft proxy", r"matrix control protocol"
]
INC_PAT  = re.compile("|".join(INCLUDE_KEYWORDS), re.I)
EXC_PAT  = re.compile("|".join(EXCLUDE_KEYWORDS), re.I)

app = typer.Typer(help="Collect MCP tools and publish to Hugo blog")

# ---------- 工具函数 ----------
def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\-]+", "-", text.lower()).strip("-")
    return text[:60] or hashlib.md5(text.encode()).hexdigest()[:12]

def github_search(max_items: int) -> List[Dict]:
    q = "modelcontextprotocol OR \"Model Context Protocol\" OR mcp-server in:name,description"
    url = f"https://api.github.com/search/repositories?q={q}&per_page=100"
    items, page = [], 1
    pbar = tqdm(desc="GitHub", unit="repo")
    while len(items) < max_items:
        resp = requests.get(f"{url}&page={page}", headers=HEADERS_GH, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("items", [])
        if not data: break
        for r in data:
            items.append({
                "name": r["full_name"],
                "url": r["html_url"],
                "description": r.get("description") or "",
                "updated": r["pushed_at"],
                "source": "github"
            })
            pbar.update(1)
            if len(items) >= max_items: break
        page += 1
    pbar.close()
    return items

def filter_items(raw: List[Dict]) -> List[Dict]:
    out = []
    for it in raw:
        txt = f"{it['name']} {it['description']}".lower()
        if INC_PAT.search(txt) and not EXC_PAT.search(txt):
            out.append(it)
    return out

def load_tracked() -> Set[str]:
    if TRACK_FILE.exists():
        return set(json.loads(TRACK_FILE.read_text()))
    return set()

def save_tracked(ids: Set[str]) -> None:
    TRACK_FILE.write_text(json.dumps(sorted(ids), ensure_ascii=False, indent=2))

def gpt_tutorial(item: Dict) -> Dict:
    prompt = f"""你是一名中文技术作者，请基于以下 MCP 工具仓库信息，写一篇 600~1000 字的教程：
工具名称：{item['name']}
工具链接：{item['url']}
工具描述：{item['description']}

产出格式（JSON）：
{{
  "title": "...",
  "tutorial_html": "<p>...</p>",
  "tags": ["tag1","tag2"]
}}"""
    payload = {
        "model": GPT_MODEL,
        "messages":[{"role":"user","content":prompt}],
        "temperature":0.6
    }
    headers = {"Authorization": f"Bearer {GPT_API_KEY}"}
    r = requests.post(GPT_API_URL, json=payload, headers=headers, timeout=60)
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {
            "title": item["name"],
            "tutorial_html": f"<p>{content}</p>",
            "tags": ["MCP"]
        }
    return data

def write_markdown(info: Dict, tutorial: Dict) -> Path:
    slug = slugify(info["name"])
    md_path = CONTENT_DIR / f"{slug}.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    front = (
        f"---\n"
        f"title: \"{tutorial['title']}\"\n"
        f"date: {datetime.now(timezone.utc).isoformat()}\n"
        f"tags: [{', '.join(['\"'+t+'\"' for t in tutorial.get('tags', [])])}]\n"
        f"draft: false\n"
        f"---\n\n"
    )
    md_path.write_text(front + tutorial["tutorial_html"], encoding="utf-8")
    return md_path

def git_commit_push(msg: str):
    subprocess.run(["git","add","."], check=True)
    res = subprocess.run(["git","commit","-m",msg])
    if res.returncode == 0:
        subprocess.run(["git","push"], check=True)

# ---------- 主流程 ----------
@app.command()
def main(max: int = MAX_ITEMS, dry_run: bool = False, initial: bool = False):
    print("🚀 开始抓取 MCP 工具...")
    raw_items = github_search(max)
    items = filter_items(raw_items)

    tracked = load_tracked()
    new_items = items if initial or not tracked else [it for it in items if it["url"] not in tracked]

    if dry_run:
        print(f"将发布 {len(new_items)} 条：")
        for it in new_items[:5]:
            print(" -", it["name"], it["url"])
        return

    if not new_items:
        print("今日无新增 MCP 工具。")
        return

    for it in new_items:
        print(f"✍️ 生成教程 → {it['name']}")
        tut = gpt_tutorial(it)
        write_markdown(it, tut)
        tracked.add(it["url"])
        time.sleep(2)   # 尊重速率

    save_tracked(tracked)
    git_commit_push(f"auto: add {len(new_items)} MCP tools")
    print(f"✅ 已提交 {len(new_items)} 篇文章，等待 GitHub Actions 构建。")

if __name__ == "__main__":
    app() 