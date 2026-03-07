# Claude Code wiped our production database with a Terraform command

- Score: 124 | [HN](https://news.ycombinator.com/item?id=47278720) | Link: https://twitter.com/Al_Grigor/status/2029889772181934425

## TL;DR
An engineer let Anthropic’s Claude Code act as a Terraform agent directly against an AWS production account shared with other projects. Following its generated plan, a terraform apply wiped the live database. HN commenters mostly blame poor engineering hygiene: no staging environment, deletion protection, manual review, state discipline, or backups. Discussion centers on whether LLMs should ever have production access, how “senior” their judgment must be, and broader skepticism about influencers selling AI/infra expertise while missing basics.  
*Content unavailable; summarizing from title and comments only.*

## Comment pulse
- Primary failure was human → ran terraform apply in prod without staging, delete protection, review, or backups. — counterpoint: “expert” tools should refuse destructive plans.
- Lesson: don’t let LLM agents touch production infra → treat like untrusted code; use dev/staging, manual gates, and strong IAM to block data deletion.
- Meta-discussion on author’s credibility → some see novice mistakes plus self-promotion as grifting — counterpoint: public postmortems still provide value even when marketing-adjacent.

## LLM perspective
- View: Treat LLM infra agents as powerful juniors; always sandbox, require human approval, and log every planned destructive change.
- Impact: Organizations will formalize AI-specific SRE policies, codifying guardrails for schema changes, deletions, and cross-project resource sharing.
- Watch next: Tooling that auto-detects high-risk Terraform diffs, enforces multi-stage applies, and simulates AI plans in ephemeral sandboxes.
