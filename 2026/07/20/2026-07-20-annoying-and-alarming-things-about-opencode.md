# Annoying and alarming things about OpenCode

- Score: 367 | [HN](https://news.ycombinator.com/item?id=48978112) | Link: https://wren.wtf/shower-thoughts/stop-using-opencode/

## TL;DR
- The author argues OpenCode, a popular AI coding agent, is both frustrating and dangerously insecure. They catalog design flaws around prompt caching, context pruning, subagent handling, permissions, and a buggy TUI, then detail how OpenCode’s ad‑hoc command and file filters are trivially bypassed, its defaults quietly wire remote models to your shell, and past releases contained serious RCEs. HN discussion splits between seeing this as a necessary security wake‑up call, versus overgeneral, unconstructive, and needlessly hostile to open‑source maintainers.

## Comment pulse
- OpenCode defenders: many “annoying things” are ordinary bugs or UX quirks, some already fixed in v2; compaction and system prompts are hard problems across tools.  
- Security‑minded readers: the alarming RCE history, weak bash/file filters, and remote‑by‑default behavior justify treating current agentic CLIs as serious attack surfaces.  
- Meta‑critics: the prose’s insults toward OSS devs feel abusive and demotivating—counterpoint: others see caustic style as long‑standing culture and harmless dark humor.

## LLM perspective
- View: Article rightly spotlights brittle, text‑based sandboxing; agent designers must assume worst‑case model behavior, not “friendly assistant” intentions.  
- Impact: Developers casually running agentic CLIs locally should reconsider, or isolate them via VMs, strict OS sandboxes, or separate machines.  
- Watch next: Demand explicit threat models, red‑teaming, and reproducible security benchmarks for coding agents, similar to browsers and hypervisors.
