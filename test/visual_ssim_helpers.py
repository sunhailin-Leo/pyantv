"""视觉回归测试工具函数 - SSIM 路径。

使用 Playwright 截图 + scikit-image SSIM 对比，验证渲染效果与基准图片一致。

双轨共存策略：
- pixel 路径：test/visual_helpers.py，使用 test/baselines/ 目录
- SSIM 路径：本文件，使用 test/baselines_ssim/ 目录

使用方式：
    # 正常测试模式（对比基准图片）
    pytest test/test_visual_ssim.py -v

    # 更新基准图片
    UPDATE_BASELINES=1 pytest test/test_visual_ssim.py -v
"""

import os
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw

from test.render_helpers import take_screenshot

# SSIM 路径的独立基线目录
BASELINES_DIR_SSIM = Path(__file__).parent / "baselines_ssim"
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
DIFFS_DIR_SSIM = Path(__file__).parent / "diffs" / "ssim"

# 依赖硬约束（M-SKIMAGE-AVAILABLE）：
# scikit-image 已在 [project.optional-dependencies].test 中声明为 SSIM 路径的硬依赖，
# 故此处**直接 import**，不做 try/except 兜底。若 import 失败应让调用方拿到
# 明确的 ImportError，指示 `pip install -e '.[test]'` 未正确安装 scikit-image，
# 而非静默降级或 skip，避免 CI 绿灯误报。
from skimage.feature import canny  # noqa: E402
from skimage.morphology import dilation  # noqa: E402
from skimage.metrics import structural_similarity as ssim  # noqa: E402


def _should_update_baselines() -> bool:
    """检查是否处于基准图片更新模式。

    Returns:
        bool: 是否处于更新模式
    """
    return os.environ.get("UPDATE_BASELINES", "").strip() in ("1", "true", "yes")


def _ensure_dirs():
    """确保输出目录存在。"""
    BASELINES_DIR_SSIM.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    DIFFS_DIR_SSIM.mkdir(parents=True, exist_ok=True)


def _compute_edge_mask(
    image_array,
    kernel_size: int = 3,
):
    """计算图像边缘掩码，用于忽略抗锯齿边缘的微小差异。

    Args:
        image_array: 图像数组（灰度）
        kernel_size: 膨胀核大小，默认 3

    Returns:
        边缘掩码数组（0 表示边缘区域，1 表示非边缘区域）
    """
    # scikit-image 已在模块顶层硬 import，此处无需再做可用性判断

    # 使用 Canny 边缘检测
    edges = canny(image_array)

    # 使用形态学膨胀扩大边缘区域
    from skimage.morphology import disk

    selem = disk(kernel_size)
    mask = dilation(edges, selem)

    # 反转掩码：边缘区域为 0，非边缘区域为 1
    mask = ~mask

    return mask


def _compute_ssim_diff(
    baseline_path: str,
    screenshot_path: str,
    diff_path: str,
    min_ssim: float = 0.95,
    edge_mask_kernel_size: int = 3,
) -> Tuple[float, Image.Image]:
    """计算两张图片的 SSIM 差异。

    Args:
        baseline_path: 基准图片路径
        screenshot_path: 当前截图路径
        diff_path: 差异图片输出路径
        min_ssim: 最小 SSIM 阈值（0.0 ~ 1.0）
        edge_mask_kernel_size: 抗锯齿边缘掩码的核大小

    Returns:
        Tuple[float, PIL.Image.Image]: (SSIM 分数, 差异图片)

    Raises:
        ValueError: min_ssim 超出 [0, 1] 范围
        AssertionError: 图片尺寸不匹配（SSIM 路径禁止 resize）
    """
    # scikit-image 已在模块顶层硬 import，此处无需再做可用性判断

    if not 0.0 <= min_ssim <= 1.0:
        raise ValueError(f"min_ssim must be in [0.0, 1.0], got {min_ssim}")

    baseline_img = Image.open(baseline_path).convert("RGB")
    screenshot_img = Image.open(screenshot_path).convert("RGB")

    # SSIM 路径禁止 resize，尺寸必须一致
    if baseline_img.size != screenshot_img.size:
        raise AssertionError(
            f"Baseline shape {baseline_img.size} != "
            f"screenshot shape {screenshot_img.size}. "
            "SSIM comparison requires images to have "
            "the same size. Ensure viewport_width and "
            "viewport_height are consistent."
        )

    # 转换为 numpy 数组
    import numpy as np

    baseline_array = np.array(baseline_img)
    screenshot_array = np.array(screenshot_img)

    # 计算 SSIM
    ssim_score = ssim(
        baseline_array,
        screenshot_array,
        multichannel=True,
        channel_axis=2,
        data_range=255,
    )

    # 创建差异图片
    diff_img = Image.new("RGB", baseline_img.size, (255, 255, 255))
    draw = ImageDraw.Draw(diff_img)

    # 计算像素差异并绘制
    width, height = baseline_img.size
    for y in range(height):
        for x in range(width):
            base_pixel = baseline_img.getpixel((x, y))
            screen_pixel = screenshot_img.getpixel((x, y))

            # 计算像素差异
            pixel_diff = sum(abs(b - s) for b, s in zip(base_pixel, screen_pixel))

            # 差异较大时用红色标记
            if pixel_diff > 30:
                draw.point((x, y), fill=(255, 0, 0))
            else:
                # 使用基准图片的像素
                draw.point((x, y), fill=base_pixel)

    # 在右下角添加 SSIM 分数水印
    text = f"SSIM={ssim_score:.4f}"
    text_position = (width - 120, height - 30)
    draw.text(text_position, text, fill=(255, 0, 0))

    diff_img.save(diff_path)

    return ssim_score, diff_img


def assert_visual_match_ssim(
    chart,
    baseline_name: str,
    min_ssim: float = 0.95,
    viewport_width: int = 800,
    viewport_height: int = 600,
    edge_mask_kernel_size: int = 3,
) -> None:
    """对比图表渲染截图与基准图片（SSIM 路径）。

    Args:
        chart: pyantv 图表实例
        baseline_name: 基准图片名称（不含 .png 后缀）
        min_ssim: 最小 SSIM 阈值（0.0 ~ 1.0），默认 0.95
        viewport_width: 视口宽度
        viewport_height: 视口高度
        edge_mask_kernel_size: 抗锯齿边缘掩码的核大小

    Raises:
        ValueError: min_ssim 超出 [0, 1] 范围
        AssertionError: SSIM 分数低于阈值或图片尺寸不匹配
        RuntimeError: 当截图失败时
    """
    _ensure_dirs()

    html_content = chart.render_embed()
    screenshot_path = str(SCREENSHOTS_DIR / f"{baseline_name}.png")
    baseline_path = str(BASELINES_DIR_SSIM / f"{baseline_name}.png")
    diff_path = str(DIFFS_DIR_SSIM / f"{baseline_name}_diff.png")

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

    ssim_score, _ = _compute_ssim_diff(
        baseline_path,
        screenshot_path,
        diff_path,
        min_ssim=min_ssim,
        edge_mask_kernel_size=edge_mask_kernel_size,
    )

    if ssim_score < min_ssim:
        raise AssertionError(
            f"Visual regression for '{baseline_name}': "
            f"SSIM = {ssim_score:.4f}, "
            f"threshold = {min_ssim:.4f}\n"
            f"  Baseline:   {baseline_path}\n"
            f"  Screenshot: {screenshot_path}\n"
            f"  Diff image: {diff_path}\n\n"
            f"Run with UPDATE_BASELINES=1 to update the baseline."
        )
