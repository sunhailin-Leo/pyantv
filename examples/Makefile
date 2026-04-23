.PHONY: generate serve clean open help

PORT ?= 8080
PROJECT_ROOT := $(shell cd .. && pwd)

help: ## 显示帮助信息
	@echo "🐍 pyantv 示例画廊工具"
	@echo ""
	@echo "用法: make <命令>"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "示例:"
	@echo "  make generate        # 生成画廊"
	@echo "  make serve           # 启动服务器（默认端口 8080）"
	@echo "  make serve PORT=3000 # 指定端口 3000"
	@echo "  make clean           # 清理文件"

generate: ## 重新生成画廊（运行所有示例 + 生成 index.html）
	@echo "🚀 开始生成画廊..."
	cd $(PROJECT_ROOT) && python3 examples/generate_gallery.py
	@echo ""
	@echo "💡 提示: 运行 'make serve' 启动服务器浏览"

serve: ## 启动本地 HTTP 服务器浏览画廊（可通过 PORT=xxx 指定端口）
	@if [ ! -f index.html ]; then \
		echo "⚠️  画廊页面尚未生成，先执行生成..."; \
		$(MAKE) generate; \
	fi
	@echo "🌐 启动本地服务器..."
	@echo "   地址: http://localhost:$(PORT)"
	@echo "   按 Ctrl+C 停止"
	@echo ""
	python3 -m http.server $(PORT)

clean: ## 清理生成的 HTML 文件（_output/ 和 index.html）
	@echo "🧹 清理生成的文件..."
	@if [ -d _output ]; then \
		rm -rf _output; \
		echo "   ✅ 已删除 _output/ 目录"; \
	fi
	@if [ -f index.html ]; then \
		rm -f index.html; \
		echo "   ✅ 已删除 index.html"; \
	fi
	@count=$$(find $(PROJECT_ROOT) -maxdepth 1 -name "*.html" -type f | wc -l | tr -d ' '); \
	if [ "$$count" -gt 0 ]; then \
		find $(PROJECT_ROOT) -maxdepth 1 -name "*.html" -type f -delete; \
		echo "   ✅ 已清理项目根目录下 $$count 个残留 HTML 文件"; \
	fi
	@echo "   🎉 清理完成"

open: ## 用浏览器打开画廊页面
	@if [ ! -f index.html ]; then \
		echo "⚠️  画廊页面尚未生成，先执行生成..."; \
		$(MAKE) generate; \
	fi
	@echo "🌐 用浏览器打开画廊页面..."
	@if command -v open > /dev/null 2>&1; then \
		open index.html; \
	elif command -v xdg-open > /dev/null 2>&1; then \
		xdg-open index.html; \
	else \
		echo "   请手动打开: $(CURDIR)/index.html"; \
	fi
