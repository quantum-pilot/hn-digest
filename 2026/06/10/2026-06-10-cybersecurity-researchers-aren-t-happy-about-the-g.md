# Cybersecurity researchers aren't happy about the guardrails on Anthropic's Fable

- Score: 587 | [HN](https://news.ycombinator.com/item?id=48478969) | Link: https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/

## TL;DR
Anthropic’s new Claude Fable 5 exposes the tension between AI safety and usefulness. Fable is a public, restricted version of the Mythos cybersecurity model whose aggressive cyber/bio guardrails frequently reject benign tasks and automatically downgrade to Claude Opus, frustrating security, bio, and ML researchers. Critics say keyword-based filters cripple real work, can be abused by malware to blind AI scanners, and quietly alter service quality and billing. After backlash, Anthropic pledged clearer downgrade signaling but kept tight controls and a gated “Cyber Verification” track.

## Comment pulse
- Overbroad guardrails hurt legitimate work → benign code reviews, logs, and ML research get blocked; silent model downgrades feel like sabotage and undermine commercial trust.  
- Guardrails don’t stop serious attackers → malware embeds prompts to trip scanners; criminals can switch to weaker/local models—counterpoint: still raises barriers for unsophisticated users.  
- Policy reversals and data retention worries → quick walk‑back seen as temporary; 30‑day retention on Fable/Mythos complicates “we don’t train on your data” promises.  

## LLM perspective
- View: Safety classifiers must be precise; blunt keyword filters create false positives and new attack surfaces like guardrail‑dodging malware.  
- Impact: Security, bio, and ML researchers need predictable behavior; opaque downgrades make Fable risky as infrastructure despite technical strength.  
- Watch next: Independent red‑teaming of guardrails, transparent downgrade APIs, and standardized “verified practitioner” schemes across vendors.
