# Temporal: A nine-year journey to fix time in JavaScript

- Score: 477 | [HN](https://news.ycombinator.com/item?id=47336989) | Link: https://bloomberg.github.io/js-blog/post/temporal/

### TL;DR

After nine years, JavaScript’s Temporal reached TC39 Stage 4 for ES2026, replacing Date’s mutable, ambiguous, millisecond-only model with explicit immutable types for instants, zoned datetimes, plain calendar values, and durations. It handles daylight-saving transitions, IANA time zones, non-Gregorian arithmetic, and nanosecond timestamps. The unusually large specification has about 4,500 tests; a shared Rust implementation, temporal_rs, helped multiple engines converge. Firefox, Chrome, and Edge already support it, while Safari is partial. Commenters welcome safer semantics but note rich objects still require explicit reconstruction after JSON transfer.

### Comment pulse

- Verbosity buys correctness → choosing Instant, PlainDate, or ZonedDateTime forces developers to state what kind of time they mean.
- Serialization remains deliberate → ISO strings round-trip, but JSON cannot infer which Temporal type should be rebuilt without a reviver.
- Standards work was unusually collaborative → a volunteer built Firefox’s implementation, while companies funded champions and a reusable engine library.

### LLM perspective

- **View:** The API addresses modeling errors, not time’s complexity; users must still choose calendars, zones, and boundary policies.
- **Impact:** Applications can retire many date libraries once target runtimes and web APIs finish integration.
- **Watch next:** Safari and Node support, date-picker bindings, cookie APIs, bundle migration, and timezone-data consistency.
