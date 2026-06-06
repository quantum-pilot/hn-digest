# Mythical Man Month

- Score: 343 | [HN](https://news.ycombinator.com/item?id=48046436) | Link: https://martinfowler.com/bliki/MythicalManMonth.html

- TL;DR  
    - Martin Fowler revisits Fred Brooks’s Mythical Man-Month, highlighting Brooks’s Law and the idea that large systems need strong conceptual integrity, even at the cost of omitted features. He recommends the anniversary edition including No Silver Bullet. Commenters connect these classics to modern practice: Lamport-style lightweight formal specs, AI-assisted programming’s limits without good theories, AI as “toolsmith,” and ongoing management failures that ignore communication costs. Others describe using explicit conceptual models and consistent patterns, enforced in PRs and even LLM prompts, to preserve coherence over time.

- Comment pulse  
    - Formal specs improve conceptual integrity → Lamport-style small models and TLA+ expose design flaws before code.  
    - AI tools aren't magic → speed coding, but weak theories and vague prompts yield messy systems — counterpoint: others value faster experimentation and parallel work.  
    - Brooks-style pathologies persist → teams grow without shared architecture; communication overhead, PR conflicts, and onboarding costs slow delivery despite more hires.

- LLM perspective  
    - View: Treat conceptual integrity as a first-class artifact: explicit domain models, invariants, and style guides shared across humans and AI.  
    - Impact: Orgs that invest in specs and architectural narratives will benefit more from AI assistants than those chasing coding speed.  
    - Watch next: Tooling that keeps LLM-generated code aligned with a living system model: schema checkers, property tests, lightweight formal methods.
