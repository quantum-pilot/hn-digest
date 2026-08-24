# Twelve Days of Shell

- Score: 223 | [HN](https://news.ycombinator.com/item?id=46190577) | Link: https://12days.cmdchallenge.com

### TL;DR

This browser game teaches beginner Unix commands through twelve festive file-manipulation puzzles, starting with ls and progressing through searching, globbing, moving files, and pipelines. Its terminal supports conveniences such as tab completion and readline keys, with instant success feedback. Commenters enjoyed the approachable design but found several prompts ambiguous, state changes unclear, and valid alternative commands rejected or hidden behind unshown error output. The discussion broadened into command-line ergonomics, Vim learning, browser keyboard navigation, and reducing mouse-related strain.

### Comment pulse

- Beginners need observable failure → showing wrong output would support iteration better than forcing guesses about the evaluator’s intent.
- Exercise wording is underspecified → case sensitivity, prior-state dependence, and expected output format repeatedly surprised players.
- Keyboard fluency can improve comfort → commenters recommended built-in Vim training and alternative pointing devices for RSI.

### LLM perspective

- View: A teaching shell should grade outcomes, not preferred command syntax, unless syntax itself is the lesson.
- Impact: Ambiguous validation risks teaching compliance with hidden tests instead of transferable command-line reasoning.
- Watch next: Accept equivalent commands, expose stderr and output, label workspace resets, and clarify case requirements.
