# Index, Count, Offset, Size

- Score: 152 | [HN](https://news.ycombinator.com/item?id=47058584) | Link: https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/

### TL;DR

Matklad argues many indexing bugs are preventable with strict naming rather than heavier type systems. At TigerBeetle, quantities of elements are always *_count*, element positions *_index*, byte quantities *_size*, and byte positions *_offset*, maintaining the invariant `index < count`. Combined with “big-endian” names (source_index, target_index) and matched name lengths, code visually self-checks, especially around low-level slice/serialization math. HN commenters largely endorse this, debating alternatives like dedicated index types and the overloaded, ambiguous term length.

---

### Comment pulse

- Naming dimensions (_count, _size, _index, _offset) lets reviewers spot “dimension mismatches” almost mechanically—counterpoint: some prefer distinct types so the compiler enforces units.  
- Discussion dissects length vs count vs size: many see length as element-count historically; others find it ambiguous, especially with bytes, Unicode, and heterogeneous containers.  
- Others share schemes like index for 0-based vs number/ordinal for 1-based, and lament auto-formatters breaking visually aligned, equal-length related variable names.  

---

### LLM perspective

- View: Low-friction naming rules are realistic to standardize across teams, unlike sophisticated dependent-typing systems or pervasive newtype wrappers.  
- Impact: Biggest payoff is in systems-level or serialization-heavy code where off-by-one or byte/count mixups can silently corrupt data.  
- Watch next: Tooling could flag inconsistent suffixes or enforce index/count relationships, turning this convention into a semi-formal, language-agnostic linting rule.
