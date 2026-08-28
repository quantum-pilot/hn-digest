# A small change to improve browsers for keyboard navigation

- Score: 207 | [HN](https://news.ycombinator.com/item?id=45013737) | Link: https://b.43z.one/2025-07-22/

### TL;DR

Firefox’s apostrophe quick-find can select and activate links, but ordinary find modes highlight text without reliably activating buttons, scripted spans, or other interactive elements. The author built a tiny extension that listens for Enter, locates the parent element of the current selection, invokes its click handler, and clears the selection. It improves the author’s keyboard workflow on modern sites that avoid semantic links, but the implementation deliberately remains a rough hack with undiscovered exclusions. Commenters favored established keyboard-navigation extensions and noted broader accessibility failures in scrolling and focus management.

### Comment pulse

- Readers recommended Vimium, Vimium C, Tridactyl, ShortCat, and Mouseless for richer keyboard navigation.
- PageUp, PageDown, sticky headers, custom scroll containers, and poor focus behavior remain recurring accessibility problems.
- One correction noted Enter can activate selected links and some buttons after dismissing search, depending on browser.

### LLM perspective

- View: The extension patches symptoms of nonsemantic web interfaces rather than the underlying accessibility failure.
- Impact: A small activation bridge can help power users, but synthetic clicks may choose the wrong ancestor.
- Watch next: Add focus awareness, editable-field exclusions, nested-control handling, and tests across dynamic sites.
