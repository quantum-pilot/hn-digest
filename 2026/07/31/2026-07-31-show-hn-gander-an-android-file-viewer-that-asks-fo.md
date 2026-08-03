# Show HN: Gander, an Android file viewer that asks for no permissions

- Score: 190 | [HN](https://news.ycombinator.com/item?id=49119425) | Link: https://github.com/mokshablr/gander

### TL;DR

Gander is a 15 MB, open-source Android 8+ viewer for PDFs, modern Office files, spreadsheets, slides, media, Markdown, text, and code. It works offline without declared permissions, ads, analytics, accounts, or INTERNET access, receiving chosen files or folders through Android’s Storage Access Framework and rendering web-based formats with bundled libraries in a locked-down WebView. HN users welcomed privacy-first consolidation while debating whether no INTERNET permission guarantees isolation, and they requested broader distribution and format coverage.

### Comment pulse

- Privacy skeptics identify indirect exfiltration paths → browser intents, shared user IDs, and content providers can enlist networked apps — counterpoint: direct sockets remain unavailable.
- Sideloading trust improved → a requested signing fingerprint was added, enabling users and Obtainium to verify release continuity.
- Format feedback produced a fix → .ods rendering worked internally, but missing MIME registration hid the app from Open-with.

### LLM perspective

- View: Permission minimization is a strong baseline, but trustworthy privacy also requires auditing outbound intents and inter-process interfaces.
- Impact: One offline app can replace several specialized viewers, reducing installed software while concentrating renderer and vendored-library risk.
- Watch next: Track F-Droid listing, .odt support, .pptx rendering quality, and whether a faithful offline legacy-format renderer appears.
