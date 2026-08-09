# An AI Vibe Coding Horror Story

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47762901) | Link: https://www.tobru.ch/an-ai-vibe-coding-horror-story/

### TL;DR

A medical practice employee built and deployed an AI-generated patient-management system after watching a video, importing records and sending appointment audio to two US AI services. Within 30 minutes, the author obtained full read/write access: the database had no access controls or row-level security, while authorization existed only in client-side JavaScript. Data was unencrypted, patients received no notice, and no processing agreement covered the US hosting. The practice added authentication after disclosure. Commenters shared similar incidents and argued that production AI coding still requires engineering, security, and operational review.

### Comment pulse

- Similar insurance, legal, and surgical systems exposed customer files or credentials; reporters sometimes met threats and hostility instead of remediation.
- Vibe coding impressed on prototypes and even some application internals — counterpoint: deployment, privacy, architecture, and failure modes demand experienced review.
- Models secure what users ask about; veteran engineers contribute a “graveyard” of failures that novices may never think to prompt against.

### LLM perspective

- **View:** The central risk is authority without comprehension: generated software can appear functional while silently violating essential trust boundaries.
- **Impact:** Cheap app generation moves security failures into clinics and small businesses whose users cannot meaningfully assess or avoid them.
- **Watch next:** Mandatory privacy impact reviews, deployment guardrails, independent penetration tests, incident disclosure, and regulator action on affected practices.
