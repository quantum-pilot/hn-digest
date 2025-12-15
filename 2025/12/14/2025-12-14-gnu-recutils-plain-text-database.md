# GNU recutils: Plain text database

- Score: 94 | [HN](https://news.ycombinator.com/item?id=46265811) | Link: https://www.gnu.org/software/recutils/

### TL;DR
GNU Recutils is a GNU toolset for managing “recfiles”: human-editable plain text databases with typed fields, constraints, joins, and optional AES-encrypted fields. It ships as a C library plus command-line utilities, integrates tightly with Emacs/org-mode and Vim, and converts to/from CSV and some legacy formats. HN commenters highlight recfiles as excellent for version-controlled data (clean diffs in git), praise the Emacs/Bash tooling for small projects, and compare it to other classic plain-text database schemes like WordNet’s offset-based files.  

---

### Comment pulse
- Plain text databases appeal → WordNet’s original format uses byte offsets into text files, enabling random access without loading everything—counterpoint: mostly read-only, updates are painful.  
- Recutils in practice → .rec works well for git-tracked data with readable diffs; Emacs/Bash tooling is powerful though slower than SQLite for larger workloads.  
- Access issues → Some browsers get 403/“Too Many Requests” from gnu.org; spoofing User-Agent as curl is a workaround, ironically reversing typical blocking.  

---

### LLM perspective
- View: Recutils hits a sweet spot between ad-hoc CSVs and full SQL for structured, human-edited project metadata.  
- Impact: Useful for config, inventories, and small knowledge bases where transparency, reviewability, and offline editing matter more than raw performance.  
- Watch next: Compare against SQLite, LiteFS, and structured text formats (TOML, YAML) for tooling, schema enforcement, and git-friendliness.
