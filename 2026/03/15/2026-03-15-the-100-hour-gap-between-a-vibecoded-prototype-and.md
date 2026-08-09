# The 100 hour gap between a vibecoded prototype and a working product

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47386636) | Link: https://kanfa.macbudkowski.com/vibecoding-cryptosaurus

### TL;DR

Cryptosaurus went from AI-generated prototype to production in roughly 100 hours, revealing where “30-minute app” claims stop. Most effort went into UI refinement, more than 200 image-prompt trials, cloud and Farcaster setup, contract permissions, rate limits, and a launch-time nonce collision that required refunds. The finished mini-app reached 1,000-plus downloads and 180-plus purchases. HN broadly recognized rapid proof-of-concept gains, but said verification, security, workload testing, architecture, and accumulated shortcuts reduce mature-system acceleration to perhaps two or three times.

### Comment pulse

- Early shortcuts compound hidden debt → later symptoms often originate several layers back, making deliberate design checkpoints valuable.
- Front-load architecture and visual design → clear specifications improve generation — counterpoint: coding itself is often how developers discover the problem.
- Production value depends on domain expertise → deterministic tests and read-only observability help, while hot-path infrastructure suggestions demand skepticism.

### LLM perspective

- **View:** Agents compress implementation more reliably than discovery, validation, or accountability.
- **Impact:** Builders become reviewers and coordinators; senior judgment moves earlier and remains necessary at launch.
- **Watch next:** Measured delivery time across comparable projects, escaped-defect rates, maintenance cost, and production incidents.
