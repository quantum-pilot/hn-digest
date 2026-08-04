# Temporary Cloudflare accounts for AI agents

- Score: 154 | [HN](https://news.ycombinator.com/item?id=48608394) | Link: https://blog.cloudflare.com/temporary-accounts/

### TL;DR

Cloudflare’s latest Wrangler lets unauthenticated coding agents run `wrangler deploy --temporary`, automatically receiving a disposable account, API token, Worker URL, and human-facing claim link. Agents can repeatedly deploy and verify changes during a 60-minute window; claiming transfers the Worker and bound resources into a permanent account, while unclaimed deployments are deleted. Wrangler’s error output teaches agents the new flag. HN readers welcomed broader developer uses but debated whether frictionless provisioning merely shifts the bottleneck from authentication to cost exposure and abuse control.

### Comment pulse

- The feature exceeds its AI framing → anyone can create free, working 60-minute previews for pull requests and code review without account cleanup.
- Abuse controls remain opaque → Cloudflare mentions proof-of-work, creation throttles, and additional checks, but commenters expect attackers to exploit easier anonymous provisioning.
- Cost anxiety grows with autonomous deployment → users want absolute monthly caps that halt service, fearing agents or attacks could generate large bills.

### LLM perspective

- **View:** Temporary identity is a useful cloud primitive: creation, testing, ownership transfer, and deletion become one bounded lifecycle.
- **Impact:** Background agents gain an autonomous deploy-test loop; platform operators inherit stronger attribution, quota, moderation, and cleanup obligations.
- **Watch next:** Measure abuse rates, claim conversions, deletion reliability, preview limits, and whether permanent accounts receive agent-safe budget controls.
