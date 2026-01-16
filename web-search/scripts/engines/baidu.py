"""
百度搜索引擎
通过 HTML 解析实现，无需 API Key
"""
import httpx
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import unquote
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import clean_snippet
from engines import SearchEngine, SearchResult


class BaiduEngine(SearchEngine):
    """百度搜索引擎"""

    def __init__(self):
        self.base_url = "https://www.baidu.com/s"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def _clean_url(self, url: str) -> str:
        """清理百度跳转链接"""
        if not url:
            return ""
        # 百度的链接通常是跳转链接，需要提取真实 URL
        if "baidu.com/link" in url or "baidu.com/s?" in url:
            try:
                # 从链接参数中提取真实 URL
                if "url=" in url:
                    start = url.index("url=") + 4
                    end = url.find("&", start)
                    if end == -1:
                        end = len(url)
                    real_url = unquote(url[start:end])
                    return real_url
            except Exception:
                pass
        return url

    def search(self, query: str, num_results: int = 10) -> List[SearchResult]:
        """执行搜索"""
        results = []
        max_results = min(num_results, 50)

        try:
            params = {
                "wd": query,
                "rn": str(max_results),
                "ie": "utf-8"
            }

            response = httpx.get(
                self.base_url,
                params=params,
                headers=self.headers,
                timeout=15.0,
                follow_redirects=True
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "lxml")

            # 百度搜索结果在 .result 类中
            for item in soup.select(".result")[:max_results]:
                try:
                    # 提取标题和链接
                    title_elem = item.select_one("h3 a")
                    if not title_elem:
                        title_elem = item.select_one("a")

                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    raw_url = title_elem.get("href", "")
                    url = self._clean_url(raw_url)

                    # 提取摘要
                    snippet_elem = item.select_one(".c-abstract")
                    if not snippet_elem:
                        snippet_elem = item.select_one(".abstract")
                        if not snippet_elem:
                            snippet_elem = item.select_one("div")

                    snippet = ""
                    if snippet_elem:
                        snippet = clean_snippet(snippet_elem.get_text(strip=True))

                    if title and url:
                        results.append(SearchResult(
                            title=title,
                            url=url,
                            snippet=snippet
                        ))

                except Exception:
                    continue

        except Exception as e:
            return []

        return results

    @property
    def name(self) -> str:
        return "baidu"
