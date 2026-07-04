# rnskill

[中文](README.zh.md) | English

AI Agent Skills maintained by 雪踏乌云 for Codex, Claude Code, and other Agent workflows that support `SKILL.md`.

This repository is a personal collection for skills I use and iterate over time. It currently includes one skill; more will be added later.

## Requirements

- Codex, Claude Code, or another Agent that supports project-level skills.
- A target project that can load `.agents/skills/<skill-name>/SKILL.md`.

## Installation

### Codex Project-Level Install

Copy only the skill you need into your project:

```bash
mkdir -p <project>/.agents/skills
cp -R skills/renhua <project>/.agents/skills/renhua
```

Expected structure:

```text
<project>/
└── .agents/
    └── skills/
        └── renhua/
            └── SKILL.md
```

### Claude Code Project-Level Install

If your project uses `.claude/skills`:

```bash
mkdir -p <project>/.claude/skills
cp -R skills/renhua <project>/.claude/skills/renhua
```

## Available Skills

### Writing Skills

#### 人话 (`renhua`)

A Chinese AI/technical writing de-AI editing skill.

Use it for:

- X/Twitter posts
- Chinese technical essays
- AI model reviews
- Product notes
- Public-facing Chinese drafts

Example:

```text
Use $renhua to revise this Chinese AI technical post while preserving my judgment, details, and voice.
```

The skill preserves facts, numbers, model names, test conditions, and author judgment while removing AI-flavored writing patterns.

## Author

雪踏乌云
