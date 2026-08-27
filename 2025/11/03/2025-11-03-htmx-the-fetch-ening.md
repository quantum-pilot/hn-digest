# </> Htmx – The Fetch()ening

- Score: 325 | [HN](https://news.ycombinator.com/item?id=45803358) | Link: https://htmx.org/essays/the-fetchening/

### TL;DR

htmx is skipping version 3 and developing version 4 around a rewritten `fetch`- and async-based core, with an alpha available and a deliberately slow release path. Major changes include explicit attribute inheritance, network-based history restoration by default, built-in streaming and SSE support, Idiomorph swaps, a `<partial>` element, queued View Transitions, and more consistent events and extension hooks. The project promises perpetual htmx 2 support plus compatibility extensions, while identifying inheritance as the largest likely migration issue. Stable release is targeted for early-to-mid 2026.

### Comment pulse

- Readers welcomed perpetual version 2 support and the extended migration window.
- Naming of the new `inherited` marker drew debate, while the version-number joke amused some and confused others.

### LLM perspective

- View: The rewrite modernizes internals while treating compatibility as an operational commitment, not a slogan.
- Impact: Explicit inheritance and stable hooks should reduce hidden behavior but require careful template migration.
- Watch next: Alpha feedback on event ordering, history restoration, and extension compatibility.
