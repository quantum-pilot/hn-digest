# GPT-6 Astra on robot arms

- Score: 232 | [HN](https://news.ycombinator.com/item?id=49582582) | Link: https://openai.robocurve.org/gpt-6-astra/

### TL;DR

In 20 trials per task, GPT-6 Astra placed a block into a bowl 19 times, versus Claude Fable 5.1’s eight, while averaging fewer output tokens, lower estimated cost, and less time. On a precision puzzle insertion, both completed only twice and commonly stalled at the groove. The experiment used identical policies but non-interleaved runs, different rigs for the bowl, hand resets, and unblinded human grading. Commenters praised Astra’s planning yet warned that two tasks with inverse kinematics do not establish general robotic-control superiority.

### Comment pulse

- Critics favored hierarchical systems combining general visual planning with specialized local controllers rather than one model controlling everything.
- Suggested applications included sidewalk cleanup—counterpoint: privacy, vandalism, cost, and purpose-built machines may defeat general robot arms.
- Users praised Astra’s broader computer-use planning, but these anecdotes were not part of the robot benchmark.

### LLM perspective

- View: Astra’s bowl result is striking; its puzzle failure shows manipulation progress remains task-specific.
- Impact: Better high-level planning could lower experimentation costs without replacing fast, specialized, safety-critical control layers.
- Watch next: Interleave blinded trials on identical rigs, expand objects and perturbations, and compare VLA and hierarchical baselines.
