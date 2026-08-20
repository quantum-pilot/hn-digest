# What happens when an LLM never sees material beyond fifth grade?

- Score: 244 | [HN](https://news.ycombinator.com/item?id=49317760) | Link: https://littlelearner-ll.github.io/

### TL;DR

LittleLearner trains 0.6B, 1.3B, and 5B models from scratch on an 88-billion-token FineWeb-Edu corpus filtered to US K–5 standards, alongside architecture-, token-, and recipe-matched unfiltered controls. Scaling, math-focused post-training, and in-context examples improved curriculum tasks and modestly extended the same trajectory, but did not meaningfully unlock advanced out-of-scope capabilities. The project presents the bounded models as experiments for reinforcement-learning discovery, continual concept acquisition, and child/model comparisons—not products for children. Commenters questioned filtering fidelity, flawed example answers, perfect recall versus child cognition, and models’ weak ability to admit ignorance.

### Comment pulse

- Children’s science books can contain sophisticated terms; curriculum exposure is not equivalent to an eight-year-old’s personality, memory, or reasoning.
- A quantum-entanglement control answer was criticized as inaccurate—counterpoint: it was model output, not a labeled gold reference.
- Discussion wanted bounded models to abstain, exposing metacognition and sycophancy as separate problems from knowledge acquisition.

### LLM perspective

- View: Controlled pretraining clarifies capability claims only if filtering and evaluation boundaries withstand leakage audits.
- Impact: Researchers gain a testbed for distinguishing elicitation from learning and measuring retention or interference.
- Watch next: Filtering details, contamination checks, gold-answer quality, abstention calibration, RL novelty, and child-matched exposure comparisons.
