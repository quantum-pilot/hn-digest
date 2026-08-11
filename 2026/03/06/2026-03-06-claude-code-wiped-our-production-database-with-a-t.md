# Claude Code wiped our production database with a Terraform command

- Score: 124 | [HN](https://news.ycombinator.com/item?id=47278720) | Link: https://twitter.com/Al_Grigor/status/2029889772181934425

### TL;DR

An engineer let Claude Code run Terraform in an AWS account shared with production. Missing local state created duplicates; after an old archive replaced the new state, an approved destroy deleted production networking, compute, RDS, and its snapshots. AWS recovered a hidden snapshot 24 hours later, preserving 2.5 years of course data. The author now manually executes reviewed plans, stores state remotely, enables deletion protection, isolates backups, and tests restores daily. HN called these controls baseline practice and debated whether automation or its operator deserved blame.

### Comment pulse

- Claude warned against sharing infrastructure, but the user overrode it — counterpoint: a senior-grade agent should still gate destructive production commands.
- Near-reliable automation encourages misplaced trust, much like hands-off driving before the system can reliably handle rare failures.
- Recovery is not backup until tested; remote state, account isolation, independent copies, deletion protection, and manual approval are separate safeguards.

### LLM perspective

- **View:** Capability was not decisive; excessive permissions collapsed several absent operational controls into one command.
- **Impact:** Course users faced a day-long outage; the operator now pays more for support and redundant recovery infrastructure.
- **Watch next:** Least-privilege agent roles, policy-enforced approvals, immutable backups, routine restore drills, and separate production accounts.
