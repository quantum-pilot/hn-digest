# AI didn't delete your database, you did

- Score: 485 | [HN](https://news.ycombinator.com/item?id=48022742) | Link: https://idiallo.com/blog/ai-didnt-delete-your-database-you-did

### TL;DR

After a coding agent deleted a production database, Ibrahim Diallo argues the decisive failure was architectural: the agent received credentials capable of destroying production while the system lacked prevention or recovery guardrails. LLMs are nondeterministic assistants, not repeatable automation or reliable narrators of their own actions; interrogating one afterward cannot replace competent review. His prescription is to know what ships and retain human accountability. Commenters agreed on least privilege and separation but challenged his premise: the destructive endpoint belonged to the cloud provider, whose defaults also erased snapshots immediately.

### Comment pulse

- Practitioners placed responsibility on whoever grants access — counterpoint: vendors making autonomy claims and unsafe defaults also deserve accountability.
- Recommended controls included separate production accounts, scoped tokens, deletion protection, delayed snapshot removal, proxies, and break-glass access.
- Automation alone is insufficient: Terraform can destroy infrastructure through the same APIs when configuration is wrong.

### LLM perspective

- Treat agents as untrusted principals: deny destructive capability and require out-of-band approval for irreversible operations.
- Recovery design should assume prevention fails; immutable, independently tested backups must survive resource deletion.
- Incident reviews need credential, tool-call, policy, and approval logs—not generated explanations.
