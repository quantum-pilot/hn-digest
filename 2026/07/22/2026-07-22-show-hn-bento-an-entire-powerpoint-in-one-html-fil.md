# Show HN: Bento - An entire PowerPoint in one HTML file (edit+view+data+collab)

- Score: 609 | [HN](https://news.ycombinator.com/item?id=49008211) | Link: https://bento.page/slides/

### TL;DR

Bento packages a presentation’s data, editor, viewer, notes, charts, and optional collaboration into one self-saving HTML file. Slide JSON stays readable near the top; a compressed application blob inflates locally without external runtime fetches, while browser file access writes changes back or falls back to downloading a replacement. Opt-in CRDT collaboration uses encrypted client data and a blind Cloudflare relay with per-user permissions and revocation. Commenters welcomed the portable model but saw lifecycle, trust, and concurrency as remaining production hurdles.

### Comment pulse

- Single-file apps feel broadly reusable → readers envisioned wikis, spreadsheets, diagrams, and small React tools sharing content, controls, and local state.
- Collaboration needs hardening → HN traffic froze one Mac, spam forced resets, and concurrent edits stole focus — counterpoint: ordinary sessions may fare better.
- Presentation ergonomics remain debatable → one Reveal.js user missed vertical branching, while others preferred escaping complex Office formats.

### LLM perspective

- **View:** The file-as-software approach makes generated artifacts inspectable, portable, and forkable without requiring users to adopt a hosted workspace.
- **Impact:** LLMs can cheaply assemble specialized document-app hybrids, shifting differentiation toward reliability, migration paths, and human-authored interaction design.
- **Watch next:** Benchmark large decks and multiuser sessions, publish the signing threat model, and demonstrate versioned shell-to-JSON migrations.
