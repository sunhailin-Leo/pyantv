#!/usr/bin/env python3
"""
pyantv 示例画廊生成器
扫描 examples/ 目录，批量运行示例并生成 index.html 画廊页面
"""
import os
import re
import subprocess
import sys
import json
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent
PROJECT_ROOT = EXAMPLES_DIR.parent
OUTPUT_DIR = EXAMPLES_DIR / "_output"

# 目录名 → 中文分类名映射
CATEGORY_NAMES = {
    # 一级分类
    "general": "基础图表",
    "annotation": "数据标注",
    "component": "组件",
    "composite": "空间复合",
    "network": "关系图",
    "map": "地图",
    "tree": "树图",
    "interaction": "交互",
    "advanced": "高级功能",
    "threed": "3D 图表",
    "fun": "趣味可视化",
    "scenario": "场景可视化",
    "style": "样式",
    # 二级分类 - general
    "interval": "条形图",
    "line": "折线图",
    "point": "散点图",
    "area": "面积图",
    "cell": "色块图",
    "heatmap": "热力图",
    "pie": "饼图",
    "rose": "玫瑰图",
    "radar": "雷达图",
    "radial": "径向图",
    "histogram": "直方图",
    "box": "箱线图",
    "stock": "股票图",
    "gauge": "仪表盘",
    "liquid": "水波图",
    "wordcloud": "词云图",
    "sunburst": "旭日图",
    "funnel": "漏斗图",
    "bullet": "子弹图",
    "mini": "迷你图",
    "violin": "小提琴图",
    "venn": "韦恩图",
    "spiral": "螺旋图",
    "smooth": "平滑图",
    "swarm": "蜂群图",
    "polygon": "多边形",
    "text": "文本",
    "image": "图片",
    "vector": "向量场",
    "connection": "连接图",
    "parallel": "平行坐标系",
    "multi_axis": "多轴图",
    "density_heatmap": "密度热力图",
    "data_processing": "数据处理",
    "binning": "分箱",
    "grouping": "分组",
    # 二级分类 - annotation
    "text_annotation": "文本标注",
    "line_annotation": "线标注",
    "interval_annotation": "区间标注",
    "shape_annotation": "图形标注",
    "connection_annotation": "连接标注",
    # 二级分类 - component
    "axis": "坐标轴",
    "legend": "图例",
    "tooltip": "提示",
    "label": "数据标签",
    "title": "图表标题",
    "scrollbar": "滚动条",
    "animation": "过渡动画",
    "lottie": "Lottie 动画",
    "element": "元素",
    # 二级分类 - composite
    "space": "空间复合",
    "facet": "分面复合",
    "repeat": "重复复合",
    # 二级分类 - interaction
    "event": "事件",
    "brush": "刷选",
    "data_shape": "数形交互",
    # 二级分类 - advanced
    "other": "其他",
    "auto_visualization": "自动可视化",
    "insight": "洞察标注",
    "narrative": "可视化叙事",
    "sorting": "排序",
    "unit_visualization": "单元可视化",
    # 二级分类 - threed
    "scatter": "3D 散点图",
    "bar": "3D 柱状图",
    "surface": "3D 曲面图",
    # 二级分类 - style
    "theme": "主题",
    "sketch": "手绘",
    "pattern": "纹理",
    "drawing": "绘图属性",
    "renderer": "渲染器",
    "text_search": "文本搜索",
    "spec": "Spec 函数表达式",
}

# 一级分类排序
CATEGORY_ORDER = [
    "general", "annotation", "component", "composite",
    "tree", "network", "map",
    "interaction", "advanced",
    "threed", "fun", "scenario", "style",
]


