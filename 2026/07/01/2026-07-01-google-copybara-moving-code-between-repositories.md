# Google copybara: moving code between repositories

- Score: 290 | [HN](https://news.ycombinator.com/item?id=48740698) | Link: https://github.com/google/copybara

### TL;DR
Google’s Copybara is a configurable tool for moving/synchronizing code between repositories, especially from large internal monorepos to external Git repos. It rewrites commits while preserving blame information and can apply complex path and content transforms, though bidirectional syncing becomes fragile. HN commenters compare it with older and newer sync tools, discuss adding Perforce-like support and Google’s internal review stack, debate whether it’s worth using for small code-sharing vs just extracting libraries, and note the long history of “copy” utilities back to mainframes.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Tool ecosystem → Rust’s Josh, git subtree, Meta’s fbshipit, and hackathon projects add generative or opinionated transforms—counterpoint: fragmentation makes cross-company workflows and documentation harder.  
- Usage pattern → Best fit is exporting slices of large monorepos to OSS; using it as lightweight folder-sync between small repos feels tedious and config-heavy.  
- History and workflow → One-way exports cherry-pick commits, storing original SHAs in trailers; Google reviews those changes in Critique, not Gerrit/GitHub.  

---

### LLM perspective
- View: Tools like Copybara formalize code “copying” as a first-class workflow, acknowledging that perfect modularization and dependencies are often impractical.  
- Impact: Large orgs with monorepos gain robust OSS syncs and compliance; tiny teams may over-invest versus simpler scripts or subtrees.  
- Watch next: semantic-aware transforms, automatic conflict resolution, and standardized metadata for cross-repo history mapping could make bidirectional syncing less brittle.
