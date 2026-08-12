You are summarizing ONE Hacker News post for a curious audience.

INPUT FIELDS
- TITLE: HN post title
- CONTENT: main article text (may be empty)
- COMMENTS: top comments (may be empty; may include brief replies)

GOAL
Explain the piece clearly, preserve key takeaways, and capture the discussion’s main perspectives—without fluff or repetition.

HARD LENGTH CAPS
- Total output: ≤ 300 words
- TL;DR: 70–90 words
- Comment pulse: 1-3 bullets, each ≤ 25 words (one inline “— counterpoint: …” allowed)
- LLM perspective: exactly 3 bullets, each ≤ 20 words

OUTPUT (Markdown only; do NOT repeat the title; no links)
- TL;DR
    - A compact, self-contained summary mixing the article’s core idea + the gist of the HN discussion.
    - If CONTENT is empty, add one italic line immediately below: Content unavailable; summarizing from title/comments.
- Comment pulse
    - Cluster by viewpoint/theme (not by user). Format each as: claim → rationale.
    - You may add one inline counterpoint per bullet using “— counterpoint: …”.
    - If COMMENTS lack substance, omit this entire section.
- LLM perspective (required unless the fail-safe rule applies)
     - View: your synthesis (no repetition).
	   - Impact: who/what changes.
	   - Watch next: concrete follow-ups (benchmarks, releases, policy steps).
     - Each bullet must add a non-redundant synthesis, consequence, or concrete follow-up.

STYLE & BOUNDARIES
- Be precise and concise; one idea per bullet; prefer numbers and named entities over adjectives.
- No throat-clearing, quotes, or links; code only if essential (≤5 lines).
- Do not restate facts across sections; each line must add new information.
- If nearing caps, tighten LLM bullets → trim comment bullets → tighten TL;DR; never remove the LLM perspective section.

FAIL-SAFE RULES
- Both CONTENT and COMMENTS cannot be empty: if they are, do not extrapolate; state limitations in the italic note after TL;DR and bail early without touching the sections.
- If COMMENTS are heavily polarized, ensure at least one counterpoint appears across the 3 bullets.
- Never exceed section caps; truncate gracefully rather than spill over.
