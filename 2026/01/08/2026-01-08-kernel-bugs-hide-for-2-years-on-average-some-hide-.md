# Kernel bugs hide for 2 years on average. Some hide for 20

- Score: 277 | [HN](https://news.ycombinator.com/item?id=46536340) | Link: https://pebblebed.com/blog/kernel-bugs

### TL;DR

An analysis mined 125,183 Linux kernel fixes with traceable `Fixes:` tags across 2005–2025. After filtering, bugs remained undiscovered for 2.1 years on average; 13.5% lasted at least five years, and one lasted 20.7 years. Race conditions and less-tested CAN and SCTP code had especially long lifetimes. Discovery within one year appears to be improving, though recent cohorts are right-censored. The author also presents VulnBERT, reporting 92.2% recall and a 1.2% false-positive rate on a 2024 test set, while emphasizing dataset selection and generalization limits.

### Comment pulse

- A long Rust debate distinguished memory-safety gains from logic, hardware, and concurrency errors, with replies arguing Rust can still encode safer invariants.
- Readers questioned whether long lifetime measures severity or maintainer performance; others noted dangerous bugs can remain quiet simply because triggering conditions are rare.
- A related browser-security study drew interest, while commenters cautioned that kernel `Fixes:` tags are useful but inconsistently applied.

### LLM perspective

- View: Lifetime data is more useful for mapping testing blind spots than scoring overall kernel quality.
- Impact: Commit-risk ranking could focus review and fuzzing, but aggregate scores must not become automated approval gates.
- Watch next: Independent replication, prospective performance on post-2024 commits, severity calibration, and results for untagged fixes and subsystem-specific models.
