# Cursor removed cost information from the usage page and CSV export

- Score: 294 | [HN](https://news.ycombinator.com/item?id=49135257) | Link: https://forum.cursor.com/t/usage-page-to-token-amount-what/167153

### TL;DR

Cursor intentionally stopped showing dollar equivalents for included usage on individual plans, arguing that API-rate figures exceeded subscription prices and confused users. Token counts now mark covered activity as Included; actual on-demand charges remain in Dashboard Spending and paid CSV rows. A separate CSV regression was accidental and reportedly fixed. HN users saw reduced visibility as hostile to budgeting, especially after another cost indicator disappeared. Discussion broadened to agent efficiency: identical tasks reportedly consumed dramatically different token totals across harnesses, making transparent per-session measurement important even when usage is bundled.

### Comment pulse

- Billing clarity has two meanings → Cursor shows payable charges, while users also want opportunity-cost and model-efficiency estimates for included usage.
- Harness overhead can dominate → one ten-task comparison ranged from 172,807 to 5,073,137 tokens, prompting calls for traces and tool-context audits.
- Switching remains easy → Cursor’s IDE integration and multi-model access retain fans — counterpoint: VS Code plus agent extensions now competes strongly.

### LLM perspective

- **View:** Removing confusing numbers is defensible only if a clearer equivalent preserves user control and comparability.
- **Impact:** Individual users lose early warning about expensive model choices; teams need independent usage telemetry.
- **Watch next:** Track CSV stability, session-level cost indicators, token-to-dollar calculators, context pruning, and churn toward editor-neutral agents.
