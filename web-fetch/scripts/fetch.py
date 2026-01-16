#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Fetch - 网页内容抓取脚本
使用 trafilatura 提取网页正文内容

使用方法:
    python fetch.py "https://example.com"
    python fetch.py "https://example.com" --format text
    python fetch.py "https://example.com" --include-links
"""
import argparse
import json
import sys
import io

# 修复 Windows 编码问题
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def fetch(url: str, output_format: str = "markdown", include_links: bool = False,
          include_images: bool = False) -> dict:
    """
    抓取网页内容

    Args:
        url: 网页 URL
        output_format: 输出格式 (markdown, text, html)
        include_links: 是否保留链接
        include_images: 是否保留图片

    Returns:
        抓取结果字典
    """
    try:
        import trafilatura
    except ImportError:
        return {
            "error": "缺少依赖 trafilatura，请运行: pip install trafilatura",
            "url": url,
            "content": ""
        }

    # 下载网页
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return {
            "error": "无法下载网页，请检查 URL 是否正确",
            "url": url,
            "content": ""
        }

    # 提取内容
    try:
        # trafilatura 内部使用 xmljson 参数控制输出格式
        # json=True 返回字典，False 返回文本
        # 我们需要用 extract 函数的参数来控制
        output_format_map = {
            "markdown": "xml",  # 默认输出格式，可转换
            "text": "txt",
            "html": "html",
        }
        fmt = output_format_map.get(output_format, "xml")

        # 使用 extract 函数提取内容
        # 参考文档: https://trafilatura.readthedocs.io/
        content = trafilatura.extract(
            downloaded,
            output_format=fmt,
            include_links=include_links,
            include_images=include_images,
            include_tables=True,
        )

        # 获取元数据
        metadata = trafilatura.metadata.extract_metadata(downloaded)
        title = metadata.title if metadata else ""

        # 如果是 markdown 格式，需要简单转换
        # trafilatura 默认输出的是 XML 格式，我们用 text 格式更简单
        if output_format == "markdown":
            # 使用 txt 格式，然后用简单规则转换
            content = trafilatura.extract(
                downloaded,
                output_format="txt",
                include_links=include_links,
                include_images=include_images,
                include_tables=True,
            )
        elif output_format == "text":
            content = trafilatura.extract(
                downloaded,
                output_format="txt",
                include_links=False,
                include_images=False,
                include_tables=True,
            )
        elif output_format == "html":
            content = trafilatura.extract(
                downloaded,
                output_format="html",
                include_links=include_links,
                include_images=include_images,
                include_tables=True,
            )

        return {
            "url": url,
            "title": title or "",
            "content": content or "",
            "format": output_format,
            "length": len(content) if content else 0
        }

    except Exception as e:
        return {
            "error": str(e),
            "url": url,
            "content": ""
        }


def main():
    parser = argparse.ArgumentParser(
        description="Web Fetch - 网页内容抓取工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
输出格式:
  markdown   Markdown 格式（默认，推荐）
  text       纯文本格式
  html       HTML 格式

示例:
  python fetch.py "https://www.example.com"
  python fetch.py "https://www.example.com" --format text
  python fetch.py "https://www.example.com" --include-links --include-images
        """
    )

    parser.add_argument(
        "url",
        help="网页 URL"
    )

    parser.add_argument(
        "-f", "--format",
        choices=["markdown", "text", "html"],
        default="markdown",
        help="输出格式 (默认: markdown)"
    )

    parser.add_argument(
        "-l", "--include-links",
        action="store_true",
        help="保留链接"
    )

    parser.add_argument(
        "-i", "--include-images",
        action="store_true",
        help="保留图片"
    )

    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="仅输出 JSON 格式（目前默认就是 JSON）"
    )

    args = parser.parse_args()

    result = fetch(args.url, args.format, args.include_links, args.include_images)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
