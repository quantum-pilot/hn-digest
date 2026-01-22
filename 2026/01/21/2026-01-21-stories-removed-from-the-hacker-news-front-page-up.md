# Stories removed from the Hacker News Front Page, updated in real time (2024)

- Score: 232 | [HN](https://news.ycombinator.com/item?id=46704555) | Link: https://github.com/vitoplantamura/HackerNewsRemovals

### TL;DR
A small C# tool continuously polls the Hacker News API, comparing the current top 30 stories to the top 90 from the previous minute. If a story that was on the front page disappears without plausibly dropping in rank, it’s logged as “removed,” with rank, points, comments, and links. The author created it after LLM‑related posts about their project were renamed or removed, hoping to quantify moderation and push for more transparent, user‑visible moderation data. HN reactions center on ads, politics, and AI fatigue.

---

### Comment pulse
- Moderation is valued for keeping out ads and partisan noise → some see a “silent majority” defending quality—counterpoint: others call it a small heckler’s veto enabled by flags.  
- Many are exhausted by repetitive AI/LLM discourse → want filters or topic hiding rather than more meta‑fights about whether AI belongs on HN.  
- Several feel important tech–politics stories (Twitter/X, Musk, regulation) get mass‑flagged → argue that suppressing these is itself a political act, since tech now drives politics.

---

### LLM perspective
- View: A clever, lightweight measurement approach, but its “fast drop == moderated removal” heuristic can misclassify organic or duplicate rank changes.  
- Impact: Gives power users and critics empirical fodder about front‑page dynamics; nudges moderators toward clearer explanations and built‑in transparency tools.  
- Watch next: Add automatic duplicate detection, topic tagging (AI, politics, ads), and a public dashboard correlating removals with flags or flamewar patterns.
