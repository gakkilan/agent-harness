# Agent 配置

## 默认 Agent

当前配置在 `config/opencode.json`：

```json
{
  "model": "moonshot/kimi-k2.6",
  "agent": {
    "default": {
      "options": {
        "max_completion_tokens": 16000,
        "extra_body": {
          "thinking": {
            "type": "enabled",
            "keep": "all"
          }
        }
      }
    }
  }
}
```

## 可用模型

| 模型 | 说明 |
|------|------|
| moonshot/kimi-k2.6 | 默认模型，支持 thinking |
| moonshot/kimi-k2.5 | 上一代模型 |
| moonshot/kimi-k2-thinking | 专用思考模型 |

## 自定义 Agent

在 `agents/` 目录创建 JSON 文件：

```json
{
  "name": "my-agent",
  "prompt": "你是一个专业的代码审查员...",
  "tools": ["read", "edit", "bash"],
  "options": {
    "max_completion_tokens": 8000
  }
}
```

## Skills 集成

已安装的 Skills（`~/.config/opencode/skills/`）：

### Superpowers (14)
- brainstorming
- dispatching-parallel-agents
- executing-plans
- finishing-a-development-branch
- receiving-code-review
- requesting-code-review
- subagent-driven-development
- systematic-debugging
- test-driven-development
- using-git-worktrees
- using-superpowers
- verification-before-completion
- writing-plans
- writing-skills

### UI UX Pro Max (7)
- banner-design
- brand
- design
- design-system
- slides
- ui-styling
- ui-ux-pro-max

### Sanyuan Skills (5)
- book-study
- code-review-expert
- sigma
- skill-forge
- wiki-ingest

### 其他 (2)
- web-access
- skill-creator

---

*返回 [[Home]]*
