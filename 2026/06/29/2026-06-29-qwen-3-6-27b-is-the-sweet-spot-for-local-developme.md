# Qwen 3.6 27B is the sweet spot for local development

- Score: 549 | [HN](https://news.ycombinator.com/item?id=48721903) | Link: https://quesma.com/blog/qwen-36-is-awesome/

### TL;DR
HN folks like Qwen 3.6 27B as a capable “good enough” local coding model, but the supposed sweet spot—running it on a 128GB MacBook Pro—is heavily disputed. Commenters report severe heat/noise on laptops, argue for headless Mac minis or GPU workstations instead, and note that cloud options like DeepSeek or Qwen via OpenRouter are usually far cheaper and better. Qwen shines on simple, standard tasks; for large or unusual codebases, many still prefer top-tier cloud models.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Laptop as inference box → Sustained 27–35B runs make even high-end MacBooks uncomfortably hot/noisy; remote Mac minis/servers give better ergonomics and isolation — counterpoint: some find raised/externally‑connected MBPs acceptable.

- Economics split → $6k–7k 128GB MBP is far pricier than modest hardware plus years of API use; others treat it as a privacy-preserving, resale-friendly asset.

- Capability in “real work” → Qwen 3.6 27B handles small, standard projects and refactors well, but degrades on niche, long-context codebases and under aggressive quantization; many fall back to Claude/DeepSeek.

---

### LLM perspective
- View: For local tinkering and modest projects, 20–30B open models are a pragmatic ceiling before hardware, heat, and context issues dominate.

- Impact: Developers must choose: cheap, powerful cloud models with data risk, or expensive local rigs with slower iteration but full control.

- Watch next: Better 4–8-bit quantization, commodity 32–48GB VRAM desktops, and agent tooling that treats local models as headless services accessed from lighter clients.
