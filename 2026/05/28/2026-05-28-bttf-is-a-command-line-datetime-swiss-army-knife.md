# Bttf is a command line datetime Swiss army knife

- Score: 146 | [HN](https://news.ycombinator.com/item?id=48303881) | Link: https://github.com/BurntSushi/bttf

### TL;DR

`bttf` is a Rust command-line toolkit for parsing, formatting, comparing, rounding, converting, and generating datetimes and spans. It understands time zones, localized formats, relative expressions, recurring sequences, and can tag timestamps inside arbitrary records so pipelines preserve surrounding data. Built largely on Jiff with optional ICU4X localization, it intentionally is not POSIX `date` compatible and may still break interfaces. HN praised its explicit separation of civil time from absolute instants, while optimizing the author’s Git-history pipeline and applauding attention to datetime edge cases.

### Comment pulse

- The civil-time/instant distinction exposes DST ambiguity instead of silently choosing semantics → commenters saw this as a major advantage over common APIs.
- Per-file `git log` calls work but scale poorly → backward commit traversal or `git-last-modified` can produce the source data faster.
- Users valued concrete pipeline examples → they made advanced shell composition approachable despite limited command-line experience.

### LLM perspective

- **View:** Its distinctive feature is structured composition: datetime transformations can operate on embedded values without discarding each record’s payload.
- **Impact:** Operators gain one consistent vocabulary for logs, schedules, spans, and time zones instead of brittle utility chains.
- **Watch next:** Jiff 1.0 feedback, interface stabilization, locale configuration, and benchmarks against specialized Git and datetime tools.
