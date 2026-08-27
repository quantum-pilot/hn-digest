# Hashcards: A plain-text spaced repetition system

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46264492) | Link: https://borretti.me/article/hashcards-plain-text-spaced-repetition

### TL;DR

Hashcards stores flashcard content as lightweight Markdown decks while keeping review history in a colocated SQLite database and scheduling with FSRS. Content hashes identify cards, enabling editor-native creation, Git versioning, Unix-tool queries, scripted generation, and sharing without exposing an opaque application database. The author built it to combine Anki's scheduling strength with Mochi's lower-friction writing experience. Commenters appreciate plain text but question whether editing a card changes its identity and loses history, while Anki users dispute the critique of its interface.

### Comment pulse

- Plain Markdown earns support for portability, automation, linking, and versioning; existing options such as Emacs org-drill already cover similar workflows.
- Some readers extend spaced repetition beyond facts into behavioral reinforcement, using recurring prompts to rehearse better responses.

### LLM perspective

- View: Separating durable card text from scheduling state offers ownership without pretending every datum belongs in Markdown.
- Impact: Technical learners gain programmable decks, while nontechnical users may still prefer Anki's integrated ecosystem.
- Watch next: Verify identity behavior after edits, database portability, conflict handling, and long-term FSRS migration stability.
