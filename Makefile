# Variables
PACKAGE_NAME = pyantv
PYTHON      ?= python

# Targets
.PHONY: help
help:
	@echo "Please use \`make <target>\` where <target> is one of"
	@echo "  test         -- run local unit tests with coverage"
	@echo "  build        -- build sdist + wheel via PEP 517 (python -m build)"
	@echo "  lint         -- run flake8 for code linting"
	@echo "  format       -- format code with black and isort"
	@echo "  bench        -- run performance benchmarks"
	@echo "  check        -- run lint + test (full quality gate)"
	@echo "  install      -- install the package in editable mode"
	@echo "  install-dev  -- install all dev/test/all extras via pip (fallback)"
	@echo "  uv-install   -- install uv and sync dev + all extras via uv"
	@echo "  uv-lock      -- regenerate uv.lock (commit this file to git)"
	@echo "  publish      -- build + twine upload dist/* (replaces 'setup.py upload')"
	@echo "  docs         -- serve documentation locally (requires mkdocs)"
	@echo "  docs-build   -- build mkdocs site in strict mode (mirrors CI)"
	@echo "  clean        -- clean up temporary files"

.PHONY: test
test:
	@pytest -v --cov-config=.coveragerc --cov=./ test/

.PHONY: build
build:
	@$(PYTHON) -m build

.PHONY: lint
lint:
	@flake8 --exclude=build,example,.venv,examples --max-line-length=89

.PHONY: format
format:
	@black .
	@isort .

.PHONY: bench
bench:
	@$(PYTHON) benchmarks/bench_render.py

.PHONY: check
check: lint test

.PHONY: install
install:
	@pip install -e .

# -----------------------------------------------------------------------------
# 开发依赖安装：推荐走 uv 路径，pip 路径作为 fallback
# -----------------------------------------------------------------------------
.PHONY: install-dev
install-dev:
	@pip install -e '.[dev,test,all]'
	@echo "Development dependencies installed via pip (fallback)."

.PHONY: uv-install
uv-install:
	@pip install uv
	@uv sync --dev --extra all
	@echo "Development dependencies installed via uv."

.PHONY: uv-lock
uv-lock:
	@pip install uv
	@uv lock
	@echo "uv.lock regenerated. Remember to commit it to git for reproducible builds."

# 兼容旧目标 dev → install-dev
.PHONY: dev
dev: install-dev

# -----------------------------------------------------------------------------
# 发布：替代旧的 ``python setup.py upload``（已在 Sprint 62 移除以消除递归）
# -----------------------------------------------------------------------------
.PHONY: publish
publish: clean build
	@$(PYTHON) -m twine upload dist/*

.PHONY: docs
docs:
	@mkdocs serve

# 与 .github/workflows/python-app.yml 中 docs job 行为保持一致：
# strict 模式下任何死链 / 未引用文件 / Markdown 解析告警都会失败
.PHONY: docs-build
docs-build:
	@mkdocs build --strict --site-dir site

.PHONY: clean
clean:
	@rm -rf dist build site $(PACKAGE_NAME).egg-info
	@rm -f .coverage coverage.xml test/.coverage test/coverage.xml
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	@rm -rf test/screenshots test/diffs
	@rm -f render.html
	@echo "Cleaned build artifacts, caches, and test intermediates."

# -----------------------------------------------------------------------------
# 类型存根生成（Sprint 65）
# -----------------------------------------------------------------------------
.PHONY: stubs
stubs:
	@$(PYTHON) scripts/gen_type_stubs.py --write

.PHONY: stubs-check
stubs-check:
	@$(PYTHON) scripts/gen_type_stubs.py --check
