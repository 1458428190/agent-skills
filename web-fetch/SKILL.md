---
name: web-fetch
description: 网页内容抓取技能，提取网页正文内容，支持多种输出格式。无需 API Key，使用 trafilatura 库实现。
---

# Web Fetch Skill

网页内容抓取技能，智能提取网页正文，自动过滤广告、导航等无关内容。

## 功能特点

- **智能提取** - 自动识别正文内容，过滤广告、导航、页脚等
- **多种格式** - 支持 Markdown、纯文本、HTML 输出
- **保留结构** - 保留标题、段落、列表、表格等结构
- **元数据** - 提取页面标题、作者等元信息

## 使用方法

```bash
# 默认抓取（Markdown 格式）
python .claude/skills/web-fetch/scripts/fetch.py "https://example.com"

# 指定输出格式
python .claude/skills/web-fetch/scripts/fetch.py "https://example.com" --format text
python .claude/skills/web-fetch/scripts/fetch.py "https://example.com" --format html

# 保留链接和图片
python .claude/skills/web-fetch/scripts/fetch.py "https://example.com" --include-links --include-images
```

## 输出格式

```json
{
  "url": "https://example.com",
  "title": "页面标题",
  "content": "# 正文内容\\n\\n提取的正文...",
  "format": "markdown",
  "length": 1234
}
```

## 依赖安装

```bash
pip install trafilatura
```

## 注意事项

1. trafilatura 对新闻文章、博客文章效果最好
2. 某些 heavily JavaScript 渲染的页面可能无法正确抓取
3. 始终输出 JSON 格式，避免编码问题
