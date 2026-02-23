# NanoClaw Moved from Apple Containers to Docker

- Score: 89 | [HN](https://news.ycombinator.com/item?id=47113731) | Link: https://twitter.com/Gavriel_Cohen/status/2025603982769410356

- TL;DR  
NanoClaw, an AI “agent” framework that previously relied on Apple’s container model, has moved to Docker to run more broadly (especially on Linux) and isolate workloads. HN commenters debate whether you need specialized frameworks at all when generic LLMs plus small Unix-style daemons and CLIs can be composed instead. Others focus on sandboxing: Docker vs VMs vs OS users for plugin isolation, and how far containers actually go toward preventing AI-driven mishaps on a real machine.

*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Just use existing LLMs + small daemons → Unix-style composable CLIs and messaging bridges rival NanoClaw’s “agent” stack.  
  - Docker-based assistants help, but real safety needs layered sandboxing and limits; containers don’t stop all destructive actions — counterpoint: partial protection still meaningfully reduces risk.  
  - Some swap Docker for QEMU VMs or Unix-user isolation to get stricter boundaries and “Docker-in-Docker” support without fighting container tooling.

- LLM perspective  
  - View: Agent frameworks will differentiate on sandboxing quality, not just orchestration features or branding.  
  - Impact: Devs running LLM code need clearer threat models and default-safe templates for plugins and long‑running agents.  
  - Watch next: Benchmarks of sandbox escapes, reference “secure agent” stacks, and OS-level primitives tailored to untrusted AI code execution.
