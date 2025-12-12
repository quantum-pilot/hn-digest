# Patterns.dev

- Score: 568 | [HN](https://news.ycombinator.com/item?id=46226483) | Link: https://www.patterns.dev/

### TL;DR
Patterns.dev is a web resource on software and UI design patterns, prompting debate about their real-world value. Commenters see patterns mainly as a shared vocabulary for recurring solutions, invaluable in large enterprise codebases but often harmful when blindly imposed on simpler JavaScript or Go projects. Several note that juniors over-index on “Gang of Four” catalogs instead of fundamentals like data structures and complexity. Others recall Yahoo’s old UX pattern library and modern component galleries as proof that naming common UI behaviors speeds collaboration.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Patterns emerge naturally; naming them (Adapter, Builder, Singleton) makes cross-team communication easier, especially on big .NET/Java systems with many similar services.
- Misapplied patterns—especially enterprise OOP idioms transplanted into old JavaScript—produce needless factories/facades, confusing object lifecycles, and harder debugging than straightforward code.
- Seniors emphasize basics: pick good data structures (e.g., hash-join style lookups) and simple loops before reaching for textbook patterns or “architecture astronautics.”

---

### LLM perspective
- View: Treat patterns as descriptive labels for recurring designs, not prescriptions to satisfy; start from clarity and requirements, then name what you already built.
- Impact: Teams gain from common terminology but avoid language-mismatched abstractions when they respect each language’s native idioms and standard libraries.
- Watch next: Prefer resources that pair each pattern with failure modes, alternatives, and concrete code size/complexity comparisons across languages and project scales.
