# rnskill

中文 | [English](README.md)

雪踏乌云维护的 AI Agent Skills 集合，适用于 Codex、Claude Code 等支持 `SKILL.md` 的 Agent 工作流。

当前覆盖中文写作、动效导演、原创参考动效复刻、风格化视频、片头包装和带逐帧证据的复刻质检。

## 前置要求

- 已安装 Codex、Claude Code 或其他支持项目级 Skill 的 Agent。
- 目标项目可以读取 `.agents/skills/<skill-name>/SKILL.md`。

## 安装

### Claude Code 插件市场

```bash
claude plugin marketplace add Pluviobyte/rnskill
claude plugin install rn-renhua@rnskill
```

### 通用安装（Codex / Claude Code）

```bash
npx -y skills add Pluviobyte/rnskill -g --all
```

安装单个 Skill：

```bash
npx -y skills add Pluviobyte/rnskill --skill rn-renhua
```

### 手动安装

只把需要的 Skill 复制到目标项目即可：

```bash
# Codex
mkdir -p <project>/.agents/skills
cp -R skills/rn-renhua <project>/.agents/skills/rn-renhua
cp -R skills/rn-motion-replica <project>/.agents/skills/rn-motion-replica

# Claude Code
mkdir -p <project>/.claude/skills
cp -R skills/rn-renhua <project>/.claude/skills/rn-renhua
cp -R skills/rn-motion-replica <project>/.claude/skills/rn-motion-replica
```

## 可用技能

### 写作精修

| Skill | 说明 |
|-------|------|
| [`rn-renhua`](skills/rn-renhua/) | 中文 AI/技术写作去 AI 味精修。去除二元对比壳、伪洞察标记、冒号讲义腔等 AI 写作模式，保留作者判断和具体事实。 |

### 视频制作

| Skill | 说明 |
|-------|------|
| [`rn-motion-director`](skills/rn-motion-director/) | AI 动效导演元 Skill。把选题/脚本转化为动效视频概念：视觉隐喻、运动语法、场景节拍图、Anti-PPT 质量门。 |
| [`rn-motion-replica`](skills/rn-motion-replica/) | 从获授权的参考片段构建原创、可编辑的 HyperFrames 动效工程，附参考分析证据和最终 MP4 质检。 |
| [`rn-dark-saas-video`](skills/rn-dark-saas-video/) | 暗色 SaaS 魔术短片。黑色星空舞台 + 紫色底光 + 大字动效 + 渐变 CTA。8 套场景蓝图、3 种时长预设。 |
| [`rn-bw-text-opener`](skills/rn-bw-text-opener/) | 黑白文字打字机开场动画。纯黑背景 + 白色逐字打字 + 同步音效 + 文字替换效果。3 种时长预设，附带 Python 时序规划脚本。 |

### 视频质检

| Skill | 说明 |
|-------|------|
| [`rn-replica-qc`](skills/rn-replica-qc/) | SOP v2 复刻质检。五级保真度，加上素材、运行时、交付三道全帧门；逐帧重放与参数化动效分别入库。 |

## 目录结构

```text
rnskill/
├── skills/
│   ├── rn-renhua/              # 写作：去 AI 味精修
│   ├── rn-motion-director/     # 视频：动效导演
│   ├── rn-motion-replica/      # 视频：原创可编辑动效复刻
│   ├── rn-dark-saas-video/     # 视频：暗色 SaaS 风格
│   ├── rn-bw-text-opener/      # 视频：黑白打字开场
│   └── rn-replica-qc/          # 质检：参考视频复刻
├── docs/                       # 各 Skill 概览页
├── assets/                     # 展示图片和视频
├── tools/                      # 打包和构建脚本
├── .claude-plugin/             # Claude Code 插件市场清单
└── .github/workflows/          # 发布自动化
```

## 维护同步

四个镜像视频 Skill 以 `Pluviobyte/video-production-skills` 为开发源。下面的命令只刷新这些镜像，不会覆盖 `rn-renhua`、`rn-motion-replica` 等 `rnskill` 原生 Skill：

```bash
python3 tools/sync-video-skills.py --source /path/to/video-production-skills
python3 tools/sync-video-skills.py --source /path/to/video-production-skills --check
```

## 许可证

CC BY-NC 4.0。详见 [LICENSE](LICENSE)。

## 作者

雪踏乌云 · [@Pluvio9yte](https://x.com/Pluvio9yte)
