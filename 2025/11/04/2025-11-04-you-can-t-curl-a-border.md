# You can't cURL a Border

- Score: 445 | [HN](https://news.ycombinator.com/item?id=45806263) | Link: https://drobinin.com/posts/you-cant-curl-a-border/

### TL;DR

Vadim Drobinin describes Residency, an on-device travel linter built from a decade-long trip ledger. It simulates proposed journeys against jurisdiction-specific day counting, rolling windows, tax presence, visa, passport, and driving-permit rules. Facts are stored as instants, evaluated in each jurisdiction's local days, and interpreted through versioned rule definitions so earlier answers remain reproducible. The author rejects cloud sync to avoid retaining sensitive movement data. Commenters admired the edge-case work but questioned testing, marketing emphasis, and one stated British citizenship timing rule.

### Comment pulse

- A commenter claimed the citizenship look-back date depends on Home Office receipt, not submission; the thread treated the rule as uncertain.
- Readers emphasized exhaustive unit tests and editable rule definitions for trustworthy date calculations.

### LLM perspective

- View: Treating travel compliance as versioned simulation is stronger than offering an unexplained “you're fine.”
- Impact: Local processing reduces disclosure while surfacing conflicts before a traveler buys a difficult itinerary.
- Watch next: Test coverage, provenance updates, conflicting official guidance, timezone revisions, and user-configured rule accuracy.
