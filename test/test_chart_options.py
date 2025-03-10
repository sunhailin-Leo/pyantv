import unittest

from pyantv.options.chart_options import (
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
    CustomDataOpts,
    FetchDataOpts,
    InlineDataOpts,
    JSFunc,
)


class TestChartOptions(unittest.TestCase):

    def test_ema_data_transform_opts(self):
        obj = EMADataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "ema",
                "field": None,
                "alpha": None,
                "as": None,
            },
        )

    def test_filter_data_transform_opts(self):
        obj = FilterDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "filter",
                "callback": None,
            },
        )

    def test_fold_data_transform_opts(self):
        obj = FoldDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "fold",
                "fields": None,
                "key": None,
                "value": None,
            },
        )

    def test_join_data_transform_opts(self):
        obj = JoinDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "join",
                "join": None,
                "on": None,
                "select": None,
            },
        )

    def test_kde_data_transform_opts(self):
        obj = KdeDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "kde",
                "join": None,
                "field": None,
                "groupBy": None,
                "as": None,
                "size": None,
            },
        )

    def test_log_data_transform_opts(self):
        obj = LogDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "log",
            },
        )

    def test_map_data_transform_opts(self):
        obj = MapDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "map",
                "callback": None,
            },
        )

    def test_pick_data_transform_opts(self):
        obj = PickDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "pick",
                "fields": None,
            },
        )

    def test_rename_data_transform_opts(self):
        obj = RenameDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "rename",
            },
        )
        obj = RenameDataTransformOpts(rename_map={"old_name": "new_name"})
        self.assertEqual(
            obj.opts,
            {
                "type": "rename",
                "old_name": "new_name",
            },
        )

    def test_slice_data_transform_opts(self):
        obj = SliceDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "slice",
                "start": None,
                "end": None,
            },
        )

    def test_sort_data_transform_opts(self):
        obj = SortDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sort",
                "callback": None,
            },
        )

    def test_sort_by_data_transform_opts(self):
        obj = SortByDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "sortBy",
                "fields": None,
            },
        )

    def test_custom_data_transform_opts(self):
        obj = CustomDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "custom",
                "callback": None,
            },
        )

    def test_feature_data_transform_opts(self):
        obj = FeatureDataTransformOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "feature",
                "name": None,
            },
        )

    def test_custom_data_opts(self):
        obj = CustomDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "custom",
                "callback": None,
            },
        )

    def test_fetch_data_opts(self):
        obj = FetchDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "fetch",
                "value": None,
                "format": None,
                "delimiter": None,
                "autoType": None,
                "transform": None,
            },
        )

    def test_inline_data_opts(self):
        obj = InlineDataOpts()
        self.assertEqual(
            obj.opts,
            {
                "type": "inline",
                "value": None,
                "transform": None,
            },
        )
