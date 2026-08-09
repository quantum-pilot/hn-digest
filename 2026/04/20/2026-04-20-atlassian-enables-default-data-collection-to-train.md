# Atlassian enables default data collection to train AI

- Score: 477 | [HN](https://news.ycombinator.com/item?id=47833247) | Link: https://letsdatascience.com/news/atlassian-enables-default-data-collection-to-train-ai-f71343d8

### TL;DR

Beginning August 17, Atlassian plans to use metadata and in-app content from Jira, Confluence, and related cloud products to train Rovo and Rovo Dev. Free, Standard, and Premium customers cannot disable metadata contribution; in-app defaults vary by tier, while Enterprise starts with both categories off. Inputs may include issue text, comments, page bodies, workflow names, story points, and SLA values. Atlassian promises de-identification, 30-day content removal, 90-day model retraining after opt-out, and exclusions for government, isolated, HIPAA, and customer-key deployments. Metadata may remain for seven years.

### Comment pulse

- Customers objected that sensitive tickets, specifications, and internal discussions are being opted into training, with controls initially absent from admin consoles.
- Atlassian says settings will roll out by May 19, giving administrators time before enforcement.
- Some called this industry-standard SaaS behavior — counterpoint: broad content scope plus tier-gated opt-outs makes governance a paid feature.

### LLM perspective

- De-identification does not eliminate inference risks from project structure, deadlines, or operational metrics.
- Procurement teams must distinguish data residency from permission to use content for model development.
- Watch whether deletion-triggered retraining is independently auditable and extends through downstream model providers.
