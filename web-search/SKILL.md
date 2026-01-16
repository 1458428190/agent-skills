---
name: web-search
description: 免费联网搜索技能，支持 DuckDuckGo、Bing、百度、Google 四个搜索引擎。当需要联网查询资料、搜索最新信息时使用此技能。无需任何 API Key，完全免费。
---

# Web Search Skill

免费联网搜索技能，支持多个主流搜索引擎。

## 支持的搜索引擎

- **Google** - 默认引擎，搜索结果质量最高
- **DuckDuckGo** - 完全免费无限制，稳定性好
- **Bing** - 微软搜索，通过 HTML 解析
- **百度** - 国内搜索，通过 HTML 解析（可能不稳定）

## 使用方法

```bash
# 默认搜索 (Google，前10条结果)
python .claude/skills/web-search/scripts/search.py "搜索内容"

# 指定引擎
python .claude/skills/web-search/scripts/search.py "搜索内容" --engine bing
python .claude/skills/web-search/scripts/search.py "搜索内容" --engine baidu
python .claude/skills/web-search/scripts/search.py "搜索内容" --engine duckduckgo

# 指定结果数量
python .claude/skills/web-search/scripts/search.py "搜索内容" --num 20
```

## 输出格式

```json
{
  "query": "搜索内容",
  "engine": "duckduckgo",
  "count": 3,
  "results": [
    {
      "title": "结果标题",
      "url": "https://example.com",
      "snippet": "结果摘要..."
    }
  ]
}
```

## 注意事项

1. 首次使用前需要安装依赖：`pip install duckduckgo-search httpx beautifulsoup4 lxml`
2. **Google 是默认引擎，搜索结果质量最高**
3. 其他引擎通过 HTML 解析实现，可能因网站结构变化而失效
4. 始终输出 JSON 格式，避免编码问题
