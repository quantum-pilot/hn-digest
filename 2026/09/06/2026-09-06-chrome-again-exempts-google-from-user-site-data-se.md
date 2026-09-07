# Chrome again exempts Google from user site data settings

- Score: 579 | [HN](https://news.ycombinator.com/item?id=49581870) | Link: https://lapcatsoftware.com/articles/2026/9/1.html

### TL;DR

Jeff Johnson reports that Chrome 152.0.7977.83 retains Google Search cookies, local storage, and session storage after all windows close, despite the setting to delete saved site data. He reproduced this on two Macs while signed out, with Chrome sign-in disabled and DuckDuckGo set as default search. Johnson says google.com appears to be the only exception he observed and favors a QA failure over conspiracy, but has not identified when it began or its cause. Commenters confirmed relevant sign-in distinctions and debated Chrome’s trustworthiness.

### Comment pulse

- Some suspected Google-specific favoritism — counterpoint: the author explicitly considered an accidental regression more likely.
- A proposed sign-in explanation conflicted with the test conditions, which disabled Chrome sign-in and used a signed-out session.
- Another commenter reported difficulty deleting an accidental search entry, but that anecdote does not establish the same bug.

### LLM perspective

- View: A privacy control is unreliable if its exceptions are invisible, regardless of whether the cause is intentional.
- Impact: Signed-out users may retain Google data they reasonably expected Chrome to erase.
- Watch next: A minimal reproduction, Chromium bug acknowledgment, affected platforms, stored-data scope, and regression tests.
