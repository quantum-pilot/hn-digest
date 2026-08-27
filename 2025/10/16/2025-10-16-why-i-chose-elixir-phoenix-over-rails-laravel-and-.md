# Why I Chose Elixir Phoenix over Rails, Laravel, and Next.js

- Score: 234 | [HN](https://news.ycombinator.com/item?id=45605291) | Link: https://akarshc.com/post/phoenix-for-my-project.html

### TL;DR

A solo developer chose Elixir and Phoenix for a project needing real-time updates, background jobs, concurrency, and resilience within one monolith. LiveView keeps UI state on the server and communicates over WebSockets, Oban handles jobs, and BEAM processes plus supervision localize failures. The author presents this as a constraint-driven choice rather than universal superiority, but understates competing capabilities: commenters note modern Rails includes WebSocket-based Hotwire, Solid Cable, and Solid Queue. Phoenix’s strongest differentiator is therefore its runtime and programming model, not exclusive possession of those features.

### Comment pulse

- Phoenix users praised LiveView component composition, Oban, concurrency, and stable integration ergonomics.
- Rails developers challenged claims that real-time messaging and jobs require substantial setup in current Rails releases.
- Commenters emphasized that WebSockets can be unnecessary overhead for ordinary sites and that framework familiarity still matters.

### LLM perspective

- View: Phoenix is compelling when persistent connections and isolated concurrency dominate; feature checklists alone do not settle the choice.
- Impact: A server-driven monolith can reduce cross-stack state coordination for a solo developer.
- Watch next: Prototype representative load, deployment, job recovery, frontend escape hatches, and team learning costs before committing.
