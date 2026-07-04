# rnskill

中文 | [English](README.md)

雪踏乌云维护的 AI Agent Skills 集合，适用于 Codex、Claude Code 等支持 `SKILL.md` 的 Agent 工作流。

这个仓库用于集中存放我自己长期使用、迭代和发布的 Skills。当前先收录一个 Skill，其他 Skill 后续再逐步加入。

## 前置要求

- 已安装 Codex、Claude Code 或其他支持项目级 Skill 的 Agent。
- 目标项目可以读取 `.agents/skills/<skill-name>/SKILL.md`。

## 安装

### Codex 项目级安装

只把需要的 Skill 复制到目标项目即可：

```bash
mkdir -p <project>/.agents/skills
cp -R skills/renhua <project>/.agents/skills/renhua
```

目录结构示例：

```text
<project>/
└── .agents/
    └── skills/
        └── renhua/
            └── SKILL.md
```

### Claude Code 项目级安装

如果项目使用 `.claude/skills`：

```bash
mkdir -p <project>/.claude/skills
cp -R skills/renhua <project>/.claude/skills/renhua
```

## 可用技能

### 写作技能

#### 人话 (`renhua`)

中文 AI/技术写作去 AI 味精修 Skill。

适合用于：

- X/Twitter 帖子
- 中文技术文章
- AI 模型测评
- 产品笔记
- 公开发布前的中文稿件精修

调用示例：

```text
Use $renhua to revise this Chinese AI technical post while preserving my judgment, details, and voice.
```

本 Skill 默认保留事实、数字、模型名、测试条件和作者判断，避免把技术稿改成顺滑但失去个人判断的泛化文本。

## 目录结构

```text
rnskill/
├── README.zh.md
├── README.md
└── skills/
    └── renhua/
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

## 作者

雪踏乌云
