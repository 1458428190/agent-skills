#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Search - 联网搜索脚本
支持 DuckDuckGo、Bing、百度、Google 四个搜索引擎

使用方法:
    python search.py "搜索内容"
    python search.py "搜索内容" --engine bing
    python search.py "搜索内容" --num 20
    python search.py "搜索内容" --engine google --num 15
"""
import argparse
import json
import sys
import os
import io

# 修复 Windows 编码问题
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 添加脚本目录到 Python 路径
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from engines import DuckDuckGoEngine, BingEngine, BaiduEngine, GoogleEngine


# 引擎映射
ENGINES = {
    "duckduckgo": DuckDuckGoEngine,
    "bing": BingEngine,
    "baidu": BaiduEngine,
    "google": GoogleEngine,
}


def search(query: str, engine: str = "google", num_results: int = 10) -> dict:
    """
    执行搜索

    Args:
        query: 搜索关键词
        engine: 搜索引擎名称
        num_results: 返回结果数量

    Returns:
        搜索结果字典
    """
    engine_class = ENGINES.get(engine.lower())
    if not engine_class:
        available = ", ".join(ENGINES.keys())
        raise ValueError(f"不支持的搜索引擎: {engine}。可用引擎: {available}")

    search_engine = engine_class()
    results = search_engine.search(query, num_results)

    return {
        "query": query,
        "engine": search_engine.name,
        "count": len(results),
        "results": [r.to_dict() for r in results]
    }


def main():
    parser = argparse.ArgumentParser(
        description="Web Search - 免费联网搜索工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
支持的搜索引擎:
  google       默认引擎
  duckduckgo   完全免费
  bing         微软搜索
  baidu        百度搜索

示例:
  python search.py "AI量化交易"
  python search.py "AI量化交易" --engine bing
  python search.py "AI量化交易" --num 20
  python search.py "AI量化交易" --engine google --num 15
        """
    )

    parser.add_argument(
        "query",
        help="搜索关键词"
    )

    parser.add_argument(
        "-e", "--engine",
        choices=list(ENGINES.keys()),
        default="google",
        help="搜索引擎 (默认: google)"
    )

    parser.add_argument(
        "-n", "--num",
        type=int,
        default=10,
        help="返回结果数量 (默认: 10)"
    )

    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="仅输出 JSON 格式"
    )

    args = parser.parse_args()

    try:
        result = search(args.query, args.engine, args.num)

        # 始终输出 JSON 格式，避免编码问题
        print(json.dumps(result, ensure_ascii=False, indent=2))

    except Exception as e:
        error_result = {
            "error": str(e),
            "query": args.query,
            "engine": args.engine,
            "count": 0,
            "results": []
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
