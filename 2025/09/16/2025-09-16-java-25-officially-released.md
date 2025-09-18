# Java 25 officially released

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45261946) | Link: https://mail.openjdk.org/pipermail/announce/2025-September/000360.html

- TL;DR
    - Java 25 (JDK 25) is GA and LTS, delivering 18 JEPs: scoped values, structured concurrency (preview), flexible constructor bodies, module import declarations, compact source files, KDF API, multiple JFR upgrades, AOT ergonomics, compact object headers, generational Shenandoah GC, and removal of 32-bit x86. HN split: praise for JVM stability/tooling vs. warnings about legacy upgrade pain and Oracle licensing anxiety. Many welcome cleaner language features and single-file ergonomics; debate continues over import terseness, readability, and IDE dependence.

- Comment pulse
    - JVM for backend stability and long-term compatibility → mature ecosystem, strong tooling; Clojure/Kotlin/Scala also benefit.
    - Caution on Oracle licensing and upgrades → fear of EULAs and brittle legacy dependencies — counterpoint: use OpenJDK vendors; many enterprises run Java widely.
    - Language ergonomics improving → flexible constructors, module imports, compact files; disagreement on import wildcards and IDE reliance for readability.

- LLM perspective
    - View: Java 25 cements JVM as conservative-but-modern; previews mature gradually without breaking deployed systems.
    - Impact: LTS will drive enterprise upgrades; GC and JFR gains help latency-sensitive services.
    - Watch next: Stabilization of structured concurrency/scoped values; Vector API graduation; vendor distributions and licensing guidance.
