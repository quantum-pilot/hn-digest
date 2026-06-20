# Datasette Apps: Host custom HTML applications inside Datasette

- Score: 137 | [HN](https://news.ycombinator.com/item?id=48593731) | Link: https://simonwillison.net/2026/Jun/18/datasette-apps/

- TL;DR
    - Datasette Apps is a new plugin that lets you host self-contained HTML+JS apps directly inside Datasette, in hardened sandboxed iframes that can run read-only SQL and carefully controlled writes via stored queries. Security relies on iframe sandboxing, an immutable CSP set via a meta tag, and MessageChannel-based APIs, plus visible logs for SQL and CSP errors. Willison used multiple LLMs for design and security review. HN readers frame this as part of a broader “bring-your-own UI over data” trend.

- Comment pulse
    - Context: commenters restate Datasette as a data-publishing platform for journalists, governments, researchers, etc., and compare it with Observable Framework and other notebook/dashboard tools.
    - Pattern: many see a trend toward BYO UI over databases (Motherduck dives, Snowflake+Streamlit, iframe React apps) replacing rigid dashboards—counterpoint: still risks ecosystem lock‑in.
    - Security and dev UX: readers like browser sandbox/CSP primitives but fear subtle bugs; they also request Git-backed app sources and simpler SQLite-first web stacks.

- LLM perspective
    - View: Turns Datasette into a lightweight, multi-tenant app runtime for data-centric tools, not just an API and table browser.
    - Impact: Non-web-specialist teams can ship custom interfaces near their data, while central admins retain tight SQL, CSP, and permission control.
    - Watch next: Key questions: real-world sandbox escapes, how far write-enabled apps go, and whether filesystem-backed apps become first-class for versioning.
