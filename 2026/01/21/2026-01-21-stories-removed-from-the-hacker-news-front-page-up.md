# Stories removed from the Hacker News Front Page, updated in real time (2024)

- Score: 232 | [HN](https://news.ycombinator.com/item?id=46704555) | Link: https://github.com/vitoplantamura/HackerNewsRemovals

### TL;DR

This project polls HN’s top 90 stories each minute and records items that disappear from the previous top 30, excluding second-chance-pool entries and removing records when stories reappear. It aims to expose front-page moderation, but its central inference—that a story cannot naturally fall beyond rank 90 in one minute—is imperfect, and duplicates are a known confounder. HN discussion strongly defended the moderators’ results while disputing whether opaque flagging suppresses legitimate political or AI topics and whether automated safeguards adequately handle hot threads.

### Comment pulse

- Moderation support → readers credit Dang’s team with preserving signal against promotions, duplicates, politics, and repetitive AI discourse.
- Transparency concern → few flags can remove stories without reasons — counterpoint: users can hide unwanted posts and moderation operates at difficult scale.
- Measurement weakness → disappearance is a proxy, so duplicates, ranking movement, second chances, and flamewar controls complicate any censorship interpretation.

### LLM perspective

- View: The dataset is useful observational evidence, but it cannot identify moderator intent or distinguish every removal mechanism.
- Impact: Better provenance could reduce suspicion while helping moderators diagnose duplicate, flagging, and ranking edge cases.
- Watch next: Add reason codes, confidence levels, duplicate detection, reappearance histories, and validation against known moderation events.
