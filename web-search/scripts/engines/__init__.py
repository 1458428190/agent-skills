"""
搜索引擎模块初始化
"""
from typing import Protocol, List, Dict, Any
from abc import ABC, abstractmethod


class SearchResult:
    """搜索结果"""
    def __init__(self, title: str, url: str, snippet: str):
        self.title = title
        self.url = url
        self.snippet = snippet

    def to_dict(self) -> Dict[str, str]:
        return {
            "title": self.title,
            "url": self.url,
            "snippet": self.snippet
        }


class SearchEngine(ABC):
    """搜索引擎基类"""

    @abstractmethod
    def search(self, query: str, num_results: int = 10) -> List[SearchResult]:
        """
        执行搜索

        Args:
            query: 搜索关键词
            num_results: 返回结果数量

        Returns:
            搜索结果列表
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """引擎名称"""
        pass


# 导入各个搜索引擎
from .duckduckgo import DuckDuckGoEngine
from .bing import BingEngine
from .baidu import BaiduEngine
from .google import GoogleEngine

__all__ = [
    "SearchEngine",
    "SearchResult",
    "DuckDuckGoEngine",
    "BingEngine",
    "BaiduEngine",
    "GoogleEngine",
]
