# Windows 11's built-in Weather app wastes more than 1 GB of RAM

- Score: 335 | [HN](https://news.ycombinator.com/item?id=49232138) | Link: https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html

### TL;DR

Tests cited by Notebookcheck found Windows 11’s built-in Weather app using about 1.2 GB of memory while displaying a forecast, sometimes rising to 1.5–1.6 GB during basic navigation. The app is an MSN web experience hosted through WebView2, spawning multiple Chromium processes and embedding advertisements; Apple’s native counterpart reportedly used under 250 MB in a similar comparison. The footprint may matter on 8 GB systems, but Task Manager accounting, shared versus private pages, committed versus physical memory, and cross-platform methodology complicate the headline comparison.

### Comment pulse

- Readers viewed both the Windows figure and macOS’s roughly 230 MB as excessive for weather.
- Some reported that installing MSN Weather as an ad-blocked browser app used far less memory.
- Debate over Task Manager semantics showed that “RAM usage” is not one unambiguous measurement.

### LLM perspective

- **View:** The application appears bloated, though the fivefold comparison needs a clearly defined measurement method.
- **Impact:** Web-based built-ins can impose disproportionate costs on low-memory PCs while weakening trust in platform polish.
- **Watch next:** Reproducible private-working-set tests and whether Microsoft rebuilds MSN apps with native UI.
