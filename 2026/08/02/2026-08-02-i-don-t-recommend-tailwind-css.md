# I don't recommend Tailwind CSS

- Score: 153 | [HN](https://news.ycombinator.com/item?id=49141891) | Link: https://en.andros.dev/blog/af3ee191/why-i-dont-recommend-tailwind-css/

- TL;DR  
  The article argues against Tailwind CSS, claiming its utility-class approach, reliance on CSS cascade, and non-semantic naming create fragile, illogical styling and poor long-term maintainability. HN commenters split: some say Tailwind massively improves onboarding, consistency, and local reasoning for everyday app UIs, and that the author over-theorizes developer behavior. Others point to modern CSS (nesting, variables, modules, scoped styles) and design-system patterns as cleaner, more future-proof alternatives that retain semantic structure without Tailwind’s long class strings.  

  *Content unavailable; summarizing from title and comments.*

- Comment pulse  
  - Tailwind speeds teams → shared utilities reduce CSS naming and keep styles near markup — counterpoint: critics say beginners still struggle and scoped CSS suffices.  
  - Seasoned CSS devs distrust Tailwind → see random cascade resolution and long utility chains as inline-style rebranded, preferring semantic classes, variables, CSS Modules.  
  - Nuanced view → keep design tokens and components in CSS or design systems, but use Tailwind-like utilities for layout/typography tightly coupled to DOM structure.  

- LLM perspective  
  - View: Tailwind fits product teams wanting fast UI and minimal CSS mental load, but clashes with semantic, token-driven design systems.  
  - Impact: Backend-leaning teams, prototypes, and internal tools gain most; design-system teams and accessibility specialists may prefer explicit CSS architecture.  
  - Watch next: Watch browser support for nesting, cascade layers, and mixins; if standardized, they narrow Tailwind’s advantages while keeping CSS idiomatic.
