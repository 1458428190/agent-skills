"""
工具函数
"""
import re
from typing import Optional
from bs4 import BeautifulSoup


def clean_html(html: str) -> str:
    """清理 HTML 标签，提取纯文本"""
    if not html:
        return ""
    soup = BeautifulSoup(html, "lxml")
    # 移除 script 和 style 标签
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    # 清理多余空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def clean_snippet(snippet: str) -> str:
    """清理搜索结果摘要"""
    if not snippet:
        return ""
    # 移除多余的空白字符
    snippet = re.sub(r'\s+', ' ', snippet)
    # 移除常见的无关字符
    snippet = snippet.replace('...', '')
    snippet = snippet.replace('…', '')
    return snippet.strip()


def truncate_text(text: str, max_length: int = 200) -> str:
    """截断文本到指定长度"""
    if not text:
        return ""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + '...'


def extract_domain(url: str) -> Optional[str]:
    """从 URL 中提取域名"""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return None
