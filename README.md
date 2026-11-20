# AI 副业 × 模型自学

一个 Agent Skill（技能型插件），把两件事拆成可执行的流程与清单：

- **用 AI 做副业**：方向选择、获客渠道、定价模型、交付 SOP、90 天启动路线
- **大模型自主学习**：自监督与预训练原理、SFT 与 LoRA/QLoRA 微调、RAG 全链路、DPO/GRPO 对齐、评测，以及四阶段自学路线

不是资料合集，是决策工具：先诊断，再给带数字的方案。

## 目录结构

```
ai-side-hustle-and-model-learning/
├── SKILL.md                           # 入口：双轨分流、诊断问题、工作流、红线
├── references/
│   ├── side-hustle-playbook.md        # 12 个方向矩阵、6 套交付 SOP、定价、90 天路线
│   ├── learning-path.md               # 自监督/微调/RAG/对齐原理 + 四阶段路线 + 显存成本
│   └── templates.md                   # 诊断表、报价单、计划表、验收清单、实验记录
└── scripts/
    └── pricing_calc.py                # 报价反算有效时薪 / 目标时薪反推报价
```

## 安装

把 `ai-side-hustle-and-model-learning/` 整个目录放到 Agent 的技能目录（通常是以 `workspace/.user_skills` 结尾的路径）下，重启会话即可被识别。

```bash
git clone https://github.com/zhu080218/ai-side-hustle-and-model-learning.git
cp -r ai-side-hustle-and-model-learning/ai-side-hustle-and-model-learning ~/workspace/.user_skills/
```

## 什么时候会触发

- 「AI 能做什么副业」「怎么用 AI 赚钱」「接单怎么报价」「要不要辞职做副业」
- 「自监督学习原理」「微调怎么做」「LoRA 和 RAG 怎么选」「怎么自学大模型」「给条学习路线」

## 报价脚本

```bash
# 已知报价，算净收入与有效时薪
python scripts/pricing_calc.py --quote 3000 --hours 12 --revisions 2 --revision-hours 1.5 --cost 200 --fee-rate 0.05

# 已知目标时薪，反推应报价格
python scripts/pricing_calc.py --target-hourly 300 --hours 10 --cost 150 --fee-rate 0.1
```

## 设计取舍

1. **客户来源权重不低于技能**。AI 降低的是生产成本，不是信任成本。
2. **学习按级别而非兴趣**。L0/L1/L2 定级，每阶段配可验收项目——没有验收指标的学习计划只是焦虑的排版。
3. **不承诺收益**。所有收入表述为「区间 + 前提条件」。

## 边界

拒绝刷单、代写论文、洗稿搬运、账号买卖、伪造他人形象或声音等方向，遇到时给合规替代路径。

## License

MIT
