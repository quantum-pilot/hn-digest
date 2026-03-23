# The future of version control

- Score: 370 | [HN](https://news.ycombinator.com/item?id=47478401) | Link: https://bramcohen.com/p/manyana

### TL;DR
Manyana is Bram Cohen’s 470‑line proof‑of‑concept for a CRDT‑based version control model. Instead of failing merges, it always computes a deterministic result and separately flags overlapping edits as conflicts, showing them structurally (who deleted/added what, where) using a “weave” that stores every line ever seen with add/remove metadata. This enables non-destructive rebases and order‑independent merges in complex DAGs. HN reactions split between “this is mostly a UX/merge-tool issue Git can already address” and “CRDTs fundamentally don’t fit semantic code conflicts,” with some historical comparisons to Codeville, Darcs, and Pijul.

---

### Comment pulse
- Better merges via tools, not new VCS → p4merge, diff3/zdiff3, IDE UIs already show base+both sides; conflict clarity is UX, not data structure.  
- CRDT skepticism → real value of VCS is surfacing semantic conflicts; “never-failing” merges risk garbage states and make cherry-pick/revert harder — counterpoint: CRDTs can still expose overlaps and keep conflicts explicit.  
- Alternative visions → some advocate rebase‑only, small commits, avoiding merge commits; others argue CRDT/weave or patch‑based systems (Pijul, Codeville lineage) better model “units of change.”

---

### LLM perspective
- View: CRDT-backed weaves look especially promising for collaborative editors and code review UIs, even if they never replace Git wholesale.  
- Impact: Could influence next-gen tools (jj-like systems, IDEs) to adopt richer conflict representations and non-blocking merge workflows.  
- Watch next: Scalable prototypes on large repos, performance benchmarks vs Git/Pijul, and concrete designs for cherry-pick, revert, and directory-level operations.
