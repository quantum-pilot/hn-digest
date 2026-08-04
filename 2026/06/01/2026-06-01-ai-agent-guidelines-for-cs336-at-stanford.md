# AI Agent Guidelines for CS336 at Stanford

- Score: 300 | [HN](https://news.ycombinator.com/item?id=48359232) | Link: https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md

### TL;DR

Stanford’s CS336 repository instructs coding agents to act as teaching assistants, not assignment solvers. They may explain concepts and errors, review student-written code, ask guiding questions, recommend course materials, and suggest tests, invariants, toy inputs, profiling, or ablations. They must not write code or pseudocode, fill TODOs, edit repositories, run commands, reveal solution ideas, or point to outside implementations. HN readers welcomed a coaching model over blanket AI bans but doubted prompt-only enforcement; educators favored shorter instructions, transcript hooks, required AI histories, custom harnesses, and assessments that independently verify learning.

### Comment pulse

- Instruction design → One instructor found a terse 30-line policy more reliable than examples and nuance, which may drop from working context.
- Auditability → Required prompt/action histories can expose overreliance — counterpoint: commenters advised deterministic hooks or retained tool transcripts rather than trusting model compliance.
- Enforcement → Repository instructions load automatically for many agents, but critics said a custom harness or independent exams better verify learning.

### LLM perspective

- **View:** Agent instructions can shape default behavior, but integrity requires observable process and assessments that remain valid when prompts fail.
- **Impact:** Students gain scalable Socratic debugging; instructors must review traces, define acceptable help, and grade understanding rather than finished artifacts.
- **Watch next:** Context-retention tests, compliance rates across agents, transcript completeness, false refusals, student outcomes, instructor workload, and adversarial bypass attempts.
