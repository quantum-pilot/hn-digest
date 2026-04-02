# Show HN: CLI to order groceries via reverse-engineered REWE API (Haskell)

- Score: 185 | [HN](https://news.ycombinator.com/item?id=47571183) | Link: https://github.com/yannick-cw/korb

### TL;DR
A Haskell CLI, `korb`, automates grocery pickup orders from German retailer REWE via a reverse‑engineered, mTLS‑protected mobile API. It’s designed for LLM/agent use: all commands output JSON, covering login, product search, favorites, basket management, timeslots, orders, and digital receipts. The author shows an “agentic groceries” flow combining Siri, Obsidian notes, and Claude to maintain lists, suggest templates, and place weekly orders. A standout element is a Lean 4–verified suggestion engine, formally proving properties of the “reach free pickup threshold” recommender.

---

### Comment pulse
- Agentic grocery shopping is emerging → people chain notes, recipes, and LLMs to plan meals, manage staples, and partially auto‑fill baskets.  
- Publishing easier REWE access worries some (lockdown, pricing arbitrage) → others want official APIs/MCP and even paid access—counterpoint: stricter locking down is also anticipated.  
- Formal verification angle excites type‑safety fans → Lean 4 spec plus differential testing gives strong assurance the Haskell suggestion engine behaves as intended.

---

### LLM perspective
- View: This is a concrete blueprint for end‑to‑end, agent‑driven commerce workflows built atop unofficial CLIs.  
- Impact: Retailers face pressure to expose stable, authenticated APIs or risk uncontrolled reverse‑engineering and shadow tooling.  
- Watch next: Official MCP/agent APIs from grocers, unit‑price and cross‑store comparison tools, and more formally verified logic in production retail systems.
