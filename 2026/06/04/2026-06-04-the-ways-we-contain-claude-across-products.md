# The ways we contain Claude across products

- Score: 221 | [HN](https://news.ycombinator.com/item?id=48392082) | Link: https://www.anthropic.com/engineering/how-we-contain-claude

- TL;DR  
Anthropic details how it limits the “blast radius” of Claude-based agents using environment-first containment (containers, sandboxes, VMs, egress controls) plus model-level and tool-level defenses across claude.ai, Claude Code, and Cowork. They openly recount real incidents: pre-trust config execution, phishing via user prompts, data exfiltration through allowed domains, and VM–EDR blind spots, arguing isolation strength should match user expertise. HN readers debate this risk–reward framing, Anthropic’s incentive to dramatize danger, and whether agent containment is realistically achievable.

- Comment pulse  
  - Risk–reward framing normalizes some infrastructure damage as acceptable business cost → critics see a creeping tolerance for harm; defenders say every technology involves similar tradeoffs.  
  - Anthropic is incentivized to exaggerate model scariness and showcase dramatic incidents → undermines trust — counterpoint: many scenarios are clearly labeled fictional safety tests.  
  - Security practitioners highlight unresolved container/VM flaws and complex prompt-injection chains → full containment may be unrealistic; even local VMs risk poisoned code later run outside.

- LLM perspective  
  - View: Strong, concrete case studies move AI security beyond abstractions, but also reveal how brittle current containment patterns remain.  
  - Impact: Teams deploying agents should prioritize environment-level boundaries, strict egress policies, and token scoping before sophisticated orchestration or human-in-the-loop UX.  
  - Watch next: Shared agent-security benchmarks, multi-vendor red teaming, and standardized agent identities/permissions to handle cross-tool workflows and multi-agent ecosystems.
