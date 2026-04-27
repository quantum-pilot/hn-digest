# Dillo Browser Release 3.3.0

- Score: 145 | [HN](https://news.ycombinator.com/item?id=47911977) | Link: https://dillo-browser.org/release/3.3.0/

### TL;DR
Dillo 3.3.0 advances the ultra-lightweight browser with a new `dilloc` control tool over a UNIX socket, enabling scripting (open, reload, dump, load HTML) and page-specific actions like re-fetching via curl-impersonate to bypass some JS-heavy barriers. It adds experimental FLTK 1.4 support (not for general users yet), fixes OAuth logins while keeping strict cookie policies, improves keyboard/mouse ergonomics, and migrates hosting off GitHub. HN discussion centers on small browsers vs. a JS-dominated, increasingly regulated web.

### Comment pulse
- Modern web hostile to minimalist browsers → Google search and major sites often demand heavy JS; proxy front-ends like Startpage or html.duckduckgo partially restore no-JS access — counterpoint: dependence on third-party proxies is brittle.
- Privacy and regulation may drive Dillo adoption → age-verification mandates and browser-level tracking could push users toward small, script-light browsers to preserve anonymity.
- `dilloc` already valued → users script redirect-style menus that swap JS-laden URLs for simpler mirrors, similar to Libredirect, making Dillo more usable on today’s web.

### LLM perspective
- View: Dillo is evolving into a programmable UI for custom HTTP pipelines, rather than competing as a full modern browser.
- Impact: Best suited to power users, BSD/Linux minimalists, and environments where predictability, small footprint, and auditability trump site compatibility.
- Watch next: Growth of shared page-action scripts, FLTK 1.4 stabilization on Wayland/high DPI, and strategies for CAPTCHAs and age gates without JS bloat.
