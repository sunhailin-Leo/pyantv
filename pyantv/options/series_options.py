from typing import Any, Optional, Sequence, Tuple, Union

from ..commons.utils import JsCode

Numeric = Union[int, float]
JSFunc = Union[str, JsCode]

__all__ = [
    "Any",
    "Optional",
    "Sequence",
    "Tuple",
    "Union",
    "JsCode",
    "Numeric",
    "JSFunc",
    "BasicOpts",
]


class BasicOpts:
    __slots__ = ("opts",)

    def update(self, **kwargs):
        self.opts.update(kwargs)

    def get(self, key: str) -> Any:
        return self.opts.get(key)
