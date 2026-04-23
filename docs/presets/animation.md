# 动画 Presets

动画 Presets 控制图表的入场动画效果，让图表展示更加生动。

## with_smooth_animation

应用平滑入场动画，使用淡入效果配合自定义缓动函数。

**函数签名：**
```python
def with_smooth_animation(chart, duration=1000, easing="ease-in-out-cubic")
```

**参数：**
- `chart` (Chart): 图表实例
- `duration` (int, 可选): 动画时长，单位毫秒，默认 `1000`
- `easing` (str, 可选): 缓动函数名称，默认 `"ease-in-out-cubic"`

**返回：** 应用动画后的图表实例

**常用缓动函数：**
- `"linear"` - 线性
- `"ease"` - 平滑
- `"ease-in"` - 加速
- `"ease-out"` - 减速
- `"ease-in-out"` - 加速后减速
- `"ease-in-out-cubic"` - 三次贝塞尔加速减速（默认）

**示例：**
```python
from pyantv import Line
from pyantv.presets import with_smooth_animation

chart = Line.from_data(data=data, x_field_name="x", y_field_name="y")

# 使用默认参数（1秒动画，ease-in-out-cubic 缓动）
with_smooth_animation(chart)

# 自定义动画时长为 500 毫秒
with_smooth_animation(chart, duration=500)

# 使用线性缓动
with_smooth_animation(chart, easing="linear")

chart.render("smooth_animation.html")
```

## 动画时长建议

| 场景 | 推荐时长 | 说明 |
|------|---------|------|
| 简单图表 | 500-800ms | 快速展示，减少等待 |
| 复杂图表 | 1000-1500ms | 让用户看清变化过程 |
| 数据大屏 | 1200-2000ms | 增强视觉冲击力 |
| 快速切换 | 300-500ms | 快速响应，避免延迟 |
