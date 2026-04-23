# 回归测试模板

## 概述

本模板定义 pyantv 项目的回归测试流程，确保每次代码变更不会破坏现有功能。

## 测试维度

### 维度 1: 单元测试

```bash
pytest test/ -v --tb=short
```

**判定规则**：
- 全部 PASS → ✅
- 任何 FAIL → ❌ 整体 FAIL

### 维度 2: 覆盖率

```bash
pytest -v --cov-config=.coveragerc --cov=./ --cov-report=term-missing test/
```

**判定规则**：
- 总覆盖率 ≥ 70% → ✅
- 增量覆盖率 ≥ 70% → ✅
- 低于阈值 → ⚠️ WARNING

### 维度 3: Lint 检查

```bash
make lint
```

**判定规则**：
- 无错误 → ✅
- 有错误 → ⚠️ WARNING（不阻塞，但记录）

### 维度 4: 渲染验证

```bash
pytest test/ -v -k "render"
```

**判定规则**：
- 全部 PASS → ✅
- 任何 FAIL → ⚠️ WARNING

## 报告格式

```markdown
## 回归测试报告

### 执行时间: YYYY-MM-DD HH:MM:SS
### Sprint: N

| 维度 | 状态 | 详情 |
|------|------|------|
| 单元测试 | ✅/❌ | X passed, Y failed |
| 覆盖率 | ✅/⚠️ | 总覆盖率 XX%, 增量 XX% |
| Lint | ✅/⚠️ | X errors, Y warnings |
| 渲染验证 | ✅/⚠️ | X passed, Y failed |

### 总体判定: PASS / FAIL / WARNING

### 失败详情
（如有失败，列出具体的测试名称和错误信息）
```

## 关键模块覆盖率基线

| 模块 | 最低覆盖率 |
|------|----------|
| `pyantv/charts/basic_charts/` | 75% |
| `pyantv/charts/composition_charts/` | 70% |
| `pyantv/options/` | 80% |
| `pyantv/render/` | 70% |
| `pyantv/commons/` | 70% |

## 执行顺序

```
1. Lint 检查（最快，先排除格式问题）
   ↓
2. 单元测试（核心验证）
   ↓
3. 覆盖率分析（质量指标）
   ↓
4. 渲染验证（输出正确性）
```

## 快速回归 vs 完整回归

### 快速回归（Preflight，30 秒）
- Lint 检查
- `make build` 构建验证

### 完整回归（Full Regression）
- 所有 4 个维度
- 输出完整报告
