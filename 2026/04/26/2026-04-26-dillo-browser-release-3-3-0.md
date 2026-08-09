# Dillo Browser Release 3.3.0

- Score: 145 | [HN](https://news.ycombinator.com/item?id=47911977) | Link: https://dillo-browser.org/release/3.3.0/

### TL;DR

Dillo 3.3.0 adds scriptable browser control through a UNIX socket and the new `dilloc` utility, plus configurable page actions that can transform or refetch the current page. It introduces experimental FLTK 1.4 support, but maintainers warn packagers against enabling it by default because high-DPI and Wayland rendering remain unreliable. OAuth redirects now accept narrowly scoped cookies, while Brotli, IPv6 defaults, navigation improvements, and memory-safety fixes round out the release. HN users welcomed automation but emphasized how JavaScript-only services increasingly exclude small browsers.

### Comment pulse

- `dilloc` already enables redirect menus resembling Unix plumbers, replacing JavaScript-dependent URLs with simpler equivalents.
- Google and some HN requests reportedly fail in Dillo; alternative search frontends remain usable without JavaScript.
- Privacy-conscious users see Dillo as a fallback if mainstream browsers adopt age verification — counterpoint: commenters expect broader legal pressure on anonymity.

### LLM perspective

- Remote loading of arbitrary page content expands capability; action scripts deserve careful quoting, trust boundaries, and review.
- FLTK testing should publish DPI, compositor, platform, and font-backend matrices before default enablement.
- Track compatibility gains against binary size, startup time, memory use, and security surface.
