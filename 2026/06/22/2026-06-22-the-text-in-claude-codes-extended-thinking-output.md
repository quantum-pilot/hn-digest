# The text in Claude Code’s “Extended Thinking” output

- Score: 265 | [HN](https://news.ycombinator.com/item?id=48630535) | Link: https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/

### TL;DR

The post finds that Claude Code session logs store encrypted reasoning signatures, while Ctrl+O and the API expose only summaries; Anthropic retains the key, and full thinking reportedly requires an enterprise agreement. Therefore, the displayed text cannot serve as a faithful audit trail of what drove an agent’s actions, though inputs, outputs, and actions can still be logged. HN commenters agreed hidden chain-of-thought is common across major vendors, debating whether it primarily protects against distillation, conceals unsafe behavior, or creates security risk; several noted tool calls remain externally visible.

### Comment pulse

- Hidden reasoning protects competitive advantage → vendors prevent rivals from distilling proprietary traces — counterpoint: opacity makes products less auditable and harder to optimize.

- Prompt injection could exploit unseen reasoning → critics fear concealed objectives or exfiltration — counterpoint: client-executed tool calls remain visible outside encrypted blocks.

- Chain-of-thought is not a human-style explanation → commenters observed illegible intermediate text can look alarming or wrong yet still yield correct answers.

### LLM perspective

- **View:** A reasoning summary is telemetry, not provenance; auditability must come from observable state transitions, permissions, and reproducible execution records.

- **Impact:** Teams relying on Claude Code for regulated work need separate action logs and should avoid claims of decision-level traceability.

- **Watch next:** Compare documentation, export formats, enterprise access terms, tool-call visibility, token accounting, and independent tests of encrypted-block behavior.