def _highlight_python(code: str) -> str:
    """在 Python 端对源码做语法高亮，生成安全的 HTML"""
    import html as html_mod

    keywords = {
        "from", "import", "as", "def", "class", "return", "if", "else", "elif",
        "for", "in", "while", "try", "except", "finally", "with", "yield",
        "lambda", "and", "or", "not", "is", "True", "False", "None",
    }

    lines = code.split("\n")
    result = []
    in_docstring = False
    docstring_delim = '"""'

    for line in lines:
        stripped = line.lstrip()

        # 处理 docstring
        if in_docstring:
            escaped = html_mod.escape(line)
            if docstring_delim in line:
                in_docstring = False
            result.append(f'<span class="str">{escaped}</span>')
            continue

        if stripped.startswith('"""') or stripped.startswith("'''"):
            docstring_delim = stripped[:3]
            escaped = html_mod.escape(line)
            # 单行 docstring
            if line.count(docstring_delim) >= 2:
                result.append(f'<span class="str">{escaped}</span>')
            else:
                in_docstring = True
                result.append(f'<span class="str">{escaped}</span>')
            continue

        # 找注释位置（排除字符串内的 #）
        comment_idx = -1
        in_str = False
        str_char = ""
        for j, ch in enumerate(line):
            if in_str:
                if ch == str_char and (j == 0 or line[j - 1] != "\\"):
                    in_str = False
                continue
            if ch in ('"', "'"):
                in_str = True
                str_char = ch
                continue
            if ch == "#":
                comment_idx = j
                break

        code_part = line[:comment_idx] if comment_idx >= 0 else line
        comment_part = line[comment_idx:] if comment_idx >= 0 else ""

        # 逐字符 tokenize 代码部分
        tokens = []
        i = 0
        while i < len(code_part):
            ch = code_part[i]

            # 字符串
            if ch in ('"', "'"):
                end = i + 1
                while end < len(code_part):
                    if code_part[end] == ch and code_part[end - 1] != "\\":
                        end += 1
                        break
                    end += 1
                tokens.append(("str", code_part[i:end]))
                i = end
                continue

            # 数字
            if ch.isdigit() or (ch == "." and i + 1 < len(code_part) and code_part[i + 1].isdigit()):
                end = i
                has_dot = False
                while end < len(code_part) and (code_part[end].isdigit() or (code_part[end] == "." and not has_dot)):
                    if code_part[end] == ".":
                        has_dot = True
                    end += 1
                # 确保前面不是标识符的一部分
                if i == 0 or not (code_part[i - 1].isalnum() or code_part[i - 1] == "_"):
                    tokens.append(("num", code_part[i:end]))
                else:
                    tokens.append(("plain", code_part[i:end]))
                i = end
                continue

            # 标识符/关键字
            if ch.isalpha() or ch == "_":
                end = i
                while end < len(code_part) and (code_part[end].isalnum() or code_part[end] == "_"):
                    end += 1
                word = code_part[i:end]
                # 检查是否是函数调用
                rest = code_part[end:].lstrip()
                if word in keywords:
                    tokens.append(("kw", word))
                elif rest.startswith("("):
                    tokens.append(("fn", word))
                else:
                    tokens.append(("plain", word))
                i = end
                continue

            tokens.append(("plain", ch))
            i += 1

        # 组装
        highlighted_parts = []
        for token_type, token_val in tokens:
            escaped_val = html_mod.escape(token_val)
            if token_type == "plain":
                highlighted_parts.append(escaped_val)
            else:
                highlighted_parts.append(f'<span class="{token_type}">{escaped_val}</span>')

        code_html = "".join(highlighted_parts)
        if comment_part:
            code_html += f'<span class="cmt">{html_mod.escape(comment_part)}</span>'

        result.append(code_html)

    return "\n".join(result)


def extract_metadata(filepath: Path) -> dict:
    """从 .py 文件的 docstring 中提取标题和 G2 链接"""
    content = filepath.read_text(encoding="utf-8")
    title = filepath.stem.replace("_", " ").title()
    g2_url = ""

    docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
    if docstring_match:
        lines = docstring_match.group(1).strip().split("\n")
        if lines:
            title = lines[0].strip()
        for line in lines[1:]:
            line = line.strip()
            if "g2.antv.antgroup.com" in line:
                url_match = re.search(r"https?://[^\s]+", line)
                if url_match:
                    g2_url = url_match.group(0)
                break

    return {"title": title, "g2_url": g2_url, "source": content, "source_highlighted": _highlight_python(content)}


