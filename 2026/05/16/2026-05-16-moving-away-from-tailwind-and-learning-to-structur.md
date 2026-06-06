# Moving away from Tailwind, and learning to structure my CSS

- Score: 403 | [HN](https://news.ycombinator.com/item?id=48158400) | Link: https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/

### TL;DR
Julia Evans describes migrating sites from Tailwind to semantic HTML plus hand-structured CSS, reusing Tailwind-inspired systems (reset, tokens, utilities) while designing her own conventions: component-scoped styles, a central color and type scale, minimal global “base” rules, and grid-heavy responsive layouts that need fewer media queries. Reasons for leaving Tailwind include its build-system dependence, large bundles, limits on “weird” CSS, messy coexistence with plain CSS, and discomfort with how it can devalue serious CSS expertise. HN commenters debate Tailwind’s effects on semantics, pedagogy, and productivity.

### Comment pulse
- Tailwind harms semantic HTML and accessibility → encourages CSS-first workflows and div soup for learners — counterpoint: accessibility is about author choices, not utilities.  
- Tailwind is a pragmatic choice → reduces custom CSS, speeds development, aligns with LLM support, and lets full-stack devs focus on backends and business logic.  
- Alternatives like ITCSS and CSS Modules appeal → keep cascade, improve tooling and readability; many praise Evans’ approachable style as a model for communication.  

### LLM perspective
- View: Treat frameworks like Tailwind as temporary scaffolding; periodically rewrite using native CSS to internalize patterns and reduce dependencies.  
- Impact: Teams that invest in semantic HTML and design tokens gain easier theming, accessibility audits, and safer large-scale refactors.  
- Watch next: Tooling that blends utility classes with component-scoped CSS and layout primitives like grid, container queries, and subgrid.
