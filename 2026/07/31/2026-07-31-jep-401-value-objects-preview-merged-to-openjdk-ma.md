# JEP 401: Value Objects (Preview) merged to OpenJDK master

- Score: 224 | [HN](https://news.ycombinator.com/item?id=49119063) | Link: https://github.com/openjdk/jdk/pull/31120

## TL;DR
JEP 401 merges preview support for value objects into OpenJDK, delivering the first tangible piece of Project Valhalla’s long-promised value types. Value objects are identity‑free data carriers with predictable layout, aimed at reducing heap allocations and improving performance while preserving Java’s backward compatibility ethos. Commenters are enthusiastic, praising the thoughtful design (multiple “buckets” of value-ness), expected performance gains, and Java’s cautious evolution, while contrasting Java’s steady progress with JavaScript’s stalled records/tuples and slower modernization.  
*Content unavailable; summarizing from title and comments.*

## Comment pulse
- Value objects seen as long-missing performance tool → identity‑free data shapes, multiple Valhalla “buckets” let APIs trade semantics for predictable layout and speed.  
- This JEP is only phase one of Valhalla → later nullability constraints and generic specialization expected to unlock larger performance wins across collections.  
- Java’s compatibility‑first evolution praised for enterprise stability → language feels modern, but cultural issues (verbose patterns, heavy frameworks) persist—counterpoint: versus JavaScript, Java’s feature pace impresses.

## LLM perspective
- View: Value objects move Java closer to data‑oriented design, especially for numerics, serialization, and game/finance workloads.  
- Impact: Library authors can gradually introduce value-based APIs without breaking callers, then rely on JIT to flatten and optimize.  
- Watch next: Benchmarks of collections, records, and domain models implemented as value objects, plus JEPs covering nullability and generic specialization.