def scan_examples() -> list:
    """扫描 examples/ 目录，收集所有示例元数据"""
    examples = []
    skip_dirs = {"_output", "__pycache__"}

    for py_file in sorted(EXAMPLES_DIR.rglob("*.py")):
        if py_file.name == "generate_gallery.py":
            continue
        rel = py_file.relative_to(EXAMPLES_DIR)
        parts = list(rel.parts)
        if any(skip in parts for skip in skip_dirs):
            continue

        metadata = extract_metadata(py_file)
        category_parts = parts[:-1]
        category_level1 = category_parts[0] if category_parts else "other"
        category_level2 = category_parts[1] if len(category_parts) > 1 else ""

        category_level1_name = CATEGORY_NAMES.get(category_level1, category_level1)
        category_level2_name = CATEGORY_NAMES.get(category_level2, category_level2) if category_level2 else ""

        output_html_name = str(rel.with_suffix(".html")).replace("/", "__")

        examples.append({
            "file": str(rel),
            "abs_path": str(py_file),
            "title": metadata["title"],
            "g2_url": metadata["g2_url"],
            "source": metadata["source"],
            "source_highlighted": metadata["source_highlighted"],
            "category_l1": category_level1,
            "category_l1_name": category_level1_name,
            "category_l2": category_level2,
            "category_l2_name": category_level2_name,
            "output_html": output_html_name,
        })

    return examples


def _find_generated_html(example: dict) -> Path | None:
    """查找示例运行后生成的 HTML 文件"""
    source_content = Path(example["abs_path"]).read_text(encoding="utf-8")
    render_match = re.search(r'\.render\(\s*["\']([^"\']+)["\']\s*\)', source_content)
    if render_match:
        render_name = render_match.group(1)
        candidate = PROJECT_ROOT / render_name
        if candidate.exists():
            return candidate

    stem = Path(example["file"]).stem
    candidate = PROJECT_ROOT / f"{stem}.html"
    if candidate.exists():
        return candidate

    return None


