from .series_options import (
    BasicOpts,
    Numeric,
    Optional,
    Sequence,
    Union,
    JSFunc,
)


class EMADataTransformOpts(BasicOpts):
    def __init__(
        self,
        field: Optional[str] = None,
        alpha: Optional[Numeric] = None,
        as_: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "ema",
            "field": field,
            "alpha": alpha,
            "as": as_,
        }


class FilterDataTransformOpts(BasicOpts):
    def __init__(
        self,
        callback: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "filter",
            "callback": callback,
        }


class FoldDataTransformOpts(BasicOpts):
    def __init__(
        self,
        fields: Optional[Sequence[str]] = None,
        key: Optional[str] = None,
        value: Optional[str] = None,
    ):
        self.opts: dict = {
            "type": "fold",
            "fields": fields,
            "key": key,
            "value": value,
        }


class JoinDataTransformOpts(BasicOpts):
    def __init__(
        self,
        join: Optional[Sequence[dict]] = None,
        on_: Optional[Sequence[str]] = None,
        select_: Optional[Sequence[str]] = None,
    ):
        self.opts: dict = {
            "type": "join",
            "join": join,
            "on": on_,
            "select": select_,
        }


class KdeDataTransformOpts(BasicOpts):
    def __init__(
        self,
        join: Optional[Sequence[dict]] = None,
        field: Optional[str] = None,
        group_by: Optional[Sequence[str]] = None,
        as_: Optional[Sequence[str]] = None,
        size: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "kde",
            "join": join,
            "field": field,
            "groupBy": group_by,
            "as": as_,
            "size": size,
        }


class LogDataTransformOpts(BasicOpts):
    def __init__(self):
        self.opts: dict = {"type": "log"}


class MapDataTransformOpts(BasicOpts):
    def __init__(
        self,
        callback: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "map",
            "callback": callback,
        }


class PickDataTransformOpts(BasicOpts):
    def __init__(
        self,
        fields: Optional[Sequence[str]] = None,
    ):
        self.opts: dict = {
            "type": "pick",
            "fields": fields,
        }


class RenameDataTransformOpts(BasicOpts):
    def __init__(
        self,
        rename_map: Optional[dict] = None,
    ):
        self.opts: dict = {
            "type": "rename",
        }
        if rename_map:
            self.opts.update(rename_map)


class SliceDataTransformOpts(BasicOpts):
    def __init__(
        self,
        start: Optional[Numeric] = None,
        end: Optional[Numeric] = None,
    ):
        self.opts: dict = {
            "type": "slice",
            "start": start,
            "end": end,
        }


class SortDataTransformOpts(BasicOpts):
    def __init__(
        self,
        callback: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "sort",
            "callback": callback,
        }


class SortByDataTransformOpts(BasicOpts):
    def __init__(
        self,
        fields: Optional[Sequence[str]] = None,
    ):
        self.opts: dict = {
            "type": "sortBy",
            "fields": fields,
        }


class CustomDataTransformOpts(BasicOpts):
    def __init__(
        self,
        callback: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "custom",
            "callback": callback,
        }


class FeatureDataTransformOpts(BasicOpts):
    def __init__(
        self,
        name: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "feature",
            "name": name,
        }


# types
TransformOpts = Union[
    EMADataTransformOpts,
    FilterDataTransformOpts,
    FoldDataTransformOpts,
    JoinDataTransformOpts,
    KdeDataTransformOpts,
    LogDataTransformOpts,
    MapDataTransformOpts,
    PickDataTransformOpts,
    RenameDataTransformOpts,
    SliceDataTransformOpts,
    SortDataTransformOpts,
    SortByDataTransformOpts,
    CustomDataTransformOpts,
    FeatureDataTransformOpts,
]


class CustomDataOpts(BasicOpts):
    def __init__(
        self,
        callback: Optional[JSFunc] = None,
    ):
        self.opts: dict = {
            "type": "custom",
            "callback": callback,
        }


class FetchDataOpts(BasicOpts):
    def __init__(
        self,
        value: Optional[str] = None,
        format_: Optional[str] = None,
        delimiter: Optional[str] = None,
        is_auto_type: Optional[bool] = None,
        transform: Optional[Sequence[TransformOpts]] = None,
    ):
        self.opts: dict = {
            "type": "fetch",
            "value": value,
            "format": format_,
            "delimiter": delimiter,
            "autoType": is_auto_type,
            "transform": transform,
        }


class InlineDataOpts(BasicOpts):
    def __init__(
        self,
        value: Optional[Sequence[dict]] = None,
        transform: Optional[Sequence[TransformOpts]] = None,
    ):
        self.opts: dict = {
            "type": "inline",
            "value": value,
            "transform": transform,
        }
