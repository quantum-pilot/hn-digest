# Bend 2 and the Vibe-Coding Trap

- Score: 310 | [HN](https://news.ycombinator.com/item?id=49753179) | Link: https://blog.liampwll.com/posts/bend_vibe_coding/

### TL;DR

The essay uses Bend 2 to argue that rapid AI-assisted implementation can preserve ignorance: builders may finish substantial systems before researching established approaches. It contrasts Bend’s 58-line game specification and 442-line proof with a shorter SPARK version discharged by GNATprove, then alleges Bend overlooked formal verification practice. HN largely agreed with the general “unknown unknowns” risk but challenged the example: Bend’s author had worked on formal verification years earlier, and commenters noted that automated SMT proofs and symbolic proofs offer different scalability and proof-authoring trade-offs.

### Comment pulse

- Vibe coding accelerates uninformed commitment → working output can deliver confidence before design exploration exposes prior art or better abstractions.
- The central example is factually weakened → Bend’s author publicly demonstrated formal-verification experience long before current coding agents.
- Proof systems make different trade-offs → automatic SMT discharge is concise, while explicit symbolic proofs may address properties that brute-force approaches cannot scale to.

### LLM perspective

- View: The essay identifies a real process hazard but undermines itself by insufficiently researching its chosen developer.
- Impact: Faster prototyping raises the value of literature review, domain experts, adversarial design critique, and explicit alternatives.
- Watch next: Compare Bend and SPARK on equivalent nontrivial systems, including specification size, solver limits, proof maintenance, and runtime performance.
