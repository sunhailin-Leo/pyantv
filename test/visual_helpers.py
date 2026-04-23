"""视觉回归测试工具函数。

使用 Playwright 截图 + Pillow 像素对比，验证渲染效果与基准图片一致。

使用方式：
    # 正常测试模式（对比基准图片）
    pytest test/test_visual_regression.py -m slow

    # 更新基准图片
    UPDATE_BASELINES=1 pytest test/test_visual_regression.py -m slow
"""

import os
from pathlib import Path

from PIL import Image

from test.render_helpers import take_screenshot

BASELINES_DIR = Path(__file__).parent / "baselines"
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
DIFFS_DIR = Path(__file__).parent / "diffs"


def _should_update_baselines() -> bool:
    """检查是否处于基准图片更新模式。"""
    return os.environ.get("UPDATE_BASELINES", "").strip() in ("1", "true", "yes")


def _ensure_dirs():
    """确保输出目录存在。"""
    BASELINES_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    DIFFS_DIR.mkdir(parents=True, exist_ok=True)


def _compute_pixel_diff(
    baseline_path: str, screenshot_path: str, diff_path: str
) -> float:
    """计算两张图片的像素差异率。

    Args:
        baseline_path: 基准图片路径
        screenshot_path: 当前截图路径
        diff_path: 差异图片输出路径

    Returns:
        float: 差异率（0.0 ~ 1.0），0.0 表示完全一致
    """
    baseline_img = Image.open(baseline_path).convert("RGBA")
    screenshot_img = Image.open(screenshot_path).convert("RGBA")

    baseline_resized = baseline_img
    screenshot_resized = screenshot_img

    if baseline_img.size != screenshot_img.size:
        target_size = baseline_img.size
        screenshot_resized = screenshot_img.resize(target_size, Image.Resampling.LANCZOS)

    width, height = baseline_resized.size
    total_pixels = width * height
    diff_count = 0

    baseline_pixels = baseline_resized.load()
    screenshot_pixels = screenshot_resized.load()

    diff_img = Image.new("RGBA", (width, height))
    diff_pixels = diff_img.load()

    for x_pos in range(width):
        for y_pos in range(height):
            base_pixel = baseline_pixels[x_pos, y_pos]
            screen_pixel = screenshot_pixels[x_pos, y_pos]

            channel_diff = sum(
                abs(base_channel - screen_channel)
                for base_channel, screen_channel in zip(base_pixel, screen_pixel)
            )

            if channel_diff > 30:
                diff_count += 1
                diff_pixels[x_pos, y_pos] = (255, 0, 0, 200)
            else:
                diff_pixels[x_pos, y_pos] = (
                    base_pixel[0],
                    base_pixel[1],
                    base_pixel[2],
                    80,
                )

    diff_img.save(diff_path)
    return diff_count / total_pixels if total_pixels > 0 else 0.0


def assert_visual_match(
    chart,
    baseline_name: str,
    threshold: float = 0.01,
    viewport_width: int = 800,
    viewport_height: int = 600,
) -> None:
    """对比图表渲染截图与基准图片。

    Args:
        chart: pyantv 图表实例
        baseline_name: 基准图片名称（不含 .png 后缀）
        threshold: 允许的最大差异率（默认 1%）
        viewport_width: 视口宽度
        viewport_height: 视口高度

    Raises:
        AssertionError: 当差异率超过阈值时
        RuntimeError: 当截图失败时
    """
    _ensure_dirs()

    html_content = chart.render_embed()
    screenshot_path = str(SCREENSHOTS_DIR / f"{baseline_name}.png")
    baseline_path = str(BASELINES_DIR / f"{baseline_name}.png")
    diff_path = str(DIFFS_DIR / f"{baseline_name}_diff.png")

    success = take_screenshot(
        html_content,
        screenshot_path,
        viewport_width=viewport_width,
        viewport_height=viewport_height,
    )

    if not success:
        raise RuntimeError(
            f"Failed to take screenshot for '{baseline_name}'. "
            "Canvas element may not have rendered."
        )

    if _should_update_baselines():
        import shutil

        shutil.copy2(screenshot_path, baseline_path)
        return

    if not os.path.exists(baseline_path):
        raise FileNotFoundError(
            f"Baseline image not found: {baseline_path}\n"
            f"Run with UPDATE_BASELINES=1 to generate it."
        )

    diff_rate = _compute_pixel_diff(baseline_path, screenshot_path, diff_path)

    if diff_rate > threshold:
        raise AssertionError(
            f"Visual regression for '{baseline_name}': "
            f"diff rate = {diff_rate:.4f} ({diff_rate * 100:.2f}%), "
            f"threshold = {threshold:.4f} ({threshold * 100:.2f}%)\n"
            f"  Baseline:   {baseline_path}\n"
            f"  Screenshot: {screenshot_path}\n"
            f"  Diff image: {diff_path}\n\n"
            f"Run with UPDATE_BASELINES=1 to update the baseline."
        )
