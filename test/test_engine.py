import os
import unittest

from pyantv.charts import Interval
from pyantv.render.engine import RenderEngine, write_utf8_html_file
from pyantv.datasets import EXTRA, FILENAMES
from pyantv.globals import CurrentConfig, ChartType


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.test_file_name = "test_file.html"

    def test_generate_js_link(self):
        FILENAMES.update({"existing_dep": ("file_path", "ext")})
        EXTRA.update(
            {
                "https://extra_host.com": {
                    "dep": ("extra_file_path", "extra_ext"),
                },
                "https://extra_host.com/css": {
                    "dep1": ("extra_file_path", "css"),
                },
            }
        )

        # Bar 图
        chart = Interval()
        chart.js_host = None
        chart.js_dependencies.items = [
            "existing_dep",
            "dep",
            "dep1",
        ]

        RenderEngine.generate_js_link(chart)

        assert chart.js_host == CurrentConfig.ONLINE_HOST

        # expected_links = [
        #     "{}file_path.ext".format(CurrentConfig.ONLINE_HOST),
        #     "https://extra_host.comextra_file_path.extra_ext",
        # ]
        # assert chart.dependencies == expected_links
        #
        # expected_css_links = [
        #     "https://extra_host.com/cssextra_file_path.css",
        # ]
        # assert chart.css_libs == expected_css_links

    def test_write_utf8_html_file(self):
        html_content = "<html><body><h1>Hello, World!</h1></body></html>"
        write_utf8_html_file(self.test_file_name, html_content)

        with open(self.test_file_name, "r", encoding="utf-8") as file:
            written_content = file.read()

        self.assertEqual(written_content, html_content)

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)
