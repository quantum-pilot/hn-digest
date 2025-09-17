# Public static void main(String[] args) is dead

- Score: 189 | [HN](https://news.ycombinator.com/item?id=45258098) | Link: https://mccue.dev/pages/9-16-25-psvm

- TL;DR
  - Java now lets single-file programs run without public static void main via JEP 445’s unnamed classes and instance main methods, simplifying “Hello, World!” and quick scripts. HN splits: teachers/beginners welcome less boilerplate; some valued the old incantation for teaching Java’s model. Practitioners say it barely affects large projects or Android, where frameworks own the entry point. Critics note it’s single-file–only—so main isn’t “dead”—and want package-level functions or broader procedural allowances.
  - *Content unavailable; summarizing from title/comments.*

- Comment pulse
  - Less boilerplate aids beginners → fewer magic words before printing, improving approachability—counterpoint: the old incantation taught types, classes, and entry-point semantics progressively.
  - Little day-to-day change → large Java codebases and Android rely on frameworks; developers seldom touch main directly.
  - Scope is narrow → JEP 445 targets single-file sources; public static void main remains. Desire: package-level functions, multiple classes per file, procedural-friendly entry.

- LLM perspective
  - View: Ergonomic sugar for scripts and teaching, not a shift in Java’s programming model.
  - Impact: Educators, bootcamps, newcomers; also CLIs, containers, and coding tests via faster write-run cycles.
  - Watch next: Track JEP 445 graduation, IDE/template updates, JShell integration, and possible loosening of file-level restrictions.
