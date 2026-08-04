# Software is made between commits

- Score: 316 | [HN](https://news.ycombinator.com/item?id=48492533) | Link: https://zed.dev/blog/introducing-deltadb

### TL;DR

Zed’s DeltaDB proposes versioning every fine-grained edit, not just commits, and storing each delta beside the human-agent conversation that produced it. Stable delta identities let references survive moving code; conflict-free replicated worktrees allow concurrent human-agent editing across machines, while Git remains for CI and external interoperability. The beta is due within weeks. Hacker News split: supporters saw valuable agent context and live collaboration, while critics called intermediate work noisy private thinking, preferred curated atomic commits, and argued frequent Git commits plus first-parent views already preserve detail without creating workplace surveillance.

### Comment pulse

- Commit history has two jobs → curated atomic commits explain intent — counterpoint: frequent raw commits improve bisectability and preserve debugging evidence.

- Existing Git may suffice → auto-commits, no-fast-forward merges, and first-parent views retain granular history beneath a clean top-level narrative.

- Privacy is the fault line → agent context may improve future work — counterpoint: recording every operation invites intrusive employee surveillance.

### LLM perspective

- **View:** DeltaDB treats provenance as first-class data, but provenance value depends on deliberate retention and access boundaries.

- **Impact:** Teams could review agent decisions earlier, while managers gain a potentially coercive record of individual work formation.

- **Watch next:** Evaluate opt-in controls, redaction, storage cost, Git export fidelity, non-Zed tool capture, merge behavior, and review signal-to-noise.
