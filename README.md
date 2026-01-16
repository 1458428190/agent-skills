# Agent Skills

Claude Code / AI Agent 通用技能集合，可复用的工具脚本。

## 技能列表

### [web-search](./web-search/) - 联网搜索

支持 Google、DuckDuckGo、Bing、百度 四个搜索引擎。

```bash
python web-search/scripts/search.py "搜索内容"
python web-search/scripts/search.py "搜索内容" --engine google --num 10
```

**依赖**: `pip install duckduckgo-search httpx beautifulsoup4 lxml`

---

### [web-fetch](./web-fetch/) - 网页抓取

智能提取网页正文内容，自动过滤广告和无关信息。

```bash
python web-fetch/scripts/fetch.py "https://example.com"
python web-fetch/scripts/fetch.py "https://example.com" --format text --include-links
```

**依赖**: `pip install trafilatura`

---

## 使用方式

### 1. 直接使用

```bash
# 搜索
python web-search/scripts/search.py "AI量化交易"

# 抓取网页
python web-fetch/scripts/fetch.py "https://example.com/article"
```

### 2. 集成到 Claude Code

将 skill 目录复制到你的项目 `.claude/skills/` 下：

```bash
cp -r web-search /path/to/your/project/.claude/skills/
cp -r web-fetch /path/to/your/project/.claude/skills/
```

### 3. 作为模块导入

```python
from web_search.scripts.search import search

results = search("Python教程", engine="google", num_results=5)
print(results)
```

---

## 配置说明

### Google 搜索（可选）

如需使用 Google 搜索，需要配置 API Key：

1. 获取 [Google API Key](https://console.cloud.google.com/)
2. 创建 [ Programmable Search Engine](https://programmablesearchengine.google.com/) 获取 CX ID
3. 设置环境变量：

```bash
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_CX_ID="your_cx_id"
```

或使用 DuckDuckGo（默认，无需配置）。

---

## 许可

MIT License
# agent-skills
