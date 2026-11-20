# AI Side Hustle × Model Self-Learning

[简体中文](README.md) | **English**

An Agent Skill that turns two fuzzy ambitions into executable process and checklists:

- **Making money with AI** — direction selection, customer acquisition, pricing models, delivery SOPs, a 90-day launch plan
- **Learning LLMs on your own** — self-supervised pretraining, SFT with LoRA/QLoRA, the full RAG pipeline, DPO/GRPO alignment, evaluation, and a four-stage self-study roadmap

This is not a reading list. It is a decision tool: diagnose first, then hand back a plan with numbers in it.

## Structure

```
ai-side-hustle-and-model-learning/
├── SKILL.md                           # Entry: routing, diagnostic questions, workflows, red lines
├── references/
│   ├── side-hustle-playbook.md        # 12 directions matrix, 6 delivery SOPs, pricing, 90-day roadmap
│   ├── learning-path.md               # SSL / fine-tuning / RAG / alignment, roadmap, VRAM & cost
│   └── templates.md                   # diagnostic sheets, quotes, plans, acceptance checklists, experiment logs
└── scripts/
    └── pricing_calc.py                # quote → effective hourly rate, and the reverse
```

## Install

Drop the `ai-side-hustle-and-model-learning/` folder into your agent's skill directory (typically a path ending in `workspace/.user_skills`) and restart the session.

```bash
git clone https://github.com/zhu080218/ai-side-hustle-and-model-learning.git
cp -r ai-side-hustle-and-model-learning/ai-side-hustle-and-model-learning ~/workspace/.user_skills/
```

## When it triggers

- "What side hustles can I do with AI?" / "How do I actually make money with this?" / "How should I price this gig?" / "Should I quit my job for this?"
- "How does self-supervised learning work?" / "How do I fine-tune?" / "LoRA or RAG?" / "How do I learn LLMs from scratch?" / "Give me a study plan."

## Pricing script

```bash
# Given a quote, compute net income and effective hourly rate
python scripts/pricing_calc.py --quote 3000 --hours 12 --revisions 2 --revision-hours 1.5 --cost 200 --fee-rate 0.05

# Given a target hourly rate, compute the quote you should send
python scripts/pricing_calc.py --target-hourly 300 --hours 10 --cost 150 --fee-rate 0.1
```

## Design choices

1. **Customer access outweighs tool skills.** AI cheapens production, not trust.
2. **Learn by level, not by curiosity.** L0/L1/L2 placement, every stage gated by an acceptance test — a study plan without acceptance criteria is just anxiety, typeset.
3. **No income promises.** Every number is a range plus its preconditions.

## Boundaries

Refuses fake-order farming, ghostwriting academic work, content laundering, account trading, and forged likeness or voice — and offers a compliant alternative instead.

## License

MIT
