# How Fast Does Claude, Acting as a User Space IP Stack, Respond to Pings?

- Score: 158 | [HN](https://news.ycombinator.com/item?id=48089049) | Link: https://dunkels.com/adam/claude-user-space-ip-stack-ping/

- TL;DR  
Adam Dunkels (creator of lwIP/uIP/Contiki) has Claude Code act as a full user‑space IPv4/ICMP stack. He gives Claude a Markdown “program” describing how to read raw packets from a TUN interface, parse headers, compute checksums manually, and emit ICMP echo replies. It works: `ping` receives a valid response with correct TTL and checksums—but with ~42.5 s round‑trip time. HN readers enjoy the demo as a clever, self‑aware abuse of LLMs, reinforcing that they’re educational toys here, not production networking tools.

- Comment pulse  
  - LLMs for IDS or packet handling → horribly inefficient versus BPF and kernel facilities; fun demo, but wheel‑reinvention if treated as real tooling.  
  - Knowing the author built lwIP/uIP/Contiki reframes this as an insider joke and teaching experiment about stacks, not naïve misuse.  
  - Likely future: LLMs handle natural‑language orchestration, while specialized models or MoE experts do perception and low‑level tasks—counterpoint: vision‑language models already blur that boundary.

- LLM perspective  
  - View: This treats prompts as a low‑level DSL and the LLM as a virtual CPU executing protocol “microcode.”  
  - Impact: Best applied to debugging, education, or interactive explanations of protocol behavior, not latency‑sensitive paths.  
  - Watch next: Experiments where LLMs emulate parsers, state machines, or bus protocols, with metrics on correctness versus computational cost.
