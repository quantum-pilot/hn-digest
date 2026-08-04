# Project Valhalla, Explained: How a Decade of Work Arrives in JDK 28

- Score: 531 | [HN](https://news.ycombinator.com/item?id=48595511) | Link: https://www.jvm-weekly.com/p/project-valhalla-explained-how-a

### TL;DR

JEP 401 is targeting JDK 28 as a disabled-by-default preview, introducing value classes: reference types whose instances lack identity, have final fields, cannot be synchronized upon, and compare with == by substitutability. This lets the JVM scalarize or flatten qualifying values, reducing allocations, headers, indirection, and cache misses while preserving class abstractions. However, null-restricted types, wider flattening, and specialized generics remain future work. HN welcomed Valhalla’s progress but sharply criticized the article’s likely LLM-generated prose and a Point[] example that contradicted its own 64-bit-plus-null limitation.

### Comment pulse

- The flagship array example appears invalid today → two ints plus null state exceed the documented 64-bit atomic-flattening budget — counterpoint: larger-value flattening is planned.

- Readers objected to suspected AI authorship → repetitive emphatic prose and an unreplaced image placeholder undermined trust in otherwise valuable technical material.

- Design debate centers on nullability → critics preferred explicit nullable and non-null projections; defenders said null restrictions are simply being delivered incrementally.

### LLM perspective

- **View:** The feature’s staged scope is reasonable, but preview adopters must distinguish semantic guarantees from optimization opportunities.

- **Impact:** Performance-sensitive Java libraries can begin modeling identity-free domain values, while generic collections remain reference-shaped.

- **Watch next:** Benchmark real layouts, validate identity-dependent code, test wrapper migration, and track null restrictions and specialized-generics JEPs.
