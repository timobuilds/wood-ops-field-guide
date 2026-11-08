# Wood Operations Agentic Field Guide

![A beaver in lederhosen beside a cut log](assets/seppgmeiner.png)

This library extracts woodworking operations practices from Sepp Gmeiner’s articles in *Woodworking Canada* magazine and adapts them into instructions an AI agent can follow. Each specialist helps a team make one shop-floor decision. The [article map](ask-sepp/references/article-map.md) connects each procedure to its source.

**Remember:** This skill library is experimental. AI can make mistakes. For professional consulting on your operation, [contact Sepp Gmeiner](mailto:s.gmeiner@lignum-consulting.com).

## Install and try the guide

Download or clone this repository. The 17 folders containing a `SKILL.md` make up the guide. Keep each folder intact so its references and artwork travel with it.

| Agent | Setup |
|---|---|
| ChatGPT | If your workspace offers Skills, open **Plugins → Skills → Create → Upload from your computer**. Import the skills individually, starting with `ask-sepp`. If Skills is unavailable, use the manual method below. [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| Codex | Copy the 17 folders into your project’s `.agents/skills/` so the router is at `.agents/skills/ask-sepp/SKILL.md`. Open the project in Codex and invoke `$ask-sepp`. [Codex skills](https://developers.openai.com/codex/skills) |
| Cursor | Copy the folders into `.cursor/skills/`, or use the same `.agents/skills/` installation as Codex. Open the project in Cursor and ask Agent to use Ask Sepp. [Cursor skills](https://cursor.com/help/customization/skills) |
| Claude Code | Copy the folders into your project’s `.claude/skills/`. Start Claude Code in that project and enter `/ask-sepp` followed by your question. [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Claude.ai | Zip each skill folder separately, keeping the named folder and its contents together. Upload each archive through Claude’s Skills settings and enable the skills you want to use. [Claude skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) |

**Manual setup for other agents.** Any agent that can read Markdown can use these procedures. Give it the repository and ask it to follow `ask-sepp/SKILL.md`. In a chat without repository access, paste the router instructions, then paste the selected specialist’s instructions and any reference it requests.

Try asking “Use Ask Sepp. Assembly keeps waiting on missing doors. How do I find the first missed handoff?” Start with the [Ask Sepp router](ask-sepp/SKILL.md) or choose a specialist below.

## Specialists

- [benchmark-plants](benchmark-plants/SKILL.md)
- [build-skill-coverage](build-skill-coverage/SKILL.md)
- [check-job-readiness](check-job-readiness/SKILL.md)
- [cost-an-order](cost-an-order/SKILL.md)
- [decide-make-or-buy](decide-make-or-buy/SKILL.md)
- [design-layout](design-layout/SKILL.md)
- [evaluate-equipment](evaluate-equipment/SKILL.md)
- [improve-material-yield](improve-material-yield/SKILL.md)
- [plan-finishing](plan-finishing/SKILL.md)
- [read-plant](read-plant/SKILL.md)
- [reduce-defects](reduce-defects/SKILL.md)
- [review-scoreboard](review-scoreboard/SKILL.md)
- [run-lean-trial](run-lean-trial/SKILL.md)
- [schedule-constraint](schedule-constraint/SKILL.md)
- [set-direction](set-direction/SKILL.md)
- [simplify-order-engineering](simplify-order-engineering/SKILL.md)

Use the [routing checks](tests/routing.md) to exercise the package after editing it.
