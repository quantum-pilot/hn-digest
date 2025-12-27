# FFmpeg has issued a DMCA takedown on GitHub

- Score: 485 | [HN](https://news.ycombinator.com/item?id=46394327) | Link: https://twitter.com/FFmpeg/status/2004599109559496984

### TL;DR
FFmpeg filed a DMCA takedown on GitHub against a Rockchip-related repository that had copy‑pasted FFmpeg code, removed or obscured LGPL licensing, and claimed the result was Apache 2.0. Commenters clarify that LGPL does not forbid static linking per se, but it does forbid relicensing third‑party code under incompatible terms. The thread branches into questions about mixing licenses, how to correctly ship modified LGPL code, and whether AI code generation risks similar hidden copyright violations.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse

- Main issue → Repo allegedly copied FFmpeg code, removed LGPL headers, and relicensed as Apache 2.0; LGPL doesn’t mandate dynamic linking, only replaceability and proper licensing. — counterpoint: Some still conflate LGPL with a strict “dynamic linking only” rule.

- Correct approach → Vendor should have kept FFmpeg as a clearly LGPL fork or library and linked to it, instead of mixing sources into proprietary code.

- AI angle → Some worry code‑gen tools will unknowingly reproduce copyrighted snippets; others argue LLMs rarely emit verbatim code and law hinges on substantial, obvious copying.

---

### LLM perspective

- View: This shows open‑source projects can and will use DMCA to enforce licenses when vendors silently appropriate and relicense code.

- Impact: SoC vendors, firmware teams, and GitHub-hosted SDKs will need tighter license compliance and clearer separation of third‑party code.

- Watch next: More automated license scanning, clearer guidance for LLM code tools, and potential test cases around AI-generated derivatives of LGPL/GPL code.
