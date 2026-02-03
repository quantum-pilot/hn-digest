# Apple's MacBook Pro DFU port documentation is wrong

- Score: 191 | [HN](https://news.ycombinator.com/item?id=46852096) | Link: https://lapcatsoftware.com/articles/2026/2/1.html

- TL;DR  
  Jeff Johnson describes repeated failures updating macOS on an external SSD attached to an M4 Pro MacBook Pro. Apple’s docs say external‑disk installs must avoid the DFU port and that, for his model class, this port is on the left; on his machine, only a right‑side port behaves like DFU. Moving the SSD to the other side fixed updates. HN debates whether docs or diagnosis are wrong, but mostly blames hour‑long, silent update rollbacks with no actionable errors.

- Comment pulse  
  - DFU docs likely correct → experienced users say only the documented port is valid; similar behavior on others is unsupported, not evidence the docs are wrong.  
  - Real issue is UX → macOS spends an hour “updating,” silently rolls back, and surfaces no hint that port choice or security policy blocked success.  
  - DFU design explained → boot ROM handles one USB‑C port for simplicity; extra ports complicate code — counterpoint: others say DFU isn’t involved in installs.

- LLM perspective  
  - View: Reliance on undocumented port semantics makes recovery and updates brittle; tools should label DFU ports and disallow risky setups.  
  - Impact: Power users, IT, and developers lose time debugging opaque failures, undermining confidence in macOS as a dependable professional platform.  
  - Watch next: Whether Apple revises DFU docs and adds preflight checks or clearer logs for external‑disk installs and security‑policy problems.
