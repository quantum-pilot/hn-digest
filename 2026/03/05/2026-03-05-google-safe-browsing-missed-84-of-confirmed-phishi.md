# Google Safe Browsing missed 84% of confirmed phishing sites

- Score: 264 | [HN](https://news.ycombinator.com/item?id=47262347) | Link: https://www.norn-labs.com/blog/huginn-report-feb-2026

### TL;DR

Norn Labs manually confirmed 254 phishing URLs from public threat feeds in February and found Google Safe Browsing had flagged only 41 at scan time, a reported 83.9% miss rate. Its Muninn extension’s automatic scan caught 238 but falsely flagged six of nine legitimate controls; deep scan caught every phishing page while flagging all nine legitimate pages. Many attacks used reputable hosting, staged redirects, one-time tokens, or broken secondary controls. HN questioned the small, discovery-biased dataset and argued deep scan demonstrates maximal caution, not practical accuracy.

### Comment pulse

- Blocklists react after discovery, making them weakest during short campaigns — counterpoint: aggressive page analysis can wrongly suppress legitimate sites.
- Trusted platforms hosted 149 cases, including 16 on Google services, so domain reputation cannot substitute for page-level behavior.
- One-time tokens, anti-bot gates, and benign repeat visits frustrate scanners; broken buttons and off-domain login forms remain useful human clues.

### LLM perspective

- **View:** The headline measures recall on Huginn-discovered cases, not Safe Browsing’s overall phishing detection rate.
- **Impact:** Users choose between delayed blocklists and behavioral scanners that interrupt more legitimate browsing.
- **Watch next:** Larger prospective samples, time-to-detection curves, representative clean controls, independent labels, and precision-recall comparisons.
