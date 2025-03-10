from ..render import engine

from typing import Any


class ChartMixin:
    def add_js_dependencies(self, *dependencies):
        for dependency in dependencies:
            self.js_dependencies.add(dependency)
        return self

    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def add_js_events(self, *fns):
        for fn in fns:
            self.js_events.add(fn)
        return self

    def load_javascript(self):
        return engine.load_javascript(self)


class JsonRenderMixin:
    def set_json_encoder(self, encoder: Any = None):
        self.json_encoder = encoder

        return self
