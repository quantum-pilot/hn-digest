# Study: Self-generated Agent Skills are useless

- Score: 161 | [HN](https://news.ycombinator.com/item?id=47040430) | Link: https://arxiv.org/abs/2602.12670

### TL;DR
SkillsBench introduces a benchmark for “agent skills”—small procedural docs tools call during tasks—across 86 tasks in 11 domains. Human‑curated skills substantially improve success, especially in weaker domains, and short, focused skills beat long documentation; with them, smaller models can rival larger ones. But “self-generated” skills, created in a single pre-task prompt, slightly hurt performance. HN commenters argue this setup ignores iterative, experience-based, human–AI co-created skills over real codebases, so the headline underplays where self-generated skills actually help.

### Comment pulse
- Paper’s self-generated condition is overly constrained → toy tasks, no codebases or web/tools, no new experience to distill; agent just rephrases its own prior context — counterpoint: still useful to know pre-prompt “plan harder” doesn’t help.  
- Practitioners say good skills act as external, non-parametric memory → capture project-specific facts, state, and preferences; avoid stuffing in generic how-tos models already know.  
- Big missing condition: human–AI collaborative skills → commenters report strong gains from eval-driven coding/skill loops and want benchmarks including iteratively refined, co-created skills.

### LLM perspective
- View: Skills should be interfaces to external state, tools, and org knowledge, not restatements of the model’s internal know-how.  
- Impact: Teams deploying agents need pipelines that turn real task runs into candidate skills, plus automated evals gating what’s kept.  
- Watch next: Benchmarks covering multi-step projects, evolving codebases, web tools, and human edits to skills will reveal true compound benefits.
