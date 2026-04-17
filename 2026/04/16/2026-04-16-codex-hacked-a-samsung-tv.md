# Codex Hacked a Samsung TV

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47791212) | Link: https://blog.calif.io/p/codex-hacked-a-samsung-tv

- TL;DR  
Researchers built a controlled environment where OpenAI’s Codex, starting from a browser shell on a Samsung smart TV and given matching firmware source, autonomously escalated to root. Codex enumerated drivers, discovered a Novatek ntksys kernel interface that let user space map arbitrary physical memory, validated it via helper tools, then located and patched the browser process’s cred structure in RAM to become root. HN readers highlight AI’s growing role in reverse‑engineering consumer devices and debate open vs closed-source security implications.

- Comment pulse  
  - AI assistants help users reverse‑engineer router and IoT APIs → quicker creation of custom clients and metrics, though DMCA anti‑circumvention laws may chill sharing techniques.  
  - Commenters stress Codex had full firmware source → question whether closed‑source truly slows AI‑driven vuln discovery, noting binaries can be decompiled or sometimes aren’t extractable.  
  - Many dislike fragile, laggy “smart” TV software → would prefer tools or hacks that disable online features and leave a reliable, monitor‑like display.

- LLM perspective  
  - View: AI wasn’t magic here; it acted as a tireless junior exploit developer once given scaffolding, feedback, and clear objectives.  
  - Impact: Security teams must assume attackers can cheaply automate post‑exploitation workflows, shrinking the skill gap needed to weaponize obscure driver bugs.  
  - Watch next: Track experiments where AI finds initial footholds, plus integration into fuzzers and Ghidra‑like tools for end‑to‑end exploit pipelines.
