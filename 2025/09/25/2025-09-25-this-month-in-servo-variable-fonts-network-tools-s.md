# This month in Servo: variable fonts, network tools, SVG

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45373501) | Link: https://servo.org/blog/2025/09/25/this-month-in-servo/

### TL;DR

Servo merged a record 447 pull requests in August, adding inline SVG, a network monitor, debugger breakpoint discovery, variable-font support, and named CSS grid areas. Several newer capabilities remain preference-gated, including variable fonts, IndexedDB, and Trusted Types. The engine also eliminated stale-display-list hit-test crashes, capped rendering at 60 FPS, reduced animated-image work, cut 16MB of ICU code, and reached 80% WebDriver conformance. Commenters welcomed momentum but debated whether Servo’s realistic future is an embeddable engine rather than a full browser competitor.

### Comment pulse

- Browser-choice optimism → supporters want a Rust engine challenging Chromium; skeptics stress Servo’s embedding focus and missing basics like scrollbars.
- Sponsorship discussion → commenters noted Igalia’s paid contributors while questioning how Servo compares with WPE WebKit.

### LLM perspective

- View: Breadth plus stability work signals maturation, but preference gates distinguish shipped foundations from user-ready completeness.
- Impact: Embedders gain a more capable Rust engine; standalone-browser expectations remain substantially ahead of current product scope.
- Watch next: Default-enabled features, WebDriver and WPT progress, scrollbar support, benchmark CI, and real embedding deployments.
