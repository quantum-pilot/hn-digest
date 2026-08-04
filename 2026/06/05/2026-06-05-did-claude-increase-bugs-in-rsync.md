# Did Claude increase bugs in rsync?

- Score: 270 | [HN](https://news.ycombinator.com/item?id=48411635) | Link: https://alexispurslane.github.io/rsync-analysis/

### TL;DR

An analysis of 36 rsync releases compares severity-weighted bugs per 10 commits using GitHub, Bugzilla, and mailing-list reports. Only two releases contain attributed Claude commits: v3.4.2 scored 0 and v3.4.3 scored 3.29, averaging below the historical 2.95; permutation and Fisher tests returned p=.46 and p=.74, so they are not statistically unusual. The author concludes current data show no Claude-linked increase, not that future use is harmless. HN challenged the tiny sample, release attribution, discovery-time bias, and LLM-assigned severity, while highlighting a reverted Claude-tagged allocation regression and security-report-driven change surge.

### Comment pulse

- Two observations cannot establish safety → tests correctly find no anomaly, but power is too weak to rule out meaningful harm.
- Release mapping may distort causality → bugs can attach to a short-lived patch tag, and recent releases have had less discovery time.
- Regression volume has a confound → AI-generated security reports forced rapid fixes — counterpoint: Claude-assisted allocation code still produced a measurable RSS problem.

### LLM perspective

- **View:** The analysis rebuts certainty, not concern; absence of signal from n=2 is weak evidence in either direction.
- **Impact:** Maintainers need review and release controls that scale with AI-amplified report and commit volume.
- **Watch next:** Pre-register severity scoring; model discovery lag; audit unattributed assistance; compare changed lines, reviews, regressions, and fixes per release.
