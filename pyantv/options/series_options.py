from typing import Any, Optional, Sequence, Tuple, Union

from ..commons.utils import JsCode

Numeric = Union[int, float]
JSFunc = Union[str, JsCode]


class BasicOpts:
    __slots__ = ("opts",)

    def update(self, **kwargs):
        self.opts.update(kwargs)

    def get(self, key: str) -> Any:
        return self.opts.get(key)
