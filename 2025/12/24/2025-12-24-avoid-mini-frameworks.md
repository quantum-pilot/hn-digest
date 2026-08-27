# Avoid Mini-Frameworks

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46374856) | Link: https://laike9m.com/blog/avoid-mini-frameworks,171/

### TL;DR

The author warns against small-team wrappers that impose new concepts over an organization's shared framework. One such layer turned an expected easy migration into roughly a year of work and made a one-day feature take two weeks. These abstractions tend to cover only common cases, leak underlying details, fragment stacks, and become abandoned when their creators leave. The recommendation is to prefer focused libraries and utilities; a genuine framework should model durable business needs and receive major-decision scrutiny.

### Comment pulse

- Readers disputed the author's terminology, favoring the conventional inversion-of-control distinction between libraries and frameworks.
- Others accepted narrowly justified adapters but agreed essential complexity and maintenance ownership cannot be abstracted away.

### LLM perspective

- View: The sharpest warning concerns organizational ownership, not abstraction itself.
- Impact: A convenience layer can quietly transfer complexity from its authors to every adopter.
- Watch next: Require repeated use cases, escape hatches, and named maintainers before standardizing an internal wrapper.
