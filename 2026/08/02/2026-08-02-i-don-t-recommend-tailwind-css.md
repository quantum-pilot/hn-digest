# I don't recommend Tailwind CSS

- Score: 153 | [HN](https://news.ycombinator.com/item?id=49141891) | Link: https://en.andros.dev/blog/af3ee191/why-i-dont-recommend-tailwind-css/

### TL;DR

The author credits Tailwind for fast interfaces, good documentation, autocomplete, and component-friendly colocation, but argues its utility vocabulary, long class lists, arbitrary values, generated cascade order, and debugging friction impose deferred costs. Modern CSS now supplies nesting, layers, variables, container queries, `:has()`, and color mixing without a framework. The recommendation is contextual: learn CSS first, favor native or modular CSS for small and server-rendered work, and consider Tailwind where component systems and large teams benefit from shared constraints. HN remained sharply split over readability and local reasoning.

### Comment pulse

- Supporters report durable projects and fast onboarding; conventions reduce rediscovery and keep styling beside components.
- Utility conflicts resolve by generated stylesheet order, not HTML order — counterpoint: advocates call conflicting classes a design smell handled through states or merge tooling.
- CSS Modules and scoped component styles offer local reasoning without class soup, while Tailwind remains attractive for DOM-coupled layout and typography.

### LLM perspective

- View: Tailwind changes where coordination cost lives: from selector naming and stylesheet navigation to utility fluency and markup density.
- Impact: Architecture matters more than ideology; server templates, component libraries, design systems, and application layouts benefit from different styling boundaries.
- Watch next: Compare onboarding time, production debugging, bundle complexity, token consistency, dark-mode changes, and long-term refactoring across equivalent projects.
