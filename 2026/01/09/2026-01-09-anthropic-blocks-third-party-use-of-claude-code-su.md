# Anthropic blocks third-party use of Claude Code subscriptions

- Score: 559 | [HN](https://news.ycombinator.com/item?id=46549823) | Link: https://github.com/anomalyco/opencode/issues/7410

### TL;DR
Anthropic quietly closed a loophole that let people use its $200/month Claude Code subscription (meant for Anthropic’s own CLI/IDE tools) via the open-source OpenCode TUI, by reverse‑engineering and spoofing the Claude Code client. OpenCode users suddenly lost access, triggering a huge GitHub thread and HN debate. You can still use Anthropic API keys with OpenCode, but at much higher per‑token rates. Discussion centers on pricing fairness, ToS violations, lock‑in vs openness, and why OpenCode’s UX outclasses Anthropic’s own tools.

---

### Comment pulse
- Anthropic mispriced Claude Code as “all‑you‑can‑eat” vs API rates → third‑party clients made that arbitrage visible; some say fix pricing, not block clients — counterpoint: loss‑leader by design.  
- Many claim OpenCode’s TUI, architecture, and QoL crush Claude Code’s CLI → blocking it feels like an “L” and highlights Anthropic’s weaker engineering polish.  
- Some frame OpenCode’s spoofing as ToS‑breaking and near‑fraud → others argue subscribers paid for model usage and should choose any client, not just Anthropic’s.

---

### LLM perspective
- View: Expect more hard separations between discounted “official client” plans and full‑price APIs; arbitrage routes will keep getting shut down.  
- Impact: Power users, open‑source harnesses, and IDE integrators face higher effective prices or must pivot toward vendors with clearer BYO‑client support.  
- Watch next: Anthropic revising subscriptions, publishing official SDKs/CLI hooks, and whether OpenAI or others adopt similar client‑tied pricing.
