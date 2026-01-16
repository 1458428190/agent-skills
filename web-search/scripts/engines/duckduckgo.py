"""
DuckDuckGo 搜索引擎
使用 ddgs 库，完全免费无需 API
"""
from typing import List
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engines import SearchEngine, SearchResult


class DuckDuckGoEngine(SearchEngine):
    """DuckDuckGo 搜索引擎"""

    def search(self, query: str, num_results: int = 10) -> List[SearchResult]:
        """执行搜索"""
        results = []
        max_results = min(num_results, 50)

        try:
            from duckduckgo_search import DDGS

            ddgs = DDGS()

            # 使用 html 后端（更稳定）
            ddg_results = ddgs.text(
                keywords=query,
                max_results=max_results,
                backend="html"
            )

            if ddg_results:
                for item in ddg_results:
                    # 新版本 API 使用 href 而不是 link
                    title = item.get("title", "")
                    url = item.get("href", "") or item.get("link", "")
                    body = item.get("body", "")

                    if title and url:  # 需要标题和 URL
                        results.append(SearchResult(
                            title=title,
                            url=url,
                            snippet=body
                        ))

        except ImportError:
            raise ImportError(
                "请先安装 duckduckgo-search: "
                "pip install duckduckgo-search"
            )
        except Exception as e:
            # 出错时返回空列表
            import logging
            logging.warning(f"DuckDuckGo search error: {e}")
            return []

        return results

    @property
    def name(self) -> str:
        return "duckduckgo"
