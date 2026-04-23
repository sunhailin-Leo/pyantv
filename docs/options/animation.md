# 动画 Options

动画 Options 控制图表的动画效果。

## AnimateOpts

动画配置，包含入场、更新、退出动画。

**参数：**
- `enter_opts` (AnimatePropertiesOpts): 入场动画
- `update_opts` (AnimatePropertiesOpts): 更新动画
- `exit_opts` (AnimatePropertiesOpts): 退出动画

**示例：**
```python
from pyantv import options as opts

chart.set_animate(animate_opts=opts.AnimateOpts(
    enter_opts=opts.AnimatePropertiesOpts(
        type_="fadeIn",
        duration=1000,
        easing="ease-in-out-cubic"
    )
))
```

---

## AnimatePropertiesOpts

动画属性配置。

**参数：**
- `type_` (str): 动画类型
- `duration` (Numeric): 动画时长（毫秒）
- `delay` (Numeric): 动画延迟（毫秒）
- `easing` (str): 缓动函数

**常用动画类型：**
- `"fadeIn"` - 淡入
- `"fadeOut"` - 淡出
- `"scaleInX"` - X 轴缩放入场
- `"scaleInY"` - Y 轴缩放入场
- `"pathIn"` - 路径入场
- `"waveIn"` - 波浪入场

**常用缓动函数：**
- `"linear"` - 线性
- `"ease"` - 平滑
- `"ease-in"` - 加速
- `"ease-out"` - 减速
- `"ease-in-out"` - 加速后减速
- `"ease-in-out-cubic"` - 三次贝塞尔加速减速

---

## EffectTimingOpts

效果时机配置。

**参数：**
- `delay` (Numeric): 延迟时间
- `duration` (Numeric): 持续时间
- `easing` (str): 缓动函数
- `end_delay` (Numeric): 结束延迟
- `fill` (JSFunc): 填充模式
