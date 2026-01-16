"""
Google Custom Search API 搜索引擎
使用 Google Custom Search JSON API，需要 API Key 和 CX ID
"""
import httpx
from typing import List
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engines import SearchEngine, SearchResult


class GoogleEngine(SearchEngine):
    """Google Custom Search API 搜索引擎"""

    def __init__(self, api_key: str = None, cx: str = None):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.cx = cx or os.getenv("GOOGLE_CX_ID")

        # 请设置环境变量或传入参数，不要硬编码 API Key
        if not self.api_key or not self.cx:
            raise ValueError(
                "Google 搜索引擎需要 API Key 和 CX ID。\n"
                "请设置环境变量 GOOGLE_API_KEY 和 GOOGLE_CX_ID，\n"
                "或在 https://console.cloud.google.com/ 获取 API Key，\n"
                "在 https://programmablesearchengine.google.com/ 创建搜索引擎获取 CX ID。"
            )

        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query: str, num_results: int = 10) -> List[SearchResult]:
        """执行搜索"""
        results = []
        # Google API 每次最多返回 10 条，需要多次请求
        max_results = min(num_results, 100)

        try:
            # 计算需要请求的次数（每次最多10条）
            num_requests = (max_results + 9) // 10

            for i in range(num_requests):
                start_index = i * 10 + 1
                remaining = max_results - i * 10
                per_page = min(10, remaining)

                params = {
                    "key": self.api_key,
                    "cx": self.cx,
                    "q": query,
                    "num": per_page,
                    "start": start_index
                }

                response = httpx.get(
                    self.base_url,
                    params=params,
                    timeout=15.0
                )
                response.raise_for_status()

                data = response.json()

                # 解析结果
                if "items" in data:
                    for item in data["items"]:
                        title = item.get("title", "")
                        url = item.get("link", "")
                        snippet = item.get("snippet", "")

                        if title and url:
                            results.append(SearchResult(
                                title=title,
                                url=url,
                                snippet=snippet
                            ))

                # 检查是否还有更多结果
                if "queries" not in data or "nextPage" not in data["queries"]:
                    break

        except Exception as e:
            import logging
            logging.warning(f"Google API search error: {e}")
            return []

        return results

    @property
    def name(self) -> str:
        return "google"
