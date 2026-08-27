# Spec-Driven Development: The Waterfall Strikes Back

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45935763) | Link: https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html

### TL;DR

The author argues AI-oriented spec-driven development recreates waterfall by generating verbose requirements, designs, and task files before code. In his tests, agents missed repository context, repeated themselves, embedded code requiring duplicate review, ignored specifications, and marked testing complete without tests; benefits also declined on mature codebases. He recommends iterating through small experiments around risky assumptions instead. Commenters split sharply: some report strong returns from concise acceptance criteria and executable tests, while others say heavyweight prose delays feedback and merely relocates probabilistic errors into specification interpretation.

### Comment pulse

- Planning advocates distinguish short, revisable ticket specs from rigid multi-month waterfall and credit upfront acceptance criteria with reducing rework.
- Iteration advocates say detailed prose commits teams to misunderstood solutions — counterpoint: cheap AI cycles can make revision substantially faster.

### LLM perspective

- View: The useful boundary is executable clarity, not whether a document is called a specification.
- Impact: Teams may trade coding time for review burden unless specs shorten feedback and expose correctness.
- Watch next: End-to-end cycle time, defect rates, spec drift, test coverage, and performance on mature repositories.
