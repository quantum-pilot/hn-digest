# Rating 26 years of Java changes

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45551450) | Link: https://neilmadden.blog/2025/09/12/rating-26-years-of-java-changes/

- TL;DR
    - An HN thread rates 26 years of Java changes, sparking debate over what mattered most: annotations, the Collections renaissance, or the JVM itself. Many argue annotations deserve high marks for enabling DI/Spring and cutting boilerplate; others decry implicit “magic.” Streams and checked exceptions are called overengineered/underused, while modules remain unpopular. A long view credits HotSpot/JIT and Sun’s freemium strategy for dominance. Design choices (e.g., lambda typing to functional interfaces) highlight Java’s bias toward stability over elegance; some favor Kotlin for ergonomics.
    - Content unavailable; summarizing from title/comments.
- Comment pulse
    - Annotations are hugely impactful → enabled DI frameworks and configuration, reduced boilerplate; entire Spring apps are annotations-only — counterpoint: implicit wiring is brittle, encourages magic.
    - Streams/checked exceptions misfires → stream design overcomplicated for rare parallelism; checked exceptions widely ignored.
    - Big-picture matters more → HotSpot/JIT and Sun’s free language + paid VM model drove adoption; Bloch’s Collections set enduring API design norms.
- LLM perspective
    - View: Debate reflects tension between stability, backward compatibility, and ergonomic evolution; Java optimizes for predictability over novelty.
    - Impact: Enterprise teams keep Spring/DI and Collections idioms; some migrate ergonomics to Kotlin while retaining JVM and libraries.
    - Watch next: Measure Loom virtual threads versus async/await; track module adoption, pattern matching/Valhalla rollouts, and real-world stream parallelism benefits.
