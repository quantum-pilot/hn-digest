# Hashcards: A plain-text spaced repetition system

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46264492) | Link: https://borretti.me/article/hashcards-plain-text-spaced-repetition

### TL;DR
Hashcards is a local-first spaced repetition app that stores flashcards as plain-text Markdown files instead of inside an opaque database. Decks are simple `.md` files with lightweight syntax for Q/A and cloze deletions; cards are content-addressed by hash, while review history lives in a local SQLite file. The author built it after frustration with Anki’s clunky UI and Mochi’s weaker scheduling, aiming for minimal friction in card creation, Git-based ownership/versioning, and the FSRS algorithm under a clean web drill interface.

---

### Comment pulse
- Spaced repetition as behavior change → Using SRS to rehearse reactions in relationships or habits reliably eliminates repeated mistakes over years—counterpoint: some see this as over-structuring emotional life.  
- Anki criticism feels unfair → Many find Anki’s UI functional, WYSIWYG appropriate for its audience, and plugin “jank” a powerful bazaar-style extensibility rather than a flaw.  
- Plain-text + SRS has a broader ecosystem → Emacs org-drill and other Markdown-based tools show similar benefits: editor freedom, Git versioning, easy cross-linking, and note‑embedded flashcards.

---

### LLM perspective
- View: Hashcards squarely targets power users who already live in text editors, shells, and Git, not mainstream learners.  
- Impact: Could make long-term, large card collections more maintainable, scriptable, and auditable, especially for technical or research-heavy domains.  
- Watch next: Clarify hash-based identity vs. typo edits, add import/export with Anki/Mochi, and benchmark FSRS effectiveness across real-world decks.
