# Pretext: TypeScript library for multiline text measurement and layout

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47556290) | Link: https://github.com/chenglou/pretext

## TL;DR

Pretext is a TypeScript library that predicts multiline text layout and height purely in JS, without touching the DOM, by segmenting text, measuring via canvas, and reimplementing browser line-breaking rules. It supports complex scripts, emojis, and bidi text, and exposes APIs for both “just give me the height” and fully manual line layout to render via DOM, Canvas, SVG, or custom UIs. HN discussion praises the engineering difficulty, notes CSS/standards gaps, and flags cross-browser edge cases and maintenance risks.

## Comment pulse

- This fills a long-missing gap: accurate pre-render text measurement unlocks virtualization, custom layouts, subtitles, and advanced UI patterns previously built with hacks.
- Core insight is exhaustive reproduction of browser behavior and per-browser measurement quirks; some suspect AI-assisted dev made this feasible now — counterpoint: long-tail edge cases may be unmaintainable.
- Several examples already have partial CSS equivalents (`interpolate-size`, `text-wrap: balance|pretty`), but commenters argue a native browser text-measurement API is still needed.

## LLM perspective

- View: This is effectively a userland “text layout engine,” proving feasibility and clarifying what a standardized browser API should expose.
- Impact: Front-end frameworks, design tools, and editors gain reliable pre-layout sizing without DOM thrash, especially valuable for complex scripts.
- Watch next: Cross-browser accuracy reports, performance benchmarks at scale, and any movement toward a W3C proposal for text-measurement / line-layout primitives.
