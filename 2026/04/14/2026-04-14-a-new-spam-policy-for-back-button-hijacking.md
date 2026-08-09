# A new spam policy for “back button hijacking”

- Score: 818 | [HN](https://news.ycombinator.com/item?id=47760764) | Link: https://developers.google.com/search/blog/2026/04/back-button-hijacking

### TL;DR

Google announced a spam policy targeting “back button hijacking,” where sites manipulate history or navigation so Back sends users somewhere other than their prior page. The supplied article capture contains mostly Search Central navigation rather than policy details, so the discussion carries the substance: LinkedIn, Reddit, and Facebook were cited for funneling visitors into feeds; redirects, History API calls, and intercepted shortcuts can produce similar symptoms. Commenters welcomed browser-level defenses but warned that SPAs need legitimate history control and that Android apps remain major offenders.

### Comment pulse

- LinkedIn’s replace-then-push sequence makes Back open its feed; readers reported comparable behavior on Reddit and Facebook.
- Browser-wide shortcut blocking appealed to users frustrated by Ctrl+F, Ctrl+click, and Alt+Left interception — counterpoint: trusted apps sometimes need shortcuts.
- Firefox users described defenses and fewer recent problems — counterpoint: redirects can recreate hijacking without pushState, while SPAs rely on history legitimately.

### LLM perspective

- **View:** Back navigation is a user-control contract; deliberate diversion into engagement feeds is a dark pattern regardless of implementation.
- **Impact:** Search penalties may deter publishers, but browser-enforced invariants would protect users before ranking systems detect abuse.
- **Watch next:** Google’s policy definition, enforcement examples, treatment of legitimate SPAs, and equivalent protections in Chrome and Android.
