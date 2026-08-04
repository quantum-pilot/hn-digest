# Moving away from Tailwind, and learning to structure my CSS

- Score: 403 | [HN](https://news.ycombinator.com/item?id=48158400) | Link: https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/

### TL;DR

After eight years using Tailwind, Julia Evans migrated a couple of sites to semantic HTML and vanilla CSS, retaining the framework’s useful discipline: a reset, design tokens, utilities, and consistent scales. She now isolates styles by component, centralizes colors and typography, gives parent layouts responsibility for spacing, uses CSS Grid to reduce breakpoints, and keeps builds optional with esbuild. Her motivations include 2.8MB legacy stylesheets, mixed styling systems, creative limits, and respect for CSS expertise. HN split sharply between semantic, maintainable CSS and Tailwind’s localized, fast, team-friendly workflow.

### Comment pulse

- Semantic concerns dominate → critics link utility-first thinking to div soup — counterpoint: proponents say markup quality remains a developer choice.
- Maintenance trade-offs stay subjective → bespoke cascades can become fragile; localized class soup improves debugging but sacrifices readability and interactive tooling.
- Alternatives broaden the choice → commenters proposed CSS Modules for collision-free classes and ITCSS for ordered specificity, rather than choosing either extreme.

### LLM perspective

- **View:** The migration succeeds because it replaces a framework with explicit constraints, not unconstrained authoring.
- **Impact:** Small-site maintainers gain direct access to native features; teams must document conventions previously encoded by Tailwind.
- **Watch next:** Compare bundle size, change isolation, breakpoint count, accessibility audits, onboarding time, and maintenance defects across implementations.
