# Meta replaces WhatsApp for Windows with web wrapper

- Score: 405 | [HN](https://news.ycombinator.com/item?id=45910347) | Link: https://www.windowslatest.com/2025/11/12/meta-just-killed-native-whatsapp-on-windows-11-now-it-opens-webview-uses-1gb-ram-all-the-time/

### TL;DR

Windows Latest reports that WhatsApp version 2.2584.3.0 replaces its WinUI/UWP client with a WebView2 wrapper. In the publication’s tests, the new build used roughly 1.2GB while idle after login, versus under 100MB for the native app, and showed slower loading and notification problems. The article speculates layoffs drove the change, without evidence. Commenters instead highlighted cross-platform coordination and feature-parity pressures, while some users said the old native client’s input bugs made the heavier replacement preferable.

### Comment pulse

- Native-app advocates saw needless resource regression; platform veterans described coordination costs that grow with rapid, parallel feature work.
- Some users preferred higher memory use if it eliminates longstanding input and reliability bugs.

### LLM perspective

- View: The tradeoff is centralized product velocity versus platform efficiency, not simply web technology versus competence.
- Impact: Windows users absorb memory and integration costs when desktop usage cannot justify a dedicated release pipeline.
- Watch next: Independent measurements of startup, idle memory, calls, notifications, and accessibility should test whether consolidation pays off.
