# What my dad taught me about AI coding in the 90s

- Score: 144 | [HN](https://news.ycombinator.com/item?id=49419381) | Link: https://askmike.org/articles/ai-coding-lessons-in-the-90s-from-my-dad/

### TL;DR

Using blindfold chess as a contrast, the author argues that effective AI-assisted programming still requires a strong mental model of components, interfaces, and goals, even when the programmer reads or writes little code. Experienced developers may steer agents better, but boredom and convenience can weaken attention and ownership. Commenters challenge the analogy because chess state is fully observable and deterministic, whereas agent output can change a codebase unpredictably. Several suggest rapid chess is closer: experts can review everything, but only under intense pace.

### Comment pulse

- Expertise improves steering → domain knowledge helps frame problems and diagnose failures before context windows or agents wander.
- Unreviewed output breaks the board model → summaries cannot guarantee interfaces, concurrency behavior, or hidden implementation choices.
- Understanding decays anyway → even hand-written systems become unfamiliar, making explicit contracts and refreshed review essential.

### LLM perspective

- View: The durable skill is maintaining verified system invariants, not memorizing every implementation detail or trusting prose descriptions.
- Impact: Senior engineers may gain speed, while novices risk producing systems whose failure modes they cannot recognize.
- Watch next: Compare comprehension, debugging time, and interface violations across reviewed, unreviewed, and manually written changes.
