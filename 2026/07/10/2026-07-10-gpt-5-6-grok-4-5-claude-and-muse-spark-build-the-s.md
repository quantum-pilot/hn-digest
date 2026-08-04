# GPT-5.6, Grok 4.5, Claude, and Muse Spark build the same 4 apps

- Score: 127 | [HN](https://news.ycombinator.com/item?id=48865093) | Link: https://www.tryai.dev/blog/gpt-5.6-build-off-12-models

### TL;DR

A TryAI build-off gave 12 models five one-shot attempts at a raycaster, animated Rubik’s cube, calculator, and Game of Life, publishing artifacts, success counts, costs, and latency while disclaiming scientific objectivity. GPT-5.6 Sol led the raycaster; Claude Fable 5 swept clean cube solves and produced favored styling; Grok 4.5 offered strong consistency per dollar; Muse Spark was capable but erratic. Cheap open-weight models matched simpler, familiar tasks but struggled more on complex builds. HN questioned whether greenfield demos reflect real software work, reasoning rather than memorized patterns, or benchmark-resistant ability.

### Comment pulse

- One-shot greenfield generation is a narrow proxy → practicing engineers care more about iterative work inside large, messy, existing codebases.
- Visual success may measure retrieval more than reasoning → common raycaster, cube, calculator, and Life patterns likely appear extensively in training data.
- Subjective scoring still adds evidence → five attempts and published artifacts expose variance — counterpoint: task choice and human judgments remain easy to optimize around.

### LLM perspective

- **View:** The study is useful artifact exploration, not a coding leaderboard; its strongest signal is model variance across repeated runs.
- **Impact:** Model selection should match task complexity, acceptable failure rate, latency, and cost instead of defaulting to the newest flagship.
- **Watch next:** Test repository-scale maintenance, debugging, tests, review cycles, hidden requirements, and contamination-resistant tasks with blinded, reproducible scoring.
