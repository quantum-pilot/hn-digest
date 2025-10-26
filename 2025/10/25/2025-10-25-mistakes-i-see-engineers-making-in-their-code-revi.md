# Mistakes I see engineers making in their code reviews

- Score: 75 | [HN](https://news.ycombinator.com/item?id=45701404) | Link: https://www.seangoedecke.com/good-code-reviews/

- TL;DR
    - Code review should emphasize system context and consistency, not just diffs; keep comments few and meaningful; avoid “my way” nitpicks; use explicit statuses—approve by default, block when necessary. Frequent blocking often signals structural gatekeeping. AI-generated PRs deserve stricter gating. HN broadly agrees on minimizing taste-imposition, with caveats: consistency matters in mature codebases, tooling should enforce style to reduce noise, reviewers accountable for production may gatekeep more. Reviewers also caution against PR scope creep; “how would I write it?” can be a private thinking aid.

- Comment pulse
    - Don’t impose personal taste → multiple valid solutions; reserve blocking for objective issues — counterpoint: in mature codebases, consistency becomes a non-negotiable maintainability rule.
    - Automate style checks → linters/formatters block formatting and naming noise, keeping reviews architectural; deviations require justification in PR description.
    - Bias to approve with suggestions → gatekeep only for broken or misaligned changes; separate out-of-scope ideas into issues to avoid PR sprawl.

- LLM perspective
    - View: LLMs amplify code volume; human reviewers must supply system context, consistency enforcement, and judgment; AI PRs merit higher review bars.
    - Impact: Adopt explicit review statuses, cap comment counts, and shift style enforcement to CI; align incentives for platform bottleneck teams.
    - Watch next: Track approval/block rates and merge times; pilot contextual AI reviewers; measure reduced nitpicks after formatter/linter adoption.
