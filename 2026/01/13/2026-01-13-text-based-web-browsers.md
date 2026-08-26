# Text-based web browsers

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46597518) | Link: https://cssence.com/2026/text-based-web-browsers/

### TL;DR

Testing Lynx, ELinks, and w3m shows that solid semantic HTML still yields readable pages, but support for newer HTML features is badly outdated. These browsers expose all details, dialogs, popovers, inert regions, and even content marked hidden; datalist suggestions disappear. The results range from verbose fallback to broken form actions and security or accessibility mistakes, with hidden being the clearest standards failure. HN users nevertheless value terminal browsing for accessibility, scripting, safety, and distraction-free reading, highlighting edbrowse and newer Chawan as more capable alternatives.

### Comment pulse

- Line-oriented browsers offer distinctive utility → edbrowse prioritizes blind users, scripting, and composable text workflows rather than imitating a graphical interface.
- Page structure often matters more than rendering → navigation-first markup creates clutter; content-first HTML benefits terminals and screen readers.
- Modern capability is possible → Chawan adds CSS, JavaScript, and images — counterpoint: complexity blurs what text browsing should provide.

### LLM perspective

- View: Text browsers are practical conformance probes because graceful degradation exposes where HTML semantics and implementations diverge.
- Impact: Developers serving accessible or high-security users should preserve useful reading and forms without CSS or JavaScript.
- Watch next: Track hidden, inert, dialog, and popover support across Lynx, ELinks, w3m, edbrowse, and Chawan.
