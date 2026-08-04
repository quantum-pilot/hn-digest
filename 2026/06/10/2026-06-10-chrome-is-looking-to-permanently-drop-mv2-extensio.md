# Chrome is looking to permanently drop MV2 extension

- Score: 415 | [HN](https://news.ycombinator.com/item?id=48471970) | Link: https://www.neowin.net/news/google-chrome-is-killing-all-ublock-origin-bypasses-microsoft-edge-opera-to-follow/

### TL;DR

Chrome is deleting controls and code paths that kept Manifest V2 extensions alive, ending registry and flag-based bypasses around Chromium 150–151. Google cites security bugs, complexity, and technical debt; the practical casualty is full uBlock Origin, while its MV3-based Lite version remains available with reduced capabilities. Opera says MV2 will continue temporarily, and Firefox supports both manifests. HN users framed effective blocking as essential to a tolerable web, but some found Lite sufficient; others remain on Chromium for speed, compatibility, developer testing, and features despite Google’s advertising incentives.

### Comment pulse

- MV3 is not inherently the blocker → Firefox retains full WebRequest support; Chrome’s restricted API design is the decisive limitation.
- Chromium remains sticky → faster rendering, workspaces, site compatibility, and representative testing outweigh privacy objections for some users.
- Alternative browsers preserve choice → counterpoint: Firefox compatibility gaps and Orion’s reported jank, memory issues, and incomplete Linux release hinder migration.

### LLM perspective

- **View:** Extension security policy should constrain dangerous behavior without centralizing control over legitimate user-side filtering.
- **Impact:** Developers must target divergent extension APIs or abandon capabilities, while users absorb migration and browser-switching costs.
- **Watch next:** Test Chromium 151, Opera’s exception policy, Firefox WebRequest parity, and real-world blocking differences between uBO and Lite.
