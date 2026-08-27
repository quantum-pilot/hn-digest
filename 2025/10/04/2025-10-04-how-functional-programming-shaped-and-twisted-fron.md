# How functional programming shaped and twisted front end development

- Score: 116 | [HN](https://news.ycombinator.com/item?id=45473019) | Link: https://alfy.blog/2025/10/04/how-functional-programming-shaped-modern-frontend.html

### TL;DR

The essay argues that functional-programming ideals helped React-era frontends tame jQuery-era state but encouraged developers to fight the web platform. It links immutability and framework-controlled state to CSS isolation, synthetic events, hydration, client routing, controlled forms, and reimplemented native widgets, trading browser capabilities for complexity and weaker progressive enhancement. The author recommends server-rendered HTML, native elements, CSS, and selective JavaScript through tools such as HTMX, Astro, Qwik, Remix, and SvelteKit. Commenters dispute the causal story, noting browser inconsistencies, recent or experimental standards, compatibility obligations, and React’s imperfect functional character.

### Comment pulse

- Critics called several examples historical straw men because native dialog and customizable selects became broadly usable only recently.
- Supporters agreed frameworks can outlive their original necessity and urged renewed CSS and platform knowledge.

### LLM perspective

- View: Framework excess is real, but organizational scale and delayed browser convergence explain more than functional ideology alone.
- Impact: Defaulting every site to application architecture increases JavaScript, accessibility work, hydration risk, and maintenance cost.
- Watch next: Teams should periodically retest whether newly stable platform primitives can replace framework code without sacrificing requirements.
