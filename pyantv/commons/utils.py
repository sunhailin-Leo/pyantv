import re

from ..datasets import EXTRA, FILENAMES

# JsCode 占位符标记，用于在 JSON 序列化后定位并还原原始 JS 表达式。
PLACEHOLDER = "--x_x--0_0--"


class JsCode:
    def __init__(self, js_code: str):
        self.js_code = PLACEHOLDER + js_code + PLACEHOLDER

    def __eq__(self, other):
        if isinstance(other, JsCode):
            return self.js_code == other.js_code
        if isinstance(other, str):
            return self.js_code == other
        return NotImplemented

    def __hash__(self):
        return hash(self.js_code)

    def __repr__(self):
        raw = self.js_code.replace(PLACEHOLDER, "")
        return f"JsCode({raw!r})"

    def replace(self, pattern: str, repl: str) -> "JsCode":
        self.js_code = re.sub(pattern, repl, self.js_code)
        return self


class OrderedSet:
    def __init__(self, *args):
        self._values = set()
        self.items = []
        for a in args:
            self.add(a)

    def add(self, *items):
        for item in items:
            if item not in self._values:
                self._values.add(item)
                self.items.append(item)


def produce_require_dict(js_dependencies, js_host) -> dict:
    confs, libraries = [], []
    for name in js_dependencies.items:
        if name in FILENAMES:
            f, _ = FILENAMES[name]
            confs.append("'{}':'{}{}'".format(name, js_host, f))
            libraries.append("'{}'".format(name))
        else:
            for url, files in EXTRA.items():
                if name in files:
                    f, _ = files[name]
                    confs.append("'{}':'{}{}'".format(name, url, f))
                    libraries.append("'{}'".format(name))
                    break
    return dict(config_items=confs, libraries=libraries)


def replace_placeholder(html: str) -> str:
    """移除 JsCode 占位符（含可能包裹的引号）。

    等价于 ``re.sub('"?--x_x--0_0--"?', '', html)``。
    正则中前后 ``"?`` 是独立可选的，共 4 种匹配模式：
    ``"PH"``、``"PH``、``PH"``、``PH``（PH = ``--x_x--0_0--``）。
    用 3 步 str.replace 覆盖全部模式。
    """
    quoted_both = '"' + PLACEHOLDER + '"'
    quoted_left = '"' + PLACEHOLDER
    quoted_right = PLACEHOLDER + '"'
    return (
        html
        .replace(quoted_both, "")
        .replace(quoted_left, "")
        .replace(quoted_right, "")
        .replace(PLACEHOLDER, "")
    )


def replace_placeholder_with_quotes(html: str) -> str:
    """移除 JsCode 占位符（保留引号）。"""
    return html.replace(PLACEHOLDER, "")


def _expand(dict_generator):
    return dict(list(dict_generator))


def _clean_dict(mydict):
    for key, value in mydict.items():
        if value is not None:
            if isinstance(value, dict):
                value = _expand(_clean_dict(value))

            elif isinstance(value, (list, tuple, set)):
                value = list(_clean_array(value))

            # Not elegant, but effective and less code-intrusive.
            elif type(value).__name__ in ["ndarray", "Series"]:
                raise ValueError(
                    "Can't use non-native data structures "
                    "as axis data to render chart"
                )

            elif isinstance(value, str) and not value:
                # delete key with empty string
                continue

            yield key, value


def _clean_array(myarray):
    for value in myarray:
        if isinstance(value, dict):
            yield _expand(_clean_dict(value))

        elif isinstance(value, (list, tuple, set)):
            yield list(_clean_array(value))

        else:
            yield value


def remove_key_with_none_value(incoming_dict):
    """移除字典中值为 None 的键。

    递归清理嵌套字典和列表中的 None 值。

    :param incoming_dict: 输入字典。
    :returns: 清理后的字典，或原样返回非字典值。
    """
    if isinstance(incoming_dict, dict):
        return _expand(_clean_dict(incoming_dict))
    elif incoming_dict:
        return incoming_dict
    else:
        return None


def convert_data_if_needed(data):
    """将 pandas DataFrame/Series 或 numpy ndarray 转换为原生 Python 数据结构。

    支持的输入类型及转换规则：
    - ``pandas.DataFrame`` → ``list[dict]``（等价于 ``df.to_dict("records")``）
    - ``pandas.Series`` → ``list``（等价于 ``series.tolist()``）
    - ``numpy.ndarray`` → ``list``（等价于 ``arr.tolist()``）
    - ``BasicOpts`` 子类（如 ``FetchDataOpts``）→ 原样返回
    - 其他类型（list、dict、None 等）→ 原样返回

    pandas 和 numpy 为可选依赖，未安装时自动跳过检测。

    :param data: 输入数据。
    :returns: 转换后的原生 Python 数据结构，或原样返回。
    """
    from ..options.series_options import BasicOpts

    if data is None or isinstance(data, (list, dict, BasicOpts)):
        return data

    try:
        import pandas as pd

        if isinstance(data, pd.DataFrame):
            return [
                {k: (None if pd.isna(v) else v) for k, v in row.items()}
                for row in data.to_dict("records")
            ]
        if isinstance(data, pd.Series):
            return data.tolist()
    except ImportError:
        pass

    try:
        import numpy as np

        if isinstance(data, np.ndarray):
            return data.tolist()
    except ImportError:
        pass

    return data
