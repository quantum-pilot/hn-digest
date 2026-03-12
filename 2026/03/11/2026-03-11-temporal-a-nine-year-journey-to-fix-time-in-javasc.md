# Temporal: A nine-year journey to fix time in JavaScript

- Score: 477 | [HN](https://news.ycombinator.com/item?id=47336989) | Link: https://bloomberg.github.io/js-blog/post/temporal/

### TL;DR
Temporal is a new JavaScript time API that took nine years to design and standardize, aiming to fix the long-standing problems with `Date`. It clearly separates concepts like “instant in time” from “calendar date/time,” making DST and timezone handling far safer, at the cost of some verbosity and explicitness. Discussion centers on serialization and API style: object-oriented Temporal types vs JSON-friendly plain data and pure functions, plus appreciation for the long, community-driven standardization and implementation work.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Temporal greatly reduces common time bugs → explicit Instant vs calendar types and safer DST/timezone handling; extra verbosity beats late-night incident fixes.  
- Rich Temporal objects improve type safety and correctness → serialization is explicit via `.toString()`/`.from()` and revivers — counterpoint: some prefer plain JSON + date-fns-style pure functions.  
- Long road to standardization mirrors Python’s ISO8601 journey → volunteer-driven engine implementation and ports like `temporal_rs` show both complexity and strong ecosystem demand.

---

### LLM perspective
- View: Temporal will likely become the de facto standard for non-trivial JS time logic, with `Date` relegated to legacy use.  
- Impact: Web apps, APIs, and multi-time-zone systems gain fewer subtle bugs and clearer contracts between client, server, and databases.  
- Watch next: Full engine support, library/ORM integrations, migration guides, and benchmarks comparing Temporal polyfills vs native implementations.
