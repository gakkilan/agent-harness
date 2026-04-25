# Obsidian Vault 说明

这个目录包含 Obsidian Vault 配置，让你可以在 Obsidian 中管理 Agent Harness。

## 打开 Vault

1. 打开 Obsidian
2. 选择 "Open folder as vault"
3. 选择 `agent-harness` 目录

## 功能特性

### 已配置插件
- **Graph view** - 关系图谱
- **Templates** - 模板系统
- **Page preview** - 页面预览
- **Command palette** - 命令面板
- **Slash commands** - 斜杠命令
- **Starred** - 收藏
- **Outline** - 大纲视图
- **Word count** - 字数统计
- **File recovery** - 文件恢复

### 模板
- `test-template` - 创建新测试用例
- `agent-definition` - 定义新 Agent

### 快捷键
| 快捷键 | 功能 |
|--------|------|
| `Ctrl+G` | 关系图谱 |
| `Ctrl+P` | 命令面板 |
| `Ctrl+←` | 后退 |
| `Ctrl+→` | 前进 |

## 工作流建议

1. **规划阶段**：使用 [[Home]] 和 [[测试目录]] 规划测试
2. **开发阶段**：在 `tests/` 创建测试用例，使用模板
3. **执行阶段**：运行 `run-tests.ps1` 或 `run-tests.sh`
4. **分析阶段**：在 `results/` 查看输出，在 Obsidian 记录笔记

## 链接系统

使用 `[[笔记名]]` 创建双向链接：
- [[Home]]
- [[测试目录]]
- [[使用指南]]
- [[项目结构]]
- [[Agent 配置]]

---

*Vault 初始化于 2026-04-25*
