# Mago: A fast PHP toolchain written in Rust

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45232275) | Link: https://github.com/carthage-software/mago

- TL;DR
    - Mago is a Rust-based PHP toolchain (linter/formatter/static analyzer) aiming for ruff-like speed and a unified, modern UX. Docs tout linting rules, semantic checks, auto-fixes, and AST tools. HN feedback is cautious: early tests report many false positives due to missing PHPDoc/type handling and name resolution (even built-ins), suggesting immature beta quality. Commenters say speed won’t beat PHPStan/Psalm without parity and benchmarks, and clarify Mago targets tooling—not a PHP runtime. Users want a concrete roadmap and proof on real-world codebases.

- Comment pulse
    - Premature/beta quality → Missing PHPDoc and import/built-in resolution yields floods of false positives; parity with PHPStan/Psalm is prerequisite to switch.
    - Value case unclear → “Written in Rust” isn’t persuasive; users want benchmarks, stability guarantees, and a concrete parity roadmap — counterpoint: Rust tooling often delivers large productivity wins.
    - Positioning → Not a PHP runtime; think “ruff for PHP,” not uv; Composer already handles packages; focus is lint/format/type analysis.

- LLM perspective
    - View: Prioritize PHPDoc parsing, stdlib stubs, and correct name resolution; measure false-positive rate versus PHPStan/Psalm on public repos.
    - Impact: Faster CI and editor feedback for large monorepos; potential consolidation of multiple PHP tooling steps.
    - Watch next: Reproducible benchmarks, 1.0 parity checklist with dates, IDE integrations, plugin API, and PHP version support matrix.
