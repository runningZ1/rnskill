# rnskill

[中文](README.zh.md) | English

AI Agent Skills maintained by 雪踏乌云 for Codex, Claude Code, and other Agent workflows that support `SKILL.md`.

## Requirements

- Codex, Claude Code, or another Agent that supports project-level skills.
- A target project that can load `.agents/skills/<skill-name>/SKILL.md`.

## Installation

### Claude Code Plugin Marketplace

```bash
claude plugin marketplace add Pluviobyte/rnskill
claude plugin install rn-renhua@rnskill
```

### Universal (Codex / Claude Code)

```bash
npx -y skills add Pluviobyte/rnskill -g --all
```

Or install a single skill:

```bash
npx -y skills add Pluviobyte/rnskill --skill rn-renhua
```

### Manual Install

Copy only the skill you need into your project:

```bash
# Codex
mkdir -p <project>/.agents/skills
cp -R skills/rn-renhua <project>/.agents/skills/rn-renhua

# Claude Code
mkdir -p <project>/.claude/skills
cp -R skills/rn-renhua <project>/.claude/skills/rn-renhua
```

## Available Skills

### Writing

| Skill | Description |
|-------|-------------|
| [`rn-renhua`](skills/rn-renhua/) | Chinese AI/tech writing de-AI editor. Removes AI-flavored patterns while preserving author voice, facts, and judgment. |

### Video Production

| Skill | Description |
|-------|-------------|
| [`rn-motion-director`](skills/rn-motion-director/) | Motion-first AI video director. Turns topics into motion video concepts with visual metaphors, beat graphs, and anti-PPT QC. |
| [`rn-dark-saas-video`](skills/rn-dark-saas-video/) | Dark cinematic SaaS product video in "magic UI" style. 8 scene blueprints, 3 timing presets, hard style rules. |
| [`rn-bw-text-opener`](skills/rn-bw-text-opener/) | Black-white typed text opener animation with synced typing SFX. 3 timing presets. Includes a Python timing plan generator. |

### Quality Control

| Skill | Description |
|-------|-------------|
| [`rn-replica-qc`](skills/rn-replica-qc/) | Reference video replica QC. Three fidelity levels (pixel/visual/style), frame comparison, PSNR/SSIM, reusable component capture. |

## Directory Structure

```text
rnskill/
├── skills/
│   ├── rn-renhua/              # Writing: de-AI editor
│   ├── rn-motion-director/     # Video: motion director
│   ├── rn-dark-saas-video/     # Video: dark SaaS style
│   ├── rn-bw-text-opener/      # Video: typed text opener
│   └── rn-replica-qc/          # QC: reference video replica
├── docs/                       # Per-skill overview pages
├── assets/                     # Showcase images and videos
├── tools/                      # Build and packaging scripts
├── .claude-plugin/             # Claude Code marketplace manifest
└── .github/workflows/          # Release automation
```

## License

CC BY-NC 4.0. See [LICENSE](LICENSE).

## Author

雪踏乌云 · [@Pluvio9yte](https://x.com/Pluvio9yte)
