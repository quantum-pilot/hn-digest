# If you're a button, you have one job

- Score: 528 | [HN](https://news.ycombinator.com/item?id=48790689) | Link: https://unsung.aresluna.org/if-youre-a-button-you-have-one-job/

### TL;DR

A rotation button should honor every accepted tap—or clearly reject it. On iPhone, rapid taps are buffered or accelerate the animation, so eight quarter-turn commands complete two full rotations. On a Nothing Phone, taps during animation still trigger sound and haptics but are discarded, forcing users to wait. The author calls this a failure for situational power users doing repetitive work. HN agreed feedback must correspond to execution, but rejected universal buffering: debouncing protects accidental double-taps and users with tremors, so controls need explicit states or system-level repeat settings.

### Comment pulse

- Queueing versus debouncing depends on intent → repeated rotations are meaningful — counterpoint: submissions and tremor-induced presses often should execute once.
- Feedback is a contract → sound, haptics, or color imply acceptance; if execution is blocked, disable the control or signal cancellation.
- Buttons have multiple jobs → labels, state, progress, and action must stay synchronized despite independent UI and backend failures.

### LLM perspective

- **View:** The invariant is not every tap executes; it is that observable acknowledgment accurately predicts what the system will do.
- **Impact:** Predictable controls reduce attention costs for repetitive work and prevent uncertain users from compensating with extra taps.
- **Watch next:** Interaction tests covering burst input, slow animations, failed handlers, motor impairments, cancellation, and platform accessibility preferences.
