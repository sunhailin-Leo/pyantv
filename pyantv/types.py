from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from . import options as opts
from .options.series_options import JsCode, JSFunc, Numeric

# custom types
NumericAndJsFunc = Optional[Union[Numeric, JSFunc]]

# opts types
Init = Union[opts.InitOpts, dict]
RenderInit = Union[opts.RenderOpts, dict]
BaseChartStyle = Union[opts.BaseChartStyleOpts, dict]
BaseChartRadiusInsetStyle = Union[opts.BaseChartRadiusInsetStyleOpts, dict]
Data = Union[
    opts.CustomDataOpts,
    opts.FetchDataOpts,
    opts.InlineDataOpts,
    dict,
]
DataTransform = Union[
    opts.EMADataTransformOpts,
    opts.FilterDataTransformOpts,
    opts.FoldDataTransformOpts,
    opts.JoinDataTransformOpts,
    opts.KdeDataTransformOpts,
    opts.LogDataTransformOpts,
    opts.MapDataTransformOpts,
    opts.PickDataTransformOpts,
    opts.RenameDataTransformOpts,
    opts.SliceDataTransformOpts,
    opts.SortDataTransformOpts,
    opts.SortByDataTransformOpts,
    dict,
]
Scale = Union[
    opts.ScaleBaseOpts,
    opts.ScaleBandOpts,
    opts.ScaleLinearOpts,
    opts.ScaleLogOpts,
    opts.ScaleOrdinalOpts,
    opts.ScalePointOpts,
    opts.ScalePowOpts,
    opts.ScaleQuantileOpts,
    opts.ScaleQuantizeOpts,
    opts.ScaleSqrtOpts,
    opts.ScaleThresholdOpts,
    opts.ScaleTimeOpts,
    dict,
    bool,
]

Transform = Union[
    opts.TransformBinOpts,
    opts.TransformBinXOpts,
    opts.TransformDiffXOpts,
    opts.TransformDodgeXOpts,
    opts.TransformFlexXOpts,
    opts.TransformGroupOpts,
    opts.TransformGroupColorOpts,
    opts.TransformGroupXOpts,
    opts.TransformGroupYOpts,
    opts.TransformJitterOpts,
    opts.TransformJitterXOpts,
    opts.TransformJitterYOpts,
    opts.TransformNormalizeYOpts,
    opts.TransformPackOpts,
    opts.TransformSampleOpts,
    opts.TransformSelectOpts,
    opts.TransformSelectXOpts,
    opts.TransformSelectYOpts,
    opts.TransformSortColorOpts,
    opts.TransformSortXOpts,
    opts.TransformSortYOpts,
    opts.TransformStackEnterOpts,
    opts.TransformStackYOpts,
    opts.TransformSymmetryYOpts,
    dict,
]

Coordinate = Union[
    opts.CoordinateFishEyeOpts,
    opts.CoordinateParallelOpts,
    opts.CoordinatePolarOpts,
    opts.CoordinateRadialOpts,
    opts.CoordinateThetaOpts,
    opts.CoordinateTransposeOpts,
    opts.CoordinateCartesian3DOpts,
    dict,
]

Animate = Union[opts.AnimateOpts, dict, bool]
Title = Union[opts.TitleOpts, dict, bool]
Axis = Union[opts.AxisOpts, dict, bool]
State = Union[opts.StateOpts, dict, bool]
ScrollBar = Union[opts.ScrollBarOpts, dict, bool]
Slider = Union[opts.SliderOpts, dict, bool]
Legend = Union[opts.LegendCategoryOpts, opts.LegendContinuousOpts, dict, bool]
Tooltip = Union[opts.TooltipOpts, dict, bool]
Label = Union[Sequence[opts.LabelOpts], opts.LabelOpts, dict, bool]
Interaction = Union[opts.InteractionOpts, dict, bool]
