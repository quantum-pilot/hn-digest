# Tl;dv: Over 180k meetings left wide open

- Score: 523 | [HN](https://news.ycombinator.com/item?id=49242739) | Link: https://bobdahacker.com/blog/tldv-hack

### TL;DR

A researcher says tl;dv’s Firestore rules let any authenticated user enumerate 181,874 meeting records across 84,312 users and expose roughly 1,000 live conference IDs at a time. He demonstrated access by entering two active calls, while more than 1,000 configured-public meetings exposed recordings or transcripts. He reported the tenant-isolation flaw in January and described six months of unanswered follow-ups. Commenters say tl;dv later fixed it, but criticized the company’s public-sharing framing and questioned what SOC 2 certification actually guarantees.

### Comment pulse

- Readers treated six months of exposure and silence as potentially business-ending negligence.
- AI notetakers create consent risks when employees route meetings through third-party services without colleagues or employers realizing.
- SOC 2 was widely dismissed as process evidence rather than proof of secure implementation.

### LLM perspective

- **View:** Missing tenant authorization on sensitive meeting metadata is a severe access-control failure, independent of public-sharing settings.
- **Impact:** Governments, universities, and companies may need incident review, credential checks, and vendor reassessment.
- **Watch next:** Independent fix verification, affected-user notification, access-log investigation, and a documented disclosure-response process.
