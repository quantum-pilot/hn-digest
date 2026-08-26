# Everyone hates OneDrive, Microsofts cloud app that steals and deletes files

- Score: 171 | [HN](https://news.ycombinator.com/item?id=46526376) | Link: https://boingboing.net/2026/01/05/everyone-hates-onedrive-microsofts-cloud-app-that-steals-then-deletes-all-your-files.html

### TL;DR

Boing Boing argues that Windows pushes users into OneDrive without a clear explanation of how known folders become cloud-managed. When people disable backup after noticing uploads or storage limits, local-looking files may disappear, leaving a pointer for recovery. Even after redownloading them, deleting the cloud copies can remove the local copies again. The article likens this failure mode to ransomware and says Microsoft deliberately buries the safe separation procedure, making file ownership and location dangerously opaque for people who never knowingly opted in.

### Comment pulse

- Several readers described painful recoveries and said OneDrive deliberately blurs local storage, cloud backup, synchronization, and profile redirection.
- Satisfied users reported reliable syncing when they knowingly opted in and kept nonsynced files outside OneDrive-managed folders.
- The sharpest disagreement concerned consent: even defenders distinguished a useful Dropbox-like service from repeated prompts and silent folder migration.

### LLM perspective

- View: The core defect is not synchronization itself but an interface that conceals state transitions with destructive consequences.
- Impact: Cloud convenience becomes systemic risk when backup, mirroring, deletion, and local availability are presented as one seamless action.
- Watch next: Microsoft should expose file location and deletion scope explicitly, especially during enrollment, disabling, migration, and storage cleanup.
