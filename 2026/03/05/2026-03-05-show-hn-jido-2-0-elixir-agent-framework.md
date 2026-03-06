# Show HN: Jido 2.0, Elixir Agent Framework

- Score: 229 | [HN](https://news.ycombinator.com/item?id=47263036) | Link: https://jido.run/blog/jido-2-0-is-here

## TL;DR

Jido 2.0 is an Elixir/BEAM-first agent framework that treats agents as pure data plus a single cmd/2 function, with side effects modeled as directives. A supervised GenServer runtime, pluggable strategies (Direct, FSM, ReAct, CoT, etc.), and separated packages for actions (jido_action) and signaling (jido_signal) enable testable, fault-tolerant, multi-agent systems. Jido AI, built on ReqLLM, adds LLM reasoning on top. HN commenters praise the BEAM fit, robustness focus, and see parallels with OpenAI’s Symphony.

## Comment pulse

- BEAM seems ideal for agents but perceived ecosystem immaturity slowed adoption; Jido 2.0’s ecosystem and tooling may change that — counterpoint: website/docs glitches (404s, escaping) hurt first impressions.  
- Robustness focus resonates: pure agent state plus checkpointing across nodes counters misconceptions about Elixir location transparency and helps survive node failures and rolling deploys.  
- Developers tired of bespoke GenServer/Oban agent orchestration welcome Jido as a cleaner abstraction; OpenAI’s Symphony is viewed as a convergent, validating design.  

## LLM perspective

- View: Modeling agents as serializable data plus a pure cmd loop is a strong pattern for testable, debuggable AI systems.  
- Impact: Elixir teams gain a coherent path from classic OTP to AI agents without reinventing orchestration primitives.  
- Watch next: Comparative throughput/fault-tolerance benchmarks and production case studies versus frameworks like LangGraph and Symphony.
