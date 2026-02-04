# Deno Sandbox

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46874097) | Link: https://deno.com/blog/introducing-deno-sandbox

- TL;DR  
  - Deno Sandbox is a hosted Linux microVM service for running untrusted (often LLM-generated) code with strict controls over network egress and API-key exposure. Secrets appear only as placeholders inside the VM and are swapped at an outbound proxy when calling approved hosts, while allow-lists block other destinations. Sandboxes support volumes/snapshots and one-step promotion to Deno Deploy. HN discussion centers on how robust the secret-substitution model really is and how this compares to other sandbox offerings.

- Comment pulse  
  - Secret placeholders limit permanent key theft but not misuse; main risks are reflection on allowed hosts and subtle gaps in substitution or allow-lists.  
  - Several suggest context-aware proxies that inject credentials (like Fly Tokenizer) as safer, though they still must handle edge cases and protocol diversity.  
  - Developers note a Python SDK and WebSocket-based protocol, plus a crowded sandbox market; some prefer DIY on cloud VMs—counterpoint: managed services bundle scaling and security.

- LLM perspective  
  - View: Treats LLM-generated code as hostile yet useful, emphasizing least-privilege networking and non-exfiltrable secrets over traditional plugin isolation.  
  - Impact: Enables multi-tenant AI agents and user-code platforms for smaller teams that can’t build microVM and proxy infrastructure themselves.  
  - Watch next: Formal threat analyses, red-team reports, and solutions for non-HTTP protocols (databases, raw TCP) using similar secret-handling guarantees.
