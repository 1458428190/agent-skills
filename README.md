# Agent Skills

Claude Code / AI Agent 通用技能集合，可复用的工具脚本和技能指南。

## 技能列表

### Web & 网络

#### [web-search](./web-search/) - 联网搜索

支持 Google、DuckDuckGo、Bing、百度 四个搜索引擎。

```bash
python web-search/scripts/search.py "搜索内容"
python web-search/scripts/search.py "搜索内容" --engine google --num 10
```

**依赖**: `pip install duckduckgo-search httpx beautifulsoup4 lxml`

---

#### [web-fetch](./web-fetch/) - 网页抓取

智能提取网页正文内容，自动过滤广告和无关信息。

```bash
python web-fetch/scripts/fetch.py "https://example.com"
python web-fetch/scripts/fetch.py "https://example.com" --format text --include-links
```

**依赖**: `pip install trafilatura`

---

#### [browser](./browser/) - 浏览器自动化

基于 Chrome DevTools Protocol (CDP) 的浏览器自动化工具，无需 MCP 服务器。

```bash
# 启动 Chrome
node scripts/start.js --profile

# 导航
node scripts/nav.js https://example.com

# 执行 JavaScript
node scripts/eval.js 'document.title'

# 截图
node scripts/screenshot.js

# 可视化元素选择器
node scripts/pick.js "Click the submit button"
```

**依赖**: `npm install --prefix browser ws`

---

### 设计 & 前端

#### [ui-ux-pro-max](./ui-ux-pro-max/) - UI/UX 设计智能助手

包含 50 种风格、21 种配色方案、50 种字体搭配、20 种图表类型，支持 9 种技术栈。

```bash
python3 scripts/search.py "<关键词>" --domain <domain>
python3 scripts/search.py "minimal" --domain style
python3 scripts/search.py "SaaS" --domain product
```

**适用场景**: 网站设计、落地页、仪表板、管理面板、电商、SaaS、作品集等

---

#### [frontend-design](./frontend-design/) - 前端界面设计

创建高质量、具有独特设计感的前端界面，避免通用的 AI 生成风格。

**适用场景**: 网站、落地页、仪表板、React 组件、HTML/CSS 布局、Web UI 美化

---

#### [canvas-design](./canvas-design/) - 画布艺术设计

创建 PNG 和 PDF 格式的视觉艺术作品，基于设计哲学生成独特视觉设计。

**适用场景**: 海报、艺术作品、静态设计

---

#### [web-design-reviewer](./web-design-reviewer/) - 网页设计审查

通过可视化检查识别和修复网站设计问题，包括响应式设计、可访问性、视觉一致性等。

**适用场景**: 静态站点、React/Vue/Angular/Svelte 应用、Next.js/Nuxt/SvelteKit、CMS 平台

---

### 文档处理

#### [pdf](./pdf/) - PDF 处理工具集

全面的 PDF 操作工具包，支持文本和表格提取、创建新 PDF、合并/拆分文档、表单处理。

```python
from pypdf import PdfReader, PdfWriter

# 读取 PDF
reader = PdfReader("document.pdf")

# 提取文本
for page in reader.pages:
    text += page.extract_text()

# 合并 PDF
writer = PdfWriter()
writer.add_page(page)
```

**依赖**: `pip install pypdf pdfplumber reportlab`

---

#### [xlsx](./xlsx/) - Excel 表格处理

创建、编辑和分析电子表格，支持公式、格式化、数据分析和可视化。

```python
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Hello'
sheet['B2'] = '=SUM(A1:A10)'
wb.save('output.xlsx')
```

**依赖**: `pip install openpyxl pandas`

---

#### [docs-write](./docs-write/) - 文档写作指南

遵循 Metabase 的对话式、清晰、用户导向的文档写作风格。

**适用场景**: 创建或编辑文档文件（markdown、MDX 等）

---

#### [langgraph-docs](./langgraph-docs/) - LangGraph 文档查询

获取 LangGraph Python 文档以提供准确的最新指导。

---

### 开发指南

#### [ai-dev-guidelines](./ai-dev-guidelines/) - AI/ML 开发指南

LangChain、LangGraph 和 ML 模型集成的综合开发指南，涵盖 FastAPI 中的 LLM 应用、Agent、RAG 系统等。

**适用场景**: 构建 LLM 应用、Agent、RAG 系统、情感分析、链编排、提示工程、向量存储

---

#### [architecture-patterns](./architecture-patterns/) - 架构模式

包括整洁架构、六边形架构和领域驱动设计的经过验证的后端架构模式。

**适用场景**: 设计新的后端系统、重构单体应用、建立架构标准、微服务拆分

---

#### [mcp-integration](./mcp-integration/) - MCP 集成指南

将 Model Context Protocol 服务器集成到 Claude Code 插件中的综合指南。

**适用场景**: 添加 MCP 服务器、集成 MCP、配置插件、连接外部服务

---

#### [clojure-review](./clojure-review/) - Clojure 代码审查

审查 Clojure 和 ClojureScript 代码更改，确保符合 Metabase 编码标准。

**适用场景**: 审查包含 Clojure/ClojureScript 代码的 PR 或 diff

---

## 使用方式

### 1. 直接使用脚本

```bash
# 搜索
python web-search/scripts/search.py "AI量化交易"

# 抓取网页
python web-fetch/scripts/fetch.py "https://example.com/article"

# UI/UX 搜索
python3 ui-ux-pro-max/scripts/search.py "minimal" --domain style
```

### 2. 集成到 Claude Code

将 skill 目录复制到你的项目 `.claude/skills/` 下：

```bash
cp -r web-search /path/to/your/project/.claude/skills/
cp -r web-fetch /path/to/your/project/.claude/skills/
cp -r ui-ux-pro-max /path/to/your/project/.claude/skills/
# ... 其他 skills
```

### 3. 作为 Claude Code 技能使用

这些 skills 可以被 Claude Code 识别并自动触发，根据技能描述在适当的场景下激活。

### 4. 作为模块导入

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
2. 创建 [Programmable Search Engine](https://programmablesearchengine.google.com/) 获取 CX ID
3. 设置环境变量：

```bash
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_CX_ID="your_cx_id"
```

或使用 DuckDuckGo（默认，无需配置）。

---

## 许可

MIT License
