# 视觉回归测试指南

本文档面向 pyantv 的测试维护者，介绍项目内的双轨视觉回归测试体系：基于像素差的 **pixel** 路径与基于结构相似性的 **SSIM** 路径。两条轨道并存、互不替代，分别承担不同场景下的回归保护职责。

> 配套阅读：`CONTRIBUTING.md` 的 *Testing → 视觉测试* 段落。本文专注于"基线如何生成、容差如何调整、CI 如何集成"等运维细节。

---

## 1. 双轨共存原理

| 维度 | Pixel 路径 | SSIM 路径（Sprint 66 引入） |
| --- | --- | --- |
| 比较算法 | 逐像素 RGBA 差值 | `skimage.metrics.structural_similarity` |
| 助手模块 | `test/visual_helpers.py` | `test/visual_ssim_helpers.py` |
| 基线目录 | `test/baselines/` | `test/baselines_ssim/` |
| Diff 输出 | `test/diffs/` | `test/diffs/ssim/`（图片右下角水印 `SSIM=0.xxxx`） |
| 适用场景 | 模板 / 样式精确锁死 | 抗锯齿、字体微调、跨平台浮点漂移容忍 |
| 默认阈值 | `max_pixel_diff_ratio <= 1%` | `min_ssim >= 0.95` |
| 是否做 resize | 是 | **否**（依赖固定 viewport 保证尺寸） |

**为什么不全量迁移到 SSIM？** Pixel 路径对模板、CSS 类名等"非渲染像素"差异极敏感，能在第一时间抓住模板回归；SSIM 则对真实视觉差异更鲁棒，二者互补。新增图表测试时按以下原则二选一：

- 强调像素级稳定（如 legend 文案、HTML 模板字段） → 走 pixel
- 强调视觉感官一致（如新增图表、跨平台 CI） → 走 SSIM

---

## 2. 抗锯齿掩码 `edge_mask_kernel_size` 推荐值

SSIM 路径在比较前会做一次抗锯齿掩码膨胀，以容忍边缘 1~2 像素的浮点漂移。`edge_mask_kernel_size` 默认 `3`，推荐配置如下：

| 截图分辨率 | 推荐 kernel | 备注 |
| --- | --- | --- |
| ≤ 400×300 | 1 或 3 | 小图边缘像素占比高，过大 kernel 会掩盖真实差异 |
| 600×450 ~ 1024×768 | **3**（默认） | 项目主基线尺寸 |
| > 1200×900 | 5 或 7 | 大图边缘抖动更明显，可适度放宽 |

如需修改默认值，请在 `test/visual_ssim_helpers.py` 内的 `assert_ssim_visual_match` 调用处覆写，并同步在本表登记理由。

---

## 3. 新增一个 SSIM 视觉基线

> 以新增图表 `MyChart` 为例。

1. **写测试用例**：在 `test/test_visual_ssim.py`（或对应的 `test_visual_*` 文件）中调用 `assert_ssim_visual_match`：

   ```python
   from test.visual_ssim_helpers import assert_ssim_visual_match

   def test_visual_my_chart():
       chart = MyChart().add_xxx(...).render("/tmp/my_chart.html")
       assert_ssim_visual_match(
           html_path="/tmp/my_chart.html",
           baseline_name="my_chart",
           viewport_width=800,
           viewport_height=600,
           min_ssim=0.95,
       )
   ```

2. **生成基线**：首次运行设置环境变量自动写入 `test/baselines_ssim/`：

   ```bash
   UPDATE_VISUAL_BASELINES=1 pytest test/test_visual_ssim.py::test_visual_my_chart -q
   ```

3. **人工验收**：打开 `test/baselines_ssim/my_chart.png` 确认效果符合预期，再 `git add` 提交。

4. **CI 验证**：去掉环境变量重跑一次，确认 SSIM ≥ 0.95（默认阈值）。

> Pixel 路径基线生成方式同理，环境变量同样是 `UPDATE_VISUAL_BASELINES=1`，但写入目录是 `test/baselines/`。

---

## 4. CI 集成约定

- `pyproject.toml` 在 `[dependency-groups].test` 中声明 `scikit-image>=0.19`、`playwright>=1.40`、`pillow>=9.0`，CI 通过 `uv sync --group test` 一键拉齐。
- `test/visual_ssim_helpers.py` 顶部对 `skimage` 做 `pytest.importorskip`，未安装时 SSIM 用例自动 skip，不会让 pixel 路径连坐失败。
- Playwright 浏览器在 CI 内通过 `playwright install --with-deps chromium` 安装；本地首次也需要执行一次。
- `take_screenshot` 调用必须显式传入 `viewport_width / viewport_height / device_scale_factor=1`，避免不同设备 DPR 导致基线尺寸漂移。

---

## 5. 故障排查

| 现象 | 根因排查 | 处理建议 |
| --- | --- | --- |
| `AssertionError: SSIM 0.93 < 0.95` 反复出现 | 抗锯齿差异、字体回退 | 适度增大 `edge_mask_kernel_size` 或更新基线 |
| `ModuleNotFoundError: skimage` | `[dependency-groups].test` 未安装 | `uv sync --group test` 或 `pip install 'pyantv[all]' scikit-image` |
| 截图尺寸与基线不符（pixel 路径硬失败） | viewport / DPR 漂移 | 显式设置 `device_scale_factor=1`，并核对 viewport 参数 |
| Playwright `browser.launch()` 报缺依赖 | 系统 lib 缺失 | `playwright install --with-deps chromium` |
| 基线文件被误改导致 PR 噪音 | 误开 `UPDATE_VISUAL_BASELINES` | 提交前 `git diff -- test/baselines* test/baselines_ssim*` 复核 |

---

## 6. 跨平台稳定性备注

不同平台的字体渲染、抗锯齿算法存在系统性差异（macOS / Linux / Windows）。当前阈值 `min_ssim=0.95` 已留 5% 余量，覆盖大多数常见场景。如某平台出现系统性偏低，请在本节追加平台修正项，并评估是否需要分平台基线（目前不启用，避免基线管理成本爆炸）。

---

如需扩展更多视觉测试策略（如 perceptual hashing、感知颜色差），请新开 Sprint 提案讨论，避免本指南无序膨胀。
