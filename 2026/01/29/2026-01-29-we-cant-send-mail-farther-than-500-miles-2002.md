# We can’t send mail farther than 500 miles (2002)

- Score: 635 | [HN](https://news.ycombinator.com/item?id=46805665) | Link: https://web.mit.edu/jemorris/humor/500-miles

### TL;DR

A campus statistics department reported that email delivery stopped beyond roughly 500 miles, and its map proved reproducible. A consultant’s operating-system upgrade had silently downgraded Sendmail 8 to version 5 while retaining the newer configuration file. Version 5 ignored long option names and, lacking compiled defaults, set the remote connection timeout to zero—about three milliseconds on that loaded server. Because the campus network introduced unusually little local routing delay, connection success correlated strongly with light-travel distance, producing an apparently geographic email boundary near 559 miles.

### Comment pulse

- Readers praise the statisticians for collecting precise, geographically organized reproduction data instead of hiding an observation that sounded impossible.
- Similar tales involve mouse urine shorting a cold computer, ice-cream-dependent car starts, and video frames triggering power or decoder failures.
- Repeated reposts remain popular because the root cause is memorable and rewards humility before contradictory evidence.

### LLM perspective

- View: Treat bizarre user reports as measurements to reproduce, not theories to dismiss.
- Impact: Cross-version configuration tolerance can convert missing defaults into failures that masquerade as physical laws.
- Watch next: Validate software/config compatibility after upgrades, make timeouts explicit, inspect banners, and test observed boundaries systematically.
