# Training our own AI models

- Score: 190 | [HN](https://news.ycombinator.com/item?id=48296359) | Link: https://posthog.com/blog/training-ai-models

### TL;DR

PostHog plans to train proprietary models on customer data to scale session-replay analysis, simulate user testing, predict behavior, and power proactive product features. Beginning June 29, US-cloud organizations are included by default unless contracts prohibit training; EU-cloud users default out. PostHog promises anonymization, in-house training, no third-party sharing, advance notices, and an admin opt-out, but withholds model-dependent features from nonparticipants. HN reaction was sharply negative: readers questioned consent, GDPR compliance, and anonymization, and discussed removing or self-hosting analytics despite PostHog’s unusually explicit disclosure.

### Comment pulse

- Default inclusion broke trust → readers called the opt-in wording contradictory and inferred explicit consent would yield insufficient training data.
- Legal scope remains unclear → commenters asked whether anonymization meets GDPR’s high bar and whether EU end users inside US-cloud datasets receive required notice.
- Transparency earned a limited defense → one reader preferred informed opt-out and in-house training — counterpoint: others said notification cannot replace affirmative permission.

### LLM perspective

- **View:** The error is coupling model quality to default data capture; participation needs a visible exchange of value and control.
- **Impact:** Analytics vendors must treat training rights as a product decision affecting retention, procurement, legal review, and downstream user obligations.
- **Watch next:** Opt-out rates, customer churn, documented anonymization standards, jurisdiction-specific notices, and measurable gains from the resulting models.
