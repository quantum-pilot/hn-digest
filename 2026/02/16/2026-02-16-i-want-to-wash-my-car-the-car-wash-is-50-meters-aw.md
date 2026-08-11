# I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

- Score: 1379 | [HN](https://news.ycombinator.com/item?id=47031580) | Link: https://mastodon.world/@knowmadd/116072773118828295

### TL;DR

Six prominent assistants initially told a user to walk 50 meters to a car wash, overlooking that the car itself had to arrive; several then rationalized the mistake. Some reasoning-model runs answered correctly, and adding the car’s starting location improved results, but commenters argued humans should not need to spell out such obvious implications. Others noted cherry-picking and human susceptibility to linguistic traps. The example exposes unstable, confidently stated pattern completion and raises the harder evaluation question: whether viral failures are repaired generally or merely memorized.

### Comment pulse

- Strong training associations between short distance and walking may override purpose → extra context shifts the answer without repairing underlying comprehension.
- Better prompting can recover logic → counterpoint: ordinary users routinely ask incomplete questions and still expect robust interpretation.
- Viral examples are quickly patched → novel variants are needed to distinguish general reasoning from benchmark replay.

### LLM perspective

- **View:** One toy failure matters because complex analogues are harder to notice.
- **Impact:** Users need calibrated uncertainty and assumption checks before acting on ambiguous answers.
- **Watch next:** Test paraphrases, changed vehicles and distances, fresh puzzles, and repeated trials across models.
