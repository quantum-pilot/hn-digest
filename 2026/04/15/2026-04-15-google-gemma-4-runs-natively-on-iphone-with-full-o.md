# Google Gemma 4 Runs Natively on iPhone with Full Offline AI Inference

- Score: 265 | [HN](https://news.ycombinator.com/item?id=47774971) | Link: https://www.gizmoweek.com/gemma-4-runs-iphone/

### TL;DR
Google’s Gemma 4 LLM family now runs fully offline on iPhones via the Google AI Edge Gallery app, using the GPU for local inference. The 31B model benchmarks near Qwen 3.5 27B, but mobile-focused 2B/4B variants are the practical choice due to memory and thermal limits. The app supports text, vision, voice, and an extensible “Skills” system, positioning it as an on-device AI platform. HN debates GPU vs Apple Neural Engine, App Store policy friction, and the article’s content-farm feel.

---

### Comment pulse
- GPU-only inference on iPhone → Metal is easier to target but drains battery; ANE is hard to program and poorly supported for LLMs today.  
- On-device apps blocked? → Some devs hit App Store rule 2.5.2 with local LLMs; others report similar apps approved—counterpoint: enforcement is inconsistent, not absolute.  
- Real-world tinkering → Hackers built offline coding assistants using Gemma 4B/2B on iPhone, but memory limits and App Store review make them side-loaded experiments.

---

### LLM perspective
- View: This normalizes multi-billion-parameter models as “just another mobile workload,” not a cloud-only capability.  
- Impact: Mobile devs gain a serious, privacy-preserving LLM baseline without API costs, especially for tools, note-taking, and niche vertical apps.  
- Watch next: ANE/Core AI support, energy/performance benchmarks vs cloud, and whether Apple relaxes or tightens policies on bundled local models.
