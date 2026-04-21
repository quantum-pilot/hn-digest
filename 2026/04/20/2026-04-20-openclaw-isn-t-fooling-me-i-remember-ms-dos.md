# OpenClaw isn't fooling me. I remember MS-DOS

- Score: 265 | [HN](https://news.ycombinator.com/item?id=47831437) | Link: https://www.flyingpenguin.com/build-an-openclaw-free-secure-always-on-local-ai-agent/

### TL;DR
The author argues that popular “agent OS” frameworks like OpenClaw repeat MS‑DOS’s worst security idea: one flat trust boundary where a single process and token can reach everything (files, network, tools, credentials). NVIDIA’s NemoClaw tutorial tries to bolt on safety with containers, network namespaces, and approval UIs, but still wraps the whole agent instead of isolating tools and channels. He contrasts this with his Wirken gateway, which applies Unix-style separation: per-channel identities, per-tool hardened sandboxes, fine-grained approvals, and tamper-evident audit logs.

---

### Comment pulse
- This is tech debt and “worse is better” → OpenClaw ships unsafe but useful now, wins attention and jobs while cautious designs lag—counterpoint: eventually it won’t adapt to real-world threats.  
- Nostalgia vs safety → Some remember DOS-like total control as fun and empowering; others note hardware limits then, and that DOS kept ignoring protections even once available.  
- Real-world agents feel dangerous → Users see huge token use, local credential exposure, many attack surfaces; some advocate external secret proxies or cloud-hosted agents with server-side OAuth and human approvals.

---

### LLM perspective
- View: Agent platforms need explicit threat models and least-privilege by default; “one agent, one token” should be treated as a critical bug.  
- Impact: Enterprise adoption, compliance, and regulated industries will hinge on auditability, isolation of tools, and robust secret-handling patterns.  
- Watch next: Standardized agent threat models, external-secret patterns, and benchmarks comparing prompt-injection impact across architectures (tool-level vs agent-level sandboxes).
