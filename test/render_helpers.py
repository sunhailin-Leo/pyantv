"""HTML 渲染 + DOM 结构验证工具函数。

使用 Playwright 打开 pyantv 渲染的 HTML，验证 G2 图表是否正确渲染。

依赖：
    pip install playwright
    playwright install chromium
"""

import asyncio
from dataclasses import dataclass, field
from typing import List, Optional

from playwright.async_api import async_playwright


@dataclass
class RenderResult:
    """渲染验证结果。"""

    canvas_exists: bool = False
    canvas_width: int = 0
    canvas_height: int = 0
    console_errors: List[str] = field(default_factory=list)
    console_warnings: List[str] = field(default_factory=list)
    js_exceptions: List[str] = field(default_factory=list)
    chart_instance_exists: bool = False
    container_exists: bool = False
    page_title: str = ""


async def _validate_render_async(
    html_content: str,
    wait_timeout_ms: int = 10000,
    chart_id: Optional[str] = None,
) -> RenderResult:
    """异步验证 HTML 渲染结果。"""
    result = RenderResult()

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()

        page.on(
            "console",
            lambda msg: (
                result.console_errors.append(msg.text)
                if msg.type == "error"
                else (
                    result.console_warnings.append(msg.text)
                    if msg.type == "warning"
                    else None
                )
            ),
        )

        page.on("pageerror", lambda exc: result.js_exceptions.append(str(exc)))

        await page.set_content(html_content, wait_until="networkidle")

        try:
            await page.wait_for_selector("canvas", timeout=wait_timeout_ms)
        except Exception:
            await browser.close()
            return result

        result.page_title = await page.title()

        canvas_info = await page.evaluate(
            """() => {
            const canvas = document.querySelector('canvas');
            return canvas ? {
                exists: true,
                width: canvas.width,
                height: canvas.height,
            } : { exists: false, width: 0, height: 0 };
        }"""
        )
        result.canvas_exists = canvas_info["exists"]
        result.canvas_width = canvas_info["width"]
        result.canvas_height = canvas_info["height"]

        if chart_id:
            result.container_exists = await page.evaluate(
                f"!!document.getElementById('{chart_id}')"
            )

        result.chart_instance_exists = await page.evaluate(
            """() => {
            const scripts = document.querySelectorAll('script');
            for (const s of scripts) {
                if (s.textContent.includes('new G2.Chart')) return true;
            }
            return false;
        }"""
        )

        await browser.close()

    return result


def validate_render(
    html_content: str,
    wait_timeout_ms: int = 10000,
    chart_id: Optional[str] = None,
) -> RenderResult:
    """同步验证 HTML 渲染结果。

    Args:
        html_content: 完整的 HTML 字符串（来自 chart.render_embed()）
        wait_timeout_ms: 等待 canvas 出现的超时时间（毫秒）
        chart_id: 图表容器的 DOM ID

    Returns:
        RenderResult: 渲染验证结果
    """
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(
            _validate_render_async(html_content, wait_timeout_ms, chart_id)
        )
    finally:
        loop.close()


async def _take_screenshot_async(
    html_content: str,
    output_path: str,
    viewport_width: int = 800,
    viewport_height: int = 600,
    wait_timeout_ms: int = 10000,
) -> bool:
    """异步截图。"""
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={"width": viewport_width, "height": viewport_height}
        )

        await page.set_content(html_content, wait_until="networkidle")

        try:
            await page.wait_for_selector("canvas", timeout=wait_timeout_ms)
            await page.wait_for_timeout(500)
        except Exception:
            await browser.close()
            return False

        await page.screenshot(path=output_path, full_page=False)
        await browser.close()
        return True


def take_screenshot(
    html_content: str,
    output_path: str,
    viewport_width: int = 800,
    viewport_height: int = 600,
    wait_timeout_ms: int = 10000,
) -> bool:
    """对渲染的 HTML 截图。

    Args:
        html_content: 完整的 HTML 字符串
        output_path: 截图保存路径
        viewport_width: 视口宽度
        viewport_height: 视口高度
        wait_timeout_ms: 等待 canvas 出现的超时时间

    Returns:
        bool: 截图是否成功
    """
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(
            _take_screenshot_async(
                html_content,
                output_path,
                viewport_width,
                viewport_height,
                wait_timeout_ms,
            )
        )
    finally:
        loop.close()
