"""
Bing 搜索引擎
通过 HTML 解析实现，无需 API Key
"""
import httpx
from bs4 import BeautifulSoup
from typing import List
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import clean_snippet
from engines import SearchEngine, SearchResult


class BingEngine(SearchEngine):
    """Bing 搜索引擎"""

    def __init__(self):
        self.base_url = "https://www.bing.com/search"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def search(self, query: str, num_results: int = 10) -> List[SearchResult]:
        """执行搜索"""
        results = []
        max_results = min(num_results, 50)

        try:
            params = {
                "q": query,
                "count": str(max_results),
                "setlang": "en"
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

            # Bing 搜索结果在 .b_algo 类中
            for item in soup.select(".b_algo")[:max_results]:
                try:
                    # 提取标题和链接
                    title_elem = item.select_one("h2 a")
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    url = title_elem.get("href", "")

                    # 提取摘要
                    snippet_elem = item.select_one(".b_caption p")
                    if not snippet_elem:
                        snippet_elem = item.select_one("p")
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
        return "bing"
