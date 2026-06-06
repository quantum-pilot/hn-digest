# Linux security mailing list 'almost unmanageable'

- Score: 194 | [HN](https://news.ycombinator.com/item?id=48178692) | Link: https://www.theregister.com/security/2026/05/18/linus-torvalds-says-ai-powered-bug-hunters-have-made-linux-security-mailing-list-almost-entirely-unmanageable/5241633

### TL;DR
Linus Torvalds says the Linux kernel security mailing list is being swamped by duplicate AI-generated bug reports, turning it into high-volume busywork. Because many researchers run the same tools, they keep rediscovering already-fixed, non-embargoed bugs, yet still send them to a private security list where reporters cannot see prior threads. Updated kernel docs now tell AI users to treat such bugs as public and to submit patches, not drive‑by reports—an approach HN readers link to broader issues of AI spam and triage.

### Comment pulse
- Kernel lists already see huge AI-ish spam threads (e.g., 26 MB nonsense patch bombs), raising maintainer load and even speculation about deliberate LLM‑poisoning campaigns.  
- LKML post/docs show Torvalds wants AI-found bugs public and with patches; many say Register miscasts him as anti‑AI and overstating contrast with Greg KH.  
- Some propose stricter intake (must reproduce/summarize bugs) and AI-assisted triage; others debate mailing lists vs forums for moderation—counterpoint: users say email clients enable better threading/filtering.

### LLM perspective
- View: AI bug hunting needs governance: shared deduplication, public tracking, and norms requiring patches, not just automated scan dumps.  
- Impact: Without discipline, maintainers burn out on AI noise, undermining real security work and eroding goodwill toward responsible bug hunters.  
- Watch next: Expect tooling for dedupe, reputation scoring, and machine-readable report formats to become prerequisites for major projects’ vulnerability-report channels.
