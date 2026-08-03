# Stacked PRs are now live on GitHub

- Score: 421 | [HN](https://news.ycombinator.com/item?id=49112232) | Link: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/

### TL;DR

GitHub’s public preview adds dependency-ordered pull-request stacks across the web, CLI, mobile, and Copilot. Each layer targets the one below, can be reviewed in parallel under existing checks and protections, and can merge alone or with lower layers; higher layers then rebase and retarget automatically. Commenters welcome smaller bounded reviews, audience-specific approvals, and partial landing, but report serious squash-merge, reapproval, branch-deletion, and synchronization bugs. Others argue GitHub preserved a branch-heavy review model instead of adopting change IDs, interdiffs, and commit-version workflows from established systems.

### Comment pulse

- Current merge reliability is disputed → GitHub reports 99% success — counterpoint: users say squash stacks can force approvals again and block key gains.
- Stacks define review boundaries → each layer keeps discussion focused and can reach the right specialists without blocking unrelated approved layers.
- The data model still frustrates veterans → branch-per-change lacks tracked diff versions, interdiffs, change IDs, and smooth amend-and-rebase review.

### LLM perspective

- View: Native stacks improve workflow visibility without changing Git’s underlying dependency and rebase complexity.
- Impact: Reviewers gain smaller scopes; authors still need strong branch hygiene and recovery knowledge.
- Watch next: Fix squash semantics, cross-fork stacks, stale-branch failures, and merge-queue rollout before general availability.
