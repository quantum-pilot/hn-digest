# Grok CLI uploaded the whole home directory to GCS

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48892468) | Link: https://twitter.com/a_green_being/status/2076598897779020159

### TL;DR

A user alleged Grok Build silently uploaded 12GB of repository data and Git history to Google Cloud Storage, discoverable through `repo_state.upload` logs. Commenters examining the behavior distinguished it from an LLM autonomously reading files: they described deterministic client logic, possibly server-controlled, that uploads a session’s repository for remote semantic indexing. Whether the reported home-directory scope resulted from initializing Git there remained unclear. HN judged undisclosed bulk transfer unacceptable and emphasized that Markdown instructions are not security boundaries; filesystem permissions, restricted users, containers, network allowlists, and explicit consent are.

### Comment pulse

- Indexing need not require exfiltration → embedding models and `ripgrep` can run locally, avoiding wholesale source transfer.
- Instruction files are not access controls → models and harnesses may ignore prose; OS permissions and a separate control plane enforce boundaries.
- Responsibility stayed disputed → sandbox advocates urged user caution — counterpoint: tools marketed to novices must make consent and safe defaults intrinsic.

### LLM perspective

- **View:** Context convenience cannot justify invisible data movement; collection scope must be minimal, inspectable, and opt-in.
- **Impact:** Source code, credentials, personal files, and complete histories may become incident-response liabilities.
- **Watch next:** Demand xAI’s disclosure, exact client logic, retention and training policies, affected versions, deletion tooling, and an independent audit.
