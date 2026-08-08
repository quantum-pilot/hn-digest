# I’ve banned query strings

- Score: 235 | [HN](https://news.ycombinator.com/item?id=48076173) | Link: https://chrismorgan.info/no-query-strings

### TL;DR

Chris Morgan’s personal site now rejects every query string because it currently uses none, treating appended referral and UTM parameters as unauthorized modifications and privacy-invasive tracking. If query parameters become necessary, only an allowlist will pass; malformed requests receive a deliberately humorous 414 response. HN found the standards surprisingly supportive: the query is part of a URL’s request interface, so unknown values need not be ignored. Debate centered on whether rejection protects users or punishes them, given legitimate uses such as search and older query-based routing.

### Comment pulse

- Standards-minded readers likened unknown parameters to unknown paths → servers may legitimately reject either, despite looser everyday conventions.
- Tracking tags bypass Referer privacy controls and pollute copied links → counterpoint: servers can simply discard them without breaking navigation.
- Query strings remain useful for search, routing, and constrained authentication → embedding tokens, however, makes copied URLs dangerous.

### LLM perspective

- **View:** Allowlisting is coherent for a static personal site, but unsuitable as a universal web rule.
- **Impact:** Link decorators lose attribution; visitors inherit failures they did not create.
- **Watch next:** Error-code choice, crawler behavior, archives, CDNs, and future features needing query semantics.
