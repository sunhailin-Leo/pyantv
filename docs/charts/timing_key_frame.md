# TimingKeyFrame

## 概述

时间关键帧（TimingKeyFrame）组合图表。

基于 G2 的 `timingKeyframe` 复合视图，按顺序播放多个子图表
作为关键帧，实现「图表之间」的过渡动画，常用于数据故事讲述、
状态对比演示等场景。

## 配置项

- **set_timing_key_frame_children(children)**: 设置关键帧序列，按数组顺序播放每个 `Chart` 序列化结果

## 示例

```python
from pyantv import TimingKeyFrame, Interval

frame_1 = (
    Interval()
    .set_data(data=[{"x": "A", "y": 30}, {"x": "B", "y": 50}])
    .set_encode(x_field_name="x", y_field_name="y")
)
frame_2 = (
    Interval()
    .set_data(data=[{"x": "A", "y": 80}, {"x": "B", "y": 60}])
    .set_encode(x_field_name="x", y_field_name="y")
)

animation = (
    TimingKeyFrame()
    .set_timing_key_frame_children(
        children=[frame_1.get_options(), frame_2.get_options()]
    )
)
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)
