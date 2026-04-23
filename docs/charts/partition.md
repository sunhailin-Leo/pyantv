# Partition

## 概述

分区图 Mark 类。
用于展示层级数据的矩形分区可视化，类似旭日图的矩形版本。
基于 G2 的 partition composite mark 实现，子节点从父节点
的起始位置开始布局，通过宽度比例展示父子关系。
Examples:
>>> from pyantv import Partition
>>> partition = (
...     Partition()
...     .set_data(data=[
...         {"name": "root", "children": [
...             {"name": "A", "value": 10},
...             {"name": "B", "value": 20},
...         ]}
...     ])
...     .set_encode(value_field="value")
...     .set_partition_layout(fill_parent=True)
... )

## 配置项

暂无配置项说明

## 示例

```python
# 示例代码暂未添加
```

## 相关链接

- [API 参考](../api-reference.md)
- [快速开始](../quick-start.md)
