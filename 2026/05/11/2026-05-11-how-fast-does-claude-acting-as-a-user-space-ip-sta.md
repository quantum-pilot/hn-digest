# How Fast Does Claude, Acting as a User Space IP Stack, Respond to Pings?

- Score: 158 | [HN](https://news.ycombinator.com/item?id=48089049) | Link: https://dunkels.com/adam/claude-user-space-ip-stack-ping/

### TL;DR

Adam Dunkels asked Claude Code to behave as a user-space IPv4/ICMP stack: read a raw packet from a TUN helper, parse headers byte by byte, swap addresses, convert echo request to reply, calculate both checksums without scripts, and write the hex packet back. Haiku 4.5 succeeded, returning a valid ping in about 42.6 seconds. The experiment demonstrates Markdown as executable procedure and an LLM as an absurdly slow processor, not a practical stack. Commenters treated the result as playful boundary testing rather than a practical architecture.

### Comment pulse

- Readers noted Dunkels created lwIP, uIP, and Contiki, making the deliberately inefficient experiment an informed inversion of his usual work.
- An engineer rejected LLM-based intrusion detection for BPF — counterpoint: language models may still structure user intent before specialized processing.
- Comparisons ranged from CPU branch-prediction jokes to RFC 1149’s avian-carrier ping, emphasizing entertainment over performance.

### LLM perspective

- View: LLMs can execute precise low-level procedures, but latency and nondeterminism dominate when symbolic tools already fit.
- Impact: The demo clarifies where agents should orchestrate deterministic components rather than impersonate them.
- Watch next: Repeatability, checksum error rates, model comparisons, tool-assisted variants, token cost, and more complex protocols.
