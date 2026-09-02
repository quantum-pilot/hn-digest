# The ChatGPT/Codex app bundles a full copy of LibreOffice

- Score: 378 | [HN](https://news.ycombinator.com/item?id=49527396) | Link: https://simonwillison.net/2026/Sep/1/codex-libreoffice/

### TL;DR

Simon Willison found a 1.7 GB ChatGPT/Codex desktop runtime cache containing Python, Node.js, Poppler, Git, LibreOffice, and document skills describing how the app uses those binaries. The inspection suggests LibreOffice supports local reading, rendering, or manipulating office documents, especially formats without reliable lightweight alternatives. However, the captured state does not establish whether everything ships with installation or downloads when a task needs it. Commenters debated the dependency size, document fidelity, project support, smaller headless packaging, and inconsistent desktop-app experiences.

### Comment pulse

- LibreOffice offers broad legacy-format coverage → developers said it reliably opens documents that specialized libraries miss.
- A full suite is a large runtime dependency → headless packaging might retain conversion capabilities with less disk use.
- Open-source licensing permits bundling without payment → commenters still hoped commercial users would fund upstream compatibility improvements.

### LLM perspective

- View: Bundling proven tools trades installation size for deterministic local document capabilities across varied formats.
- Impact: Users gain richer file workflows, while maintainers inherit patching, licensing, security, and rendering-quality responsibilities.
- Watch next: Verify fresh-install contents, on-demand downloads, headless alternatives, update cadence, attribution, and Office compatibility tests.
