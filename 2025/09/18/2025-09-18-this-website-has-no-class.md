# This website has no class

- Score: 204 | [HN](https://news.ycombinator.com/item?id=45287155) | Link: https://aaadaaam.com/notes/no-class/

### TL;DR

The author rebuilt a personal site almost entirely without CSS classes, leaning on semantic HTML defaults, contextual selectors, custom tag names, and custom attributes for component variants. Modern nesting, `:where()`, and `:has()` helped, while the constraint reduced delivered CSS to about 5KB and improved accessibility through closer markup attention. He retained syntax-highlighting classes and would hesitate to scale the approach across a large team. Commenters called structure-coupled styling brittle, though several favored reducing generic divs and using classes only for exceptions.

### Comment pulse

- Classless styling suits stable documents — counterpoint: dynamic applications quickly need structural exceptions that turn clever selectors into maintenance hazards.
- Several readers preferred semantic elements and fewer divs without treating total class elimination as the goal.

### LLM perspective

- View: The constraint is a productive design exercise, but semantic markup and class elimination are related rather than identical goals.
- Impact: Small static sites may gain leaner CSS; multi-author applications risk coupling visual changes to fragile document structure.
- Watch next: Compare change effort, selector complexity, accessibility, performance, component reuse, and onboarding against a restrained class-based version.
