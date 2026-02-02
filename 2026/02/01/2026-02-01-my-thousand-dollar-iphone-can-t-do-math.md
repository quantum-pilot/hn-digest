# My thousand dollar iPhone can't do math

- Score: 80 | [HN](https://news.ycombinator.com/item?id=46849258) | Link: https://journal.rafaelcosta.me/my-thousand-dollar-iphone-cant-do-math/

TL;DR  
An iOS developer tried to build an on-device expense classifier using Apple’s LLM tooling. Apple Intelligence never finished enabling on an iPhone 16 Pro Max, so they switched to MLX-based local models, which produced gibberish while the same code and models worked flawlessly on an iPhone 15 Pro and a Mac. By logging intermediate tensors, they showed identical inputs but wildly different activations only on that 16, implicating a defective Neural Engine or ML stack. A replacement iPhone 17 Pro Max worked fine.

Comment pulse  
- Initial skepticism about “vibe-coded” debugging → author reimplemented without LLM help and diffed layer outputs; only this phone diverged dramatically from 15 Pro and Mac.  
- Known: low‑level FP ops aren’t bit‑reproducible → commenters argue order‑of‑magnitude differences plus Apple’s own LLM failing implies a real bug, not numeric jitter.  
- Some readers expected a “LLMs can’t do math” rant or calculator nostalgia; others stress it’s actually a case study in ML hardware failure diagnostics.

LLM perspective  
- View: Rare accelerator faults will increasingly show up only under ML workloads; logs and cross‑device comparisons become essential debugging tools.  
- Impact: Developers may misattribute such issues to models or code, wasting days; users see broken AI features and lose trust.  
- Watch next: Whether Apple exposes Neural Engine diagnostics, fixes Apple Intelligence downloads, or documents MLX/A18 quirks affecting inference reliability.
