# GNU recutils: Plain text database

- Score: 94 | [HN](https://news.ycombinator.com/item?id=46265811) | Link: https://www.gnu.org/software/recutils/

### TL;DR

GNU Recutils stores databases as human-editable text records containing arbitrary named fields, then adds command-line and C-library tools for querying and validation. Despite its simple format, it supports required or forbidden fields, keys, constraints, types, joins, grouping, aggregates, selective encryption, conversion, templates, and editor integrations. Commenters valued readable version-control diffs and shell or Emacs workflows for small projects, while acknowledging that SQLite and larger systems offer better performance. The format favors inspectability and portability over scale.

### Comment pulse

- Git users praised record-oriented text because ordinary diffs expose meaningful data changes without database-specific tooling.
- WordNet’s byte-offset indexes illustrated another plain-text design: direct reads are cheap, while writes require rebuilding indexes.
- Recutils users highlighted constraints and editor support as the difference between structured records and an improvised text file.

### LLM perspective

- View: Recutils occupies a useful middle ground between ad hoc text and opaque embedded databases.
- Impact: Small, reviewable datasets gain validation and queries while remaining editable with standard tools.
- Watch next: Evaluate concurrent writes, transaction needs, dataset growth, encryption ergonomics, and migration before choosing it over SQLite.
