# Anthropic requires 30 day data retention for Fable and Mythos

- Score: 605 | [HN](https://news.ycombinator.com/item?id=48464258) | Link: https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models

### TL;DR

Anthropic requires 30-day retention of prompts and outputs for Fable 5, Mythos 5, and future covered models to detect multi-request abuse including jailbreaks, espionage, and extortion. The change removes zero-data-retention treatment for Claude Console, Enterprise Claude Code, Bedrock, Google Cloud, and Azure deployments; consumer plans already retain safety data, while other models are unchanged. Access is restricted and logged, with exceptions for investigations or law. Hacker News saw this as incompatible with sensitive code and enterprise privacy promises, despite Anthropic’s no-training rule. Anthropic later suspended both models.

### Comment pulse

- A hard 30-day ceiling remains uncertain → investigations and legal holds permit longer retention, while coding agents may expose repositories and secrets.
- Enterprise trust becomes harder to explain → customers may reject covered models even when retained cloud data stays inside AWS or GCP.
- Safety rationale divided readers → cross-request abuse detection needs history — counterpoint: broad classifiers already downgrade benign medical, ML, and security work.

### LLM perspective

- **View:** Capability-gated retention trades stronger misuse detection for a weaker, more complex enterprise privacy boundary.
- **Impact:** ZDR customers must isolate covered-model workloads, revise disclosures, or choose less capable models for sensitive data.
- **Watch next:** Audit deletion exceptions, reviewer-access logs, cloud residency, false-positive rates, and the availability of covered models.
