# Firefox 147 Will Support the XDG Base Directory Specification

- Score: 306 | [HN](https://news.ycombinator.com/item?id=45992829) | Link: https://www.phoronix.com/news/Firefox-147-XDG-Base-Directory

### TL;DR

Firefox 147 is expected to address a 21-year-old request to respect Linux's XDG Base Directory locations instead of placing everything under `~/.mozilla`. Support landed in Mozilla's integration branch, closing the 2004 bug. Commenters welcomed fewer home-directory dotfiles but questioned whether the implementation fully separates configuration, persistent data and cache. Their code reading suggests existing `~/.mozilla` profiles remain in place while new profiles use an XDG configuration path, avoiding silent data loss but offering no automatic migration.

### Comment pulse

- Adoption by Firefox gives XDG conventions visibility → inconsistent application support has long limited their practical value.
- Skeptics called partial relocation incomplete compliance → profile data may remain concentrated under configuration rather than split by purpose.

### LLM perspective

- View: Compatibility-first fallback is sensible, but directory compliance should describe actual data semantics precisely.
- Impact: New Linux profiles become tidier while existing users avoid a risky forced migration.
- Watch next: Firefox 147 release behavior, migration documentation and separation into config, data and cache paths.
