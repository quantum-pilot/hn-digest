# Project Valhalla, Explained: How a Decade of Work Arrives in JDK 28

- Score: 531 | [HN](https://news.ycombinator.com/item?id=48595511) | Link: https://www.jvm-weekly.com/p/project-valhalla-explained-how-a

## TL;DR

Project Valhalla’s first deliverable, JEP 401, will land in JDK 28 as a preview: `value` classes (“codes like a class, works like an int”) which have no identity but are still reference types and thus nullable. The JVM can scalarize and, where size and atomicity allow, heap‑flatten these into dense layouts, dramatically improving locality and boxing costs (e.g., for `Integer`). This step doesn’t yet include non‑nullable value types or specialized generics, so flat `List<Point>` remains future work. Discussion mixes excitement, skepticism about design trade‑offs, and criticism that the article itself feels AI‑generated and contains technical sloppiness.

---

## Comment pulse

- Article quality concerns → repetitive phrasing, AI‑like images and a 64‑bit/`Point` flattening inconsistency led many to dismiss it as LLM‑written “slop.”  
- Nullability and projections → some argue dual value/reference projections and non‑null types aren’t “mentally heavy” and would strengthen guarantees—counterpoint: OpenJDK is deferring them, not rejecting them.  
- Java/Valhalla trajectory → split between “Java is playing catch‑up, poorly stewarded” and “modern JVM is excellent; Oracle/OpenJDK have accelerated evolution while preserving compatibility.”

---

## LLM perspective

- View: Treat JEP 401 as a semantics change first; only then chase performance wins in hot paths.  
- Impact: Biggest benefits will accrue to library/infra authors (collections, numerics, codecs) once they adopt value classes.  
- Watch next: Benchmark EA builds, track null‑restricted types and specialized generics JEPs, and watch how primitive wrappers’ migration impacts real‑world code.
