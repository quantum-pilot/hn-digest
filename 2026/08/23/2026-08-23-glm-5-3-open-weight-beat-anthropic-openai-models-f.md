# GLM-5.3 (open-weight) beat Anthropic/OpenAI models – for 1/5 the cost

- Score: 233 | [HN](https://news.ycombinator.com/item?id=49410097) | Link: https://reinvently.co.uk/tools/ed-o-meter/

### TL;DR

On Featherbench’s 28 single-trial tasks, GLM-5.3 scored 100% with a 9.3/10 rubric, 100% security, 16.3-second median time to first token, and $0.0101 per task. That placed it first in this particular open harness, ahead of models whose scores were reduced by failures or provider-side refusals. The benchmark exposes prompts, answers, settings, and checkers, but its wide confidence interval and many 93–96% results signal saturation. Commenters therefore rejected any broad model-superiority claim, citing trivial tasks, limited trials, judge bias, and contradictory evaluations.

### Comment pulse

- Near-universal passing weakens ranking resolution → Haiku’s 96% result and trivial coding tasks made several readers doubt discrimination.
- Reproducible openness is a strength → counterpoint: a $30 single-trial run remains noisy and too small for sweeping conclusions.
- Refusals are operational failures for users → others argued they measure provider filtering rather than underlying model capability.

### LLM perspective

- View: The result supports GLM-5.3 as a strong candidate on these tasks, not a general victory over closed models.
- Impact: Teams can cheaply rerun the harness, but decisions need workloads matching their difficulty, safety, latency, and iteration patterns.
- Watch next: More trials, harder unsaturated tasks, alternate judges, confidence-aware rankings, direct-provider runs, and independent reproduction.
