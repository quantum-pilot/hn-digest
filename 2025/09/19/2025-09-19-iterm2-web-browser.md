# iTerm2 Web Browser

- Score: 131 | [HN](https://news.ycombinator.com/item?id=45298793) | Link: https://iterm2.com/documentation-web.html

- TL;DR
    - iTerm2 adds an optional WebKit-based browser profile that lives in the same window/tab/split hierarchy as terminals. It supports hotkeys, smart selection, reader/distraction modes, basic ad/popup blocking, privacy (/dev/null), AI chat on page content, bookmarks/marks, instant replay, and automation. Built on WKWebView, it inherits Safari compatibility but lacks passkeys and advanced adblocking. HN finds the creator’s candid motivation refreshing; some like the unified workflow or enshittification-fighting potential, while security-minded users say they’ll skip it but still applaud iTerm2.

- Comment pulse
    - Fun experiment, not for daily browsing → honesty about 'midlife crisis' motive feels refreshing; users support optionality even if they’ll never enable it.
    - Security concern → embedding a browser expands attack surface; some will avoid it — counterpoint: terminal/browser might curb enshittification for power users.
    - iTerm2 admiration → users gladly donate; 3.6 changelog delights (relative timestamp baselines, extending TUI background colors); others seek advanced-use examples.

- LLM perspective
    - View: Embedding WKWebView in a terminal is niche but practical for docs, dashboards, and quick previews alongside shells.
    - Impact: Benefits macOS devops and power users; enterprise admins will likely disable the plugin; not a replacement for Safari/Chrome.
    - Watch next: Security model, sandboxing, and passkey/WebAuthn workarounds; performance under multiple panes; potential APIs for automation and triggers.
