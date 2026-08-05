# Prevent cognitive debt by manually retyping LLM-generated code

- Score: 531 | [HN](https://news.ycombinator.com/item?id=49153374) | Link: https://ankursethi.com/blog/prevent-cognitive-debt-by-manually-retyping-llm-generated-code/

### TL;DR

To avoid cognitive debt, the author instructs coding agents never to modify files automatically. The model proposes code and commands in chat; he manually types, checks, reorganizes, and adapts every change. He estimates this is about twice as fast as working unaided, far below claimed tenfold gains, but says the forced pace catches hallucinations and preserves a spatial mental model of personal projects. HN split sharply: some recognized the old learning value of retyping, while others considered it wasteful or preferred delegating implementation to focus on product-level decisions.

### Comment pulse

- Manual entry creates comprehension checkpoints → each line forces interaction with APIs, assumptions, location, and surrounding design.
- Efficiency is contested → deep review plus retyping may cost more than writing directly — counterpoint: suggestions can reveal better approaches.
- Abstraction changes the valued skill → some enjoy building rather than coding, while critics warn technical judgment decays without implementation practice.

### LLM perspective

- View: Retyping is deliberate learning, not a universally efficient production workflow.
- Impact: Solo developers retain ownership; teams need lighter mechanisms that prove comprehension without duplicating every keystroke.
- Watch next: Experiments measuring delayed maintenance, debugging accuracy, onboarding, and codebase recall across agent workflows.
