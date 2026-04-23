# 比例尺 Options

比例尺 Options 控制数据到视觉属性的映射。

## ScaleBaseOpts

比例尺基类，提供通用配置。

**参数：**
- `padding` (Numeric): 内边距
- `is_independent` (bool): 是否独立
- `key` (str): 键
- `range_` (Sequence): 范围
- `is_zero` (bool): 是否从零开始

---

## ScaleBandOpts

分段比例尺，用于离散型数据（如分类轴）。

**参数：**
- `domain` (Sequence): 定义域
- `range_` (Sequence): 值域
- `unknown` (str): 未知值处理
- `padding` (Numeric): 内边距
- `padding_inner` (Numeric): 内部内边距
- `padding_outer` (Numeric): 外部内边距
- `align` (Numeric): 对齐
- `round` (bool): 是否四舍五入
- `compare` (str): 比较方式
- `flex` (Numeric): 弹性

---

## ScaleLinearOpts

线性比例尺，用于连续型数据。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `domain_min` (Numeric): 定义域最小值
- `domain_max` (Numeric): 定义域最大值
- `range_` (Sequence): 值域
- `range_min` (Numeric): 值域最小值
- `range_max` (Numeric): 值域最大值
- `clamp` (bool): 是否限制范围
- `is_nice` (bool): 是否优化刻度
- `is_zero` (bool): 是否从零开始
- `interpolate` (str): 插值方式

---

## ScaleLogOpts

对数比例尺，用于指数型数据。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `domain_min` (Numeric): 定义域最小值
- `domain_max` (Numeric): 定义域最大值
- `range_` (Sequence): 值域
- `range_min` (Numeric): 值域最小值
- `range_max` (Numeric): 值域最大值
- `clamp` (bool): 是否限制范围
- `is_nice` (bool): 是否优化刻度
- `is_zero` (bool): 是否从零开始
- `interpolate` (str): 插值方式
- `base` (Numeric): 对数底数

---

## ScaleOrdinalOpts

序数比例尺，用于离散型数据。

**参数：**
- `domain` (Union[Sequence]): 定义域
- `range_` (Union[Sequence]): 值域
- `unknown` (str): 未知值处理
- `padding` (Numeric): 内边距
- `padding_inner` (Numeric): 内部内边距
- `padding_outer` (Numeric): 外部内边距
- `align` (Numeric): 对齐
- `round` (bool): 是否四舍五入
- `compare` (str): 比较方式

---

## ScalePointOpts

点比例尺，用于离散型数据。

**参数：**
- `domain` (Sequence): 定义域
- `range_` (Sequence): 值域
- `unknown` (str): 未知值处理
- `padding` (Numeric): 内边距
- `padding_inner` (Numeric): 内部内边距
- `padding_outer` (Numeric): 外部内边距
- `align` (Numeric): 对齐
- `round` (bool): 是否四舍五入
- `compare` (str): 比较方式

---

## ScalePowOpts

幂比例尺，用于指数型数据。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `domain_min` (Numeric): 定义域最小值
- `domain_max` (Numeric): 定义域最大值
- `range_` (Sequence): 值域
- `range_min` (Numeric): 值域最小值
- `range_max` (Numeric): 值域最大值
- `clamp` (bool): 是否限制范围
- `is_nice` (bool): 是否优化刻度
- `is_zero` (bool): 是否从零开始
- `interpolate` (str): 插值方式
- `exponent` (Numeric): 指数

---

## ScaleQuantileOpts

分位数比例尺，将数据分为多个等分。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `range_` (Sequence): 值域
- `unknown` (str): 未知值处理
- `padding` (Numeric): 内边距
- `padding_inner` (Numeric): 内部内边距
- `padding_outer` (Numeric): 外部内边距
- `align` (Numeric): 对齐
- `round` (bool): 是否四舍五入
- `compare` (str): 比较方式
- `tick_method` (str): 刻度方法
- `is_nice` (bool): 是否优化刻度

---

## ScaleQuantizeOpts

量化比例尺，将连续数据离散化。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `range_` (Sequence): 值域
- `unknown` (str): 未知值处理
- `padding` (Numeric): 内边距
- `padding_inner` (Numeric): 内部内边距
- `padding_outer` (Numeric): 外部内边距
- `align` (Numeric): 对齐
- `round` (bool): 是否四舍五入
- `compare` (str): 比较方式
- `tick_method` (str): 刻度方法
- `is_nice` (bool): 是否优化刻度

---

## ScaleSqrtOpts

平方根比例尺，用于数据范围较大的情况。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `domain_min` (Numeric): 定义域最小值
- `domain_max` (Numeric): 定义域最大值
- `range_` (Sequence): 值域
- `range_min` (Numeric): 值域最小值
- `range_max` (Numeric): 值域最大值
- `clamp` (bool): 是否限制范围
- `is_nice` (bool): 是否优化刻度
- `is_zero` (bool): 是否从零开始
- `interpolate` (str): 插值方式
- `exponent` (Numeric): 指数（固定为 0.5）

---

## ScaleThresholdOpts

阈值比例尺，根据阈值将数据映射到离散值。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `range_` (Sequence): 值域
- `unknown` (str): 未知值处理

---

## ScaleTimeOpts

时间比例尺，用于时间序列数据。

**参数：**
- `domain` (Sequence[Numeric]): 定义域
- `domain_min` (Numeric): 定义域最小值
- `domain_max` (Numeric): 定义域最大值
- `range_` (Sequence): 值域
- `range_min` (Numeric): 值域最小值
- `range_max` (Numeric): 值域最大值
- `clamp` (bool): 是否限制范围
- `is_nice` (bool): 是否优化刻度
- `is_zero` (bool): 是否从零开始
- `interpolate` (str): 插值方式
- `is_utc` (bool): 是否使用 UTC 时间
