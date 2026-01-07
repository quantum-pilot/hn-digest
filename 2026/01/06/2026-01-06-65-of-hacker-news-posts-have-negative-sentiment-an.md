# 65% of Hacker News posts have negative sentiment, and they outperform

- Score: 449 | [HN](https://news.ycombinator.com/item?id=46512881) | Link: https://philippdubach.com/standalone/hn-sentiment/

### TL;DR
An empirical study of 32k Hacker News posts and 340k comments finds about 65% have “negative” sentiment and these earn ~27% more points than average. Sentiment was measured by six transformer/LLM models; all show a negative skew. “Negative” mostly means critical or skeptical, not abusive. Commenters challenge the labeling (skepticism vs negativity, missing neutral class) and possible sampling bias, but many recognize a familiar pattern: critical, short, and snarky content reliably attracts more engagement than positive or nuanced posts.

---

### Comment pulse
- Sentiment caveats → Classifiers treat skepticism as “negative” and largely miss neutral; HN’s culture of critique gets misread as hostility — counterpoint: author stresses “evaluative, not toxic.”
- Data and model doubts → Reported 35-point average seems high; sampling via archiver may skew toward high-vote posts, prompting calls for clarified methodology and alternative classifiers.
- Why negativity wins → Disagreement invites replies while agreement is a silent upvote; site norms discourage simple praise, and short, snarky comments routinely outperform thoughtful long ones.

---

### LLM perspective
- View: The “negativity premium” likely mixes real effects with measurement artifacts around skepticism and missing neutrality.
- Impact: Platforms risk structurally rewarding critical, clickbaity brevity over careful, informative discussion, shaping community tone.
- Watch next: Release of code/data, 3-class and toxicity-aware models, and cross-site comparisons to separate critique, outrage, and low-value snark.
