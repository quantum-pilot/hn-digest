# Claudette: Make Claude stop talking like a BuzzFeed article

- Score: 335 | [HN](https://news.ycombinator.com/item?id=49388752) | Link: https://github.com/adnanakil/nobuzz/blob/main/README.md

### TL;DR

A Claude Code skill called `/debuzz` sends Claude’s previous response to Gemini through Google’s Antigravity CLI, then prints the rewrite verbatim to avoid reintroducing Claude’s theatrical style. Modes target engineers, managers, or directors while preserving appropriate technical detail. Authentication failures surface directly, with Claude rewriting only as a labeled fallback. Commenters shared simpler remedies—strict word limits, active voice, and manual editing—but said long contexts erode instructions. Many blamed Anthropic’s persona and engagement-oriented prose for growing user irritation.

### Comment pulse

- Hard quantitative limits worked best for several users → caps on words, comment length, or added code reliably constrained verbosity.
- Prompt-only controls were fragile → long contexts caused style rules to fade, pushing users toward hooks, repeated instructions, or manual cleanup.
- Persona criticism dominated → readers disliked praise, moralizing, suspense, and thought-leader framing despite valuing Claude’s coding ability.

### LLM perspective

- View: A second-model rewrite is practical middleware, but treats presentation symptoms instead of fixing the producing model’s style control.
- Impact: Teams gain audience-specific brevity while adding authentication, latency, another provider, and another opportunity to distort technical facts.
- Watch next: Meaning-preservation tests, code-block fidelity, latency and token costs, privacy review, and first-party output-style controls.
