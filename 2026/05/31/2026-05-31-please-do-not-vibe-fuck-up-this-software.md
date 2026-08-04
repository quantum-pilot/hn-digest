# Please Do Not Vibe Fuck Up This Software

- Score: 452 | [HN](https://news.ycombinator.com/item?id=48342705) | Link: https://github.com/RsyncProject/rsync/issues/929

### TL;DR

A closed rsync GitHub issue used a hostile title and screenshot, rather than a reproducible bug report, to protest Claude-assisted changes after recent regressions. Thread participants cited a high-CPU backup failure and a `--compare-dest` regression traced by commenters to a Claude Code commit; defenders noted the change addressed security work, older releases contain CVEs, and human patches also regress. HN broadly shared concern for rsync’s stability but split over blame: critics want conservative maintenance and stronger review, while others defended maintainer autonomy and condemned drive-by abuse.

### Comment pulse

- Critical infrastructure needs a higher release bar → downstream backup and government users inherit outage, audit, and provenance costs from regressions.
- AI attribution is not causal proof → maintainers fixed security flaws and humans also introduce bugs — counterpoint: generation speed can outpace review.
- The complaint’s form undermined its substance → an insulting, context-free issue invited brigading where a bisected test case would have enabled repair.

### LLM perspective

- **View:** Mature software can still require aggressive security work; stability depends on slowing promotion, not freezing development.
- **Impact:** Maintainers need protection from abuse; dependents need predictable risk signals before promoting critical updates.
- **Watch next:** Regression tests for `--compare-dest`, release-candidate soak time, downstream compatibility matrices, AI attribution policy, and issue-template enforcement.
