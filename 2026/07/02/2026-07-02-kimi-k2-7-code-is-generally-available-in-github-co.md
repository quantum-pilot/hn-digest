# Kimi K2.7 Code is generally available in GitHub Copilot

- Score: 396 | [HN](https://news.ycombinator.com/item?id=48756602) | Link: https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/

### TL;DR

GitHub has made open-weight Kimi K2.7 Code the first such model selectable in Copilot. GitHub hosts it on Azure and bills at provider list prices; rollout begins gradually for Pro, Pro+, and Max across IDEs, CLI, cloud agent, web, mobile, and Xcode, with Business and Enterprise later. Organizational access is disabled by default pending administrator review of security, compliance, and governance. HN welcomed a trusted-host option for Chinese models but focused on Copilot’s recent usage-price increases, disputed Sonnet-level benchmark claims, and contrasted cloud churn with stable local Qwen setups.

### Comment pulse

- Pricing overwhelmed product gains → users report monthly allowances disappearing in days or prompts, driving teams from Copilot toward Claude Code, Codex, Bedrock, and DeepInfra.
- Benchmark parity remains unproven → one user saw Kimi loop where Claude succeeded — counterpoint: the served version may have been a degraded quantization.
- Harness choice changes model value → prompts, tools, subagent routing, caching, and context overhead can outweigh raw model quality or token price.

### LLM perspective

- **View:** The strategic milestone is distribution, not demonstrated superiority: open-weight models now enter a mainstream managed enterprise control plane.
- **Impact:** GitHub gains leverage on model cost and choice; Moonshot gains reach without enterprises operating unfamiliar inference infrastructure.
- **Watch next:** Compare production coding tasks, reasoning loops, latency, cache rates, total spend, data handling, and Business-policy rollout quality.
