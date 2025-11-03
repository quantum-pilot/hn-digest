# At the end you use Git bisect

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45791882) | Link: https://kevin3010.github.io/git/2025/11/02/At-the-end-you-use-git-bisect.html

- TL;DR
    - Author argues interviews at least require binary search; in practice, git bisect applies it to locate a breaking commit in a busy monorepo. By marking a good and bad revision and automating tests with git bisect run, they identified a config change causing failures and reverted it. HN discussion splits: some say good architecture and observability make bisect rare; many cite it as indispensable for kernels, opaque code, and audits. The post includes a minimal pytest demo showcasing automated bisect-driven testing.

- Comment pulse
    - Bisect shines in messy or opaque systems → narrows culprit commit without full code comprehension; enables kernel/user debugging — counterpoint: in well-structured code, tests/observability suffice.
    - Beyond fixing, find why/when → commit messages, history reveal intent and duration; supports audits and “bug vs feature” calls.
    - Alternatives and tips → git log -L/-S for function or string history; keep commits small; automate with git bisect run.

- LLM perspective
    - View: Use bisect operationally; script deterministic repro, prebuild artifacts, and use git bisect skip for flaky or uncompilable commits.
    - Impact: CI pipelines that auto-bisect nightly regressions can cut triage time and assign ownership via CODEOWNERS.
    - Watch next: Monorepo-scale optimizations: shared build caches, hermetic test environments, cross-service bisect strategies when backend/data changes interact with frontend.
