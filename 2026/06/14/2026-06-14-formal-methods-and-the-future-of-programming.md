# Formal methods and the future of programming

- Score: 296 | [HN](https://news.ycombinator.com/item?id=48526633) | Link: https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1

### TL;DR
Yaron Minsky explains why Jane Street, long skeptical of heavyweight formal methods, is now building a formal methods team: LLM-based “agentic coding” generates lots of sloppy code, making verification the new bottleneck. Strong type systems and proofs can both constrain agents and feed them rich automated feedback, turning exhaustive guarantees from luxury into necessity. HN discussion explores past attempts at automation, debates the practicality and accessibility of industrial logics, and anticipates LLMs drastically lowering the human cost of writing proofs.

### Comment pulse
- Automation vs new logics → Some veterans argue practical success needs language-integrated, highly automated provers; others credit LTL, separation logic, TLA+ as industrial breakthroughs.
- Luxury vs necessity → Startups favor “offensive programming”; HFT-like domains need zero-defect systems where post-hoc fixes are impossible—GenAI may shrink defensive overhead.
- What specs buy you → Replies stress ∀-style guarantees and SAT/SMT exhaustiveness for concurrency and hardware, beyond tests’ sampled behaviors.

### LLM perspective
- View → LLM agents make formal methods less niche by absorbing proof grunt-work; success hinges on keeping specs readable, composable, reviewable.
- Impact → Most leverage will be in safety-critical, concurrent, or highly regulated systems; mainstream app code will adopt lighter type-level specs first.
- Watch next → Watch integrated stacks where language, verifier, and LLM co-design evolve, and benchmarks comparing AI-assisted proofs vs traditional testing on outages.
