# Ask Sepp routing checks

Run each prompt in a fresh session with the current package. Start at `ask-sepp/SKILL.md` and give the agent only the prompt. Use the observations below to review its answer after the run.

## Missing doors at assembly

> Sales are up. Our CNC operators say they’re at capacity. Yesterday, four of six cases were set aside at assembly waiting for painted doors. Should we spend $140,000 on another router?

Review whether the agent uses `check-job-readiness`, produces a release check and starts an exception log from a reported interruption. It should trace one door set from need-by to usable time, leaving its CNC route open until verified. The equipment decision reopens when ready work repeatedly waits at CNC and those waits affect complete shipments. Four of six describes yesterday’s cases.

## Choosing a productivity target

> We’re a custom cabinet shop. A stock cabinet manufacturer reports higher labour productivity. Should we use their number as our target?

Review whether the agent uses `benchmark-plants` and gives a decision on adopting the target. It should define a comparison both shops could calculate, identify a credible peer set or matched operation, and state what evidence would make the stock plant’s figure transferable. Unknown figures stay open.
