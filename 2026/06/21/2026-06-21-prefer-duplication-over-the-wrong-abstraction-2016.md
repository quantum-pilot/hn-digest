# Prefer duplication over the wrong abstraction (2016)

- Score: 414 | [HN](https://news.ycombinator.com/item?id=48620090) | Link: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction

## TL;DR
Sandi Metz argues that eliminating duplication too early often creates “wrong abstractions” that become brittle, condition-heavy, and hard to change. Developers then cling to these abstractions due to sunk-cost bias, piling on parameters and conditionals instead of rethinking the design. Her remedy: when an abstraction starts needing special cases, inline it back into each caller, accept duplication, and then re-extract clearer, more accurate abstractions. Going “backwards” like this typically makes features easier to add and code easier to understand.

## LLM perspective
- View: Treat abstractions as hypotheses; invalidate and replace them quickly when reality diverges.  
- Impact: Teams gain faster feature delivery, less fear of refactoring, and cleaner, domain-aligned designs.  
- Watch next: Add refactoring timeboxes, measure change friction, and codify “inline and rethink” as a standard practice.