def run_examples(examples: list) -> None:
    """批量运行所有示例，生成 HTML 到 _output/ 目录"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    total = len(examples)
    success_count = 0
    fail_count = 0

    for i, example in enumerate(examples, 1):
        output_html = OUTPUT_DIR / example["output_html"]

        print(f"[{i}/{total}] Running {example['file']}...", end=" ", flush=True)
        try:
            result = subprocess.run(
                [sys.executable, example["abs_path"]],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(PROJECT_ROOT),
            )
            generated_html = _find_generated_html(example)

            if generated_html and generated_html.exists():
                generated_html.rename(output_html)
                print("✅")
                success_count += 1
            elif result.returncode == 0:
                placeholder = f"<html><body><h2>{example['title']}</h2><p>渲染输出未找到</p></body></html>"
                output_html.write_text(placeholder, encoding="utf-8")
                print("⚠️ (no output)")
                success_count += 1
            else:
                placeholder = f"<html><body><h2>{example['title']}</h2><pre>{result.stderr[:500]}</pre></body></html>"
                output_html.write_text(placeholder, encoding="utf-8")
                print(f"❌ (exit {result.returncode})")
                fail_count += 1
        except subprocess.TimeoutExpired:
            placeholder = f"<html><body><h2>{example['title']}</h2><p>运行超时</p></body></html>"
            output_html.write_text(placeholder, encoding="utf-8")
            print("⏰ (timeout)")
            fail_count += 1
        except Exception as exc:
            placeholder = f"<html><body><h2>{example['title']}</h2><p>Error: {exc}</p></body></html>"
            output_html.write_text(placeholder, encoding="utf-8")
            print(f"💥 ({exc})")
            fail_count += 1

    print(f"\n完成: {success_count} 成功, {fail_count} 失败, 共 {total} 个示例")


def _build_html_template() -> str:
    """返回 HTML 模板字符串，使用 %%PLACEHOLDER%% 作为占位符，避免 f-string 反斜杠问题"""
    return r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>pyantv 示例画廊 — G2 for Python</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #f5f7fa; color: #333; }
.header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 24px 32px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 2px 8px rgba(0,0,0,.15); position: sticky; top: 0; z-index: 100; }
.header h1 { font-size: 22px; font-weight: 600; }
.header h1 span { font-weight: 300; opacity: .8; font-size: 14px; margin-left: 8px; }
.header-right { display: flex; align-items: center; gap: 16px; }
.search-box { padding: 8px 16px; border: none; border-radius: 20px; width: 280px; font-size: 14px; outline: none; background: rgba(255,255,255,.2); color: white; }
.search-box::placeholder { color: rgba(255,255,255,.6); }
.search-box:focus { background: rgba(255,255,255,.3); }
.stats { font-size: 13px; opacity: .8; }
.container { display: flex; min-height: calc(100vh - 72px); }
.sidebar { width: 260px; background: #fff; border-right: 1px solid #e8e8e8; overflow-y: auto; flex-shrink: 0; padding: 12px 0; }
.nav-all { padding: 10px 20px; cursor: pointer; font-weight: 600; color: #667eea; border-bottom: 1px solid #f0f0f0; }
.nav-all:hover { background: #f5f0ff; }
.nav-all.active { background: #f0ebff; }
.nav-category-header { padding: 10px 20px; cursor: pointer; font-weight: 500; display: flex; align-items: center; gap: 6px; user-select: none; transition: background .15s; }
.nav-category-header:hover { background: #f5f5f5; }
.nav-category-header.active { background: #f0ebff; color: #667eea; }
.nav-category-header .arrow { font-size: 10px; transition: transform .2s; display: inline-block; width: 14px; }
.nav-category-header .arrow.open { transform: rotate(90deg); }
.nav-category-header .count { color: #999; font-size: 12px; margin-left: auto; }
.nav-sub-item { padding: 7px 20px 7px 44px; cursor: pointer; font-size: 13px; color: #666; transition: all .15s; }
.nav-sub-item:hover { background: #f5f5f5; color: #333; }
.nav-sub-item.active { background: #f0ebff; color: #667eea; font-weight: 500; }
.nav-sub-item .count { color: #aaa; font-size: 12px; }
.main { flex: 1; padding: 24px; overflow-y: auto; }
.breadcrumb { font-size: 13px; color: #999; margin-bottom: 16px; }
.breadcrumb span { color: #667eea; }
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; }
.card { background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,.08); cursor: pointer; transition: all .2s; border: 2px solid transparent; }
.card:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,.12); border-color: #667eea; }
.card-preview { height: 160px; background: #fafafa; display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative; }
.card-preview iframe { border: none; pointer-events: none; width: 200%; height: 200%; transform: scale(0.5); transform-origin: 0 0; position: absolute; top: 0; left: 0; }
.card-preview .placeholder { font-size: 48px; opacity: .3; display: none; }
.card-preview.loading .placeholder { display: flex; }
.card-preview.loading iframe { display: none; }
.card-body { padding: 12px 16px; }
.card-title { font-size: 14px; font-weight: 500; color: #333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.card-meta { font-size: 11px; color: #aaa; margin-top: 4px; }
.modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,.5); z-index: 200; backdrop-filter: blur(4px); }
.modal-overlay.show { display: flex; align-items: center; justify-content: center; }
.modal { background: #fff; border-radius: 12px; width: 90vw; height: 85vh; max-width: 1400px; display: flex; flex-direction: column; box-shadow: 0 20px 60px rgba(0,0,0,.3); }
.modal-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; border-bottom: 1px solid #eee; flex-shrink: 0; }
.modal-header h2 { font-size: 18px; font-weight: 600; }
.modal-header-actions { display: flex; gap: 12px; align-items: center; }
.modal-header a { color: #667eea; text-decoration: none; font-size: 13px; }
.modal-header a:hover { text-decoration: underline; }
.modal-close { background: none; border: none; font-size: 24px; cursor: pointer; color: #999; padding: 4px 8px; border-radius: 4px; }
.modal-close:hover { background: #f5f5f5; color: #333; }
.modal-body { display: flex; flex: 1; overflow: hidden; }
.modal-preview { flex: 1; border-right: 1px solid #eee; position: relative; }
.modal-preview iframe { width: 100%; height: 100%; border: none; }
.modal-source { width: 45%; overflow: auto; position: relative; }
.modal-source pre { margin: 0; padding: 16px; font-size: 13px; line-height: 1.6; font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace; background: #1e1e2e; color: #cdd6f4; height: 100%; overflow: auto; }
.modal-source .copy-btn { position: absolute; top: 8px; right: 8px; background: rgba(255,255,255,.15); color: #cdd6f4; border: none; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; z-index: 10; }
.modal-source .copy-btn:hover { background: rgba(255,255,255,.25); }
.modal-tabs { display: flex; border-bottom: 1px solid #eee; flex-shrink: 0; }
.modal-tab { padding: 8px 20px; cursor: pointer; font-size: 13px; border-bottom: 2px solid transparent; color: #666; }
.modal-tab.active { color: #667eea; border-bottom-color: #667eea; font-weight: 500; }
.empty { text-align: center; padding: 60px 20px; color: #999; }
.empty-icon { font-size: 48px; margin-bottom: 16px; }
@media (max-width: 768px) {
  .sidebar { display: none; }
  .card-grid { grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); }
  .modal { width: 95vw; height: 90vh; }
  .modal-body { flex-direction: column; }
  .modal-source { width: 100%; height: 40%; }
}
.kw { color: #cba6f7; } .str { color: #a6e3a1; } .num { color: #fab387; }
.cmt { color: #6c7086; font-style: italic; } .fn { color: #89b4fa; }
</style>
</head>
<body>
<div class="header">
  <h1>🐍 pyantv 示例画廊 <span>基于 AntV G2 v5 的 Python 可视化库</span></h1>
  <div class="header-right">
    <div class="stats" id="statsText"></div>
    <input class="search-box" type="text" id="searchInput" placeholder="🔍 搜索示例..." oninput="onSearch(this.value)">
  </div>
</div>
<div class="container">
  <div class="sidebar">
    <div class="nav-all active" onclick="showAll()">📋 全部示例</div>
    %%NAV_HTML%%
  </div>
  <div class="main">
    <div class="breadcrumb" id="breadcrumb">📋 <span>全部示例</span></div>
    <div class="card-grid" id="cardGrid"></div>
    <div class="empty" id="emptyState" style="display:none;">
      <div class="empty-icon">🔍</div>
      <p>没有找到匹配的示例</p>
    </div>
  </div>
</div>
<div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
  <div class="modal" onclick="event.stopPropagation()">
    <div class="modal-header">
      <h2 id="modalTitle"></h2>
      <div class="modal-header-actions">
        <a id="modalG2Link" href="#" target="_blank">📖 G2 文档</a>
        <a id="modalFilePath" href="#">📁 源文件</a>
        <button class="modal-close" onclick="closeModal()">&times;</button>
      </div>
    </div>
    <div class="modal-tabs">
      <div class="modal-tab active" onclick="switchTab('preview', this)">👁️ 预览</div>
      <div class="modal-tab" onclick="switchTab('source', this)">📝 源码</div>
      <div class="modal-tab" onclick="switchTab('split', this)">⬜ 分屏</div>
    </div>
    <div class="modal-body" id="modalBody">
      <div class="modal-preview" id="modalPreview">
        <iframe id="modalIframe" src="about:blank"></iframe>
      </div>
      <div class="modal-source" id="modalSource" style="display:none;">
        <button class="copy-btn" onclick="copySource()">📋 复制</button>
        <pre id="modalCode"></pre>
      </div>
    </div>
  </div>
</div>
<script>
const EXAMPLES = %%EXAMPLES_JSON%%;
const ICON_MAP = %%ICON_MAP_JSON%%;
const SOURCES = %%SOURCES_JSON%%;
const SOURCES_HTML = %%SOURCES_HTML_JSON%%;

let currentFilter = { l1: null, l2: null };
let currentSearch = '';

function init() {
  document.getElementById('statsText').textContent = '共 ' + EXAMPLES.length + ' 个示例';
  renderCards(EXAMPLES);
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });
}

function renderCards(items) {
  var grid = document.getElementById('cardGrid');
  var empty = document.getElementById('emptyState');
  if (items.length === 0) { grid.innerHTML = ''; empty.style.display = 'block'; return; }
  empty.style.display = 'none';
  grid.innerHTML = items.map(function(ex) {
    var icon = ICON_MAP[ex.category_l1] || '📊';
    var globalIdx = EXAMPLES.indexOf(ex);
    return '<div class="card" onclick="openModal(' + globalIdx + ')">' +
      '<div class="card-preview">' +
      '<iframe src="_output/' + ex.output_html + '" loading="lazy" sandbox="allow-scripts allow-same-origin"></iframe>' +
      '<div class="placeholder">' + icon + '</div></div>' +
      '<div class="card-body"><div class="card-title" title="' + ex.title + '">' + ex.title + '</div>' +
      '<div class="card-meta">' + ex.category_l1_name + (ex.category_l2_name ? ' / ' + ex.category_l2_name : '') + '</div></div></div>';
  }).join('');
}

function getFilteredExamples() {
  var items = EXAMPLES;
  if (currentFilter.l1) {
    items = items.filter(function(e) { return e.category_l1 === currentFilter.l1; });
    if (currentFilter.l2 && currentFilter.l2 !== '_root') {
      items = items.filter(function(e) { return e.category_l2 === currentFilter.l2; });
    }
  }
  if (currentSearch) {
    var q = currentSearch.toLowerCase();
    items = items.filter(function(e) {
      return e.title.toLowerCase().indexOf(q) >= 0 || e.file.toLowerCase().indexOf(q) >= 0 ||
        e.category_l1_name.indexOf(q) >= 0 || e.category_l2_name.indexOf(q) >= 0;
    });
  }
  return items;
}

function showAll() {
  currentFilter = { l1: null, l2: null };
  document.querySelectorAll('.nav-all, .nav-category-header, .nav-sub-item').forEach(function(el) { el.classList.remove('active'); });
  document.querySelector('.nav-all').classList.add('active');
  document.getElementById('breadcrumb').innerHTML = '📋 <span>全部示例</span>';
  renderCards(getFilteredExamples());
}

function toggleCategory(el, l1) {
  var subList = el.nextElementSibling;
  var arrow = el.querySelector('.arrow');
  var isOpen = subList.style.display !== 'none';
  subList.style.display = isOpen ? 'none' : 'block';
  if (isOpen) { arrow.classList.remove('open'); } else { arrow.classList.add('open'); }
  currentFilter = { l1: l1, l2: null };
  document.querySelectorAll('.nav-all, .nav-category-header, .nav-sub-item').forEach(function(e) { e.classList.remove('active'); });
  el.classList.add('active');
  var found = EXAMPLES.find(function(e) { return e.category_l1 === l1; });
  var catName = found ? found.category_l1_name : l1;
  document.getElementById('breadcrumb').innerHTML = '📋 全部示例 / <span>' + catName + '</span>';
  renderCards(getFilteredExamples());
}

function filterBySubCategory(l1, l2) {
  currentFilter = { l1: l1, l2: l2 };
  document.querySelectorAll('.nav-all, .nav-category-header, .nav-sub-item').forEach(function(e) { e.classList.remove('active'); });
  var target = document.querySelector('.nav-sub-item[data-l1="' + l1 + '"][data-l2="' + l2 + '"]');
  if (target) target.classList.add('active');
  var found1 = EXAMPLES.find(function(e) { return e.category_l1 === l1; });
  var found2 = EXAMPLES.find(function(e) { return e.category_l1 === l1 && e.category_l2 === l2; });
  var catName = found1 ? found1.category_l1_name : l1;
  var subName = found2 ? found2.category_l2_name : l2;
  document.getElementById('breadcrumb').innerHTML = '📋 全部示例 / ' + catName + ' / <span>' + subName + '</span>';
  renderCards(getFilteredExamples());
}

function onSearch(value) { currentSearch = value.trim(); renderCards(getFilteredExamples()); }

function openModal(idx) {
  var ex = EXAMPLES[idx];
  document.getElementById('modalTitle').textContent = ex.title;
  document.getElementById('modalTitle').dataset.idx = idx;
  document.getElementById('modalG2Link').href = ex.g2_url || '#';
  document.getElementById('modalG2Link').style.display = ex.g2_url ? '' : 'none';
  document.getElementById('modalFilePath').textContent = '📁 ' + ex.file;
  document.getElementById('modalIframe').src = '_output/' + ex.output_html;
  document.getElementById('modalCode').innerHTML = SOURCES_HTML[ex.file] || '';
  document.getElementById('modalOverlay').classList.add('show');
  document.body.style.overflow = 'hidden';
  switchTab('split', document.querySelectorAll('.modal-tab')[2]);
}

function closeModal(event) {
  if (event && event.target !== document.getElementById('modalOverlay')) return;
  document.getElementById('modalOverlay').classList.remove('show');
  document.getElementById('modalIframe').src = 'about:blank';
  document.body.style.overflow = '';
}

function switchTab(view, tabEl) {
  document.querySelectorAll('.modal-tab').forEach(function(t) { t.classList.remove('active'); });
  tabEl.classList.add('active');
  var preview = document.getElementById('modalPreview');
  var source = document.getElementById('modalSource');
  if (view === 'preview') { preview.style.display = 'block'; preview.style.flex = '1'; source.style.display = 'none'; }
  else if (view === 'source') { preview.style.display = 'none'; source.style.display = 'block'; source.style.width = '100%'; }
  else { preview.style.display = 'block'; preview.style.flex = '1'; source.style.display = 'block'; source.style.width = '45%'; }
}

function copySource() {
  var ex = EXAMPLES[document.getElementById('modalTitle').dataset.idx];
  var code = SOURCES[ex ? ex.file : ''] || document.getElementById('modalCode').textContent;
  navigator.clipboard.writeText(code).then(function() {
    var btn = document.querySelector('.copy-btn');
    btn.textContent = '✅ 已复制';
    setTimeout(function() { btn.textContent = '📋 复制'; }, 1500);
  });
}

/* highlightPython 已移至 Python 端预处理，SOURCES_HTML 中存储预高亮的 HTML */

init();
</script>
</body>
</html>'''


def generate_html(examples: list) -> None:
    """生成 index.html 画廊页面"""
    categories = {}
    for ex in examples:
        key = ex["category_l1"]
        if key not in categories:
            categories[key] = {"name": ex["category_l1_name"], "subcategories": {}}
        sub_key = ex["category_l2"] or "_root"
        if sub_key not in categories[key]["subcategories"]:
            sub_name = ex["category_l2_name"] if ex["category_l2"] else ex["category_l1_name"]
            categories[key]["subcategories"][sub_key] = {"name": sub_name, "examples": []}
        categories[key]["subcategories"][sub_key]["examples"].append(ex)

    examples_json = json.dumps(
        [
            {
                "file": e["file"],
                "title": e["title"],
                "g2_url": e["g2_url"],
                "category_l1": e["category_l1"],
                "category_l1_name": e["category_l1_name"],
                "category_l2": e["category_l2"],
                "category_l2_name": e["category_l2_name"],
                "output_html": e["output_html"],
            }
            for e in examples
        ],
        ensure_ascii=False,
    )

    icon_map = {
        "general": "📊", "annotation": "📝", "component": "🧩", "composite": "🔲",
        "tree": "🌳", "network": "🔗", "map": "🗺️", "interaction": "👆",
        "advanced": "🚀", "threed": "🧊", "fun": "🎨", "scenario": "🎬", "style": "🎭",
    }

    nav_html_parts = []
    for cat_key in CATEGORY_ORDER:
        if cat_key not in categories:
            continue
        cat = categories[cat_key]
        sub_items = []
        for sub_key, sub_val in cat["subcategories"].items():
            count = len(sub_val["examples"])
            sub_items.append(
                '<div class="nav-sub-item" data-l1="' + cat_key + '" data-l2="' + sub_key
                + '" onclick="filterBySubCategory(\'' + cat_key + "','" + sub_key + '\')">'
                + sub_val["name"] + ' <span class="count">(' + str(count) + ')</span></div>'
            )
        total_count = sum(len(s["examples"]) for s in cat["subcategories"].values())
        nav_html_parts.append(
            '<div class="nav-category">'
            '<div class="nav-category-header" data-l1="' + cat_key
            + '" onclick="toggleCategory(this, \'' + cat_key + '\')">'
            '<span class="arrow">▶</span> ' + cat["name"]
            + ' <span class="count">(' + str(total_count) + ')</span></div>'
            '<div class="nav-sub-list" style="display:none;">' + "".join(sub_items) + '</div>'
            '</div>'
        )
    nav_html = "\n".join(nav_html_parts)

    sources_json = json.dumps({e["file"]: e["source"] for e in examples}, ensure_ascii=False)
    sources_html_json = json.dumps({e["file"]: e["source_highlighted"] for e in examples}, ensure_ascii=False)
    icon_map_json = json.dumps(icon_map, ensure_ascii=False)

    html = _build_html_template()
    html = html.replace("%%NAV_HTML%%", nav_html)
    html = html.replace("%%EXAMPLES_JSON%%", examples_json)
    html = html.replace("%%ICON_MAP_JSON%%", icon_map_json)
    html = html.replace("%%SOURCES_JSON%%", sources_json)
    html = html.replace("%%SOURCES_HTML_JSON%%", sources_html_json)

    output_path = EXAMPLES_DIR / "index.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"\n✅ 画廊页面已生成: {output_path}")


def main():
    print("🔍 扫描示例文件...")
    examples = scan_examples()
    print(f"   找到 {len(examples)} 个示例\n")

    print("🚀 批量运行示例生成 HTML...")
    run_examples(examples)

    print("\n📄 生成画廊页面...")
    generate_html(examples)

    print(f"\n🎉 完成！用浏览器打开 examples/index.html 即可浏览所有示例")


if __name__ == "__main__":
    main()
