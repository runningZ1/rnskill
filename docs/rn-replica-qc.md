# Reference Video Replica QC

用于参考视频复刻、拆解、对齐质检和动效组件沉淀。它不是“凭感觉复刻”，而是先抽帧、写时间线，再用候选视频做对照验证；如果目标是 HyperFrames / Remotion 重制，还会通过多轮对比和返修改代码，把参考视频里的动效拆成可复用组件。

## 示例成片：Presenton 复刻 Bitexact 成片

[▶ Watch Presenton Replica Bitexact Showcase](https://github.com/user-attachments/assets/f792bd12-d8b3-43b7-b751-98aeb033713b)

- 类型：参考视频复刻结果
- 级别：bit-exact / pixel-aligned 交付成片
- 时长：35.136 秒
- 规格：1920x1080，30fps，H.264 + AAC
- 文件：`rn-replica-qc/assets/showcases/presenton-replica-pixel-aligned-bitexact.mp4`

0.5 秒对照抽帧：

![0.5 秒对照图](../assets/images/rn-replica-qc-compare.jpg)

## 做什么类型的视频

- 参考视频复刻
- HyperFrames / Remotion 动效重制
- 可复用视频动效组件沉淀
- 像素级/视觉级/风格级对齐判断
- HyperFrames / Remotion 重制视频的质检
- “当前仍然没有对齐”这类返修定位

## 长期意义

这个 skill 的重点不是复制某一个视频文件，而是把参考视频中真正有视频感的运动语言拆出来：镜头节奏、线条轨道、模型列表、卡片状态切换、标题入场、遮罩、缩放、转场、字幕层级和 CTA 动效。每个被复刻并验证过的段落，都可以进一步整理成 HyperFrames / Remotion 能写、能组合、能参数化的组件。

组件库积累起来以后，AI 制作视频时就能根据内容自由选择：这个段落用模型切换组件，那个段落用流程推进组件，结尾用 CTA 组件，解释概念时用卡片展开组件。这样视频会越来越像真正的动态内容，而不是传统代码生成视频里常见的一页页 PPT 式切换。

## 风格与方法

这是一个质检和拆解 skill，本身不固定某种视觉风格。它关注证据：

- 每 `0.5s` 抽帧
- 失败窗口用 `0.1s` 或指定时间点密采样
- 秒级行为时间线
- side-by-side contact sheet
- 局部 crop / overlay / 组件级对齐证据
- 返修日志和相邻时间点回测
- PSNR / SSIM / 哈希 / `cmp` 等硬指标
- 第一个失败时间点和修复清单

每个可复用组件都应该记录：

- 组件描述和适用场景
- 输入参数和内容槽位
- 时间线、缓动、状态变化
- 技术栈：HyperFrames / Remotion / React / CSS / SVG / GSAP
- 对齐证据和已知限制

## 适合使用

- "复刻这个视频。"
- "每 0.5 秒抽帧分析原视频。"
- "检查新视频和参考视频是否对齐。"
- "我要像素级对齐。"
- "把这个动效复刻成 HyperFrames/Remotion 组件。"
- "把这段参考视频里的模型列表/线条/卡片动效沉淀到组件库。"

## 不适合使用

- 只想做一个同风格原创短片。那更适合 `rn-dark-saas-video`。
- 只想做黑底白字开场。那更适合 `rn-bw-text-opener`。
- 想让手写 HyperFrames/Remotion 直接变成像素级同帧视频。没有源素材和硬指标时，目标应写成视觉级对齐。

## 安装

```bash
npx skills add https://github.com/Pluviobyte/rnskill --skill rn-replica-qc
```
