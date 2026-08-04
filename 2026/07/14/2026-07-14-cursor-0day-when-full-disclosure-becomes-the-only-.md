# Cursor 0day: When Full Disclosure Becomes the Only Protection Left

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48910676) | Link: https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left

### TL;DR

Mindgard disclosed a Windows Cursor flaw in which opening a repository containing a root-level git.exe can make the IDE execute that binary repeatedly, without an in-product prompt, as it searches for Git. The code runs with the current user’s privileges, turning a cloned project into an arbitrary-code-execution vector. Mindgard says it reported the issue in December 2025, HackerOne reproduced it, and Cursor provided no remediation update for seven months. HN debate split over severity: some expect opening code to be passive; others compared it with existing executable and dependency risks.

### Comment pulse

- Repository trust was the fault line → critics said an attacker already placed an executable — counterpoint: cloning for review should not authorize execution.
- Windows behavior explains but does not excuse it → known-directory resolution or a configurable Git path could avoid workspace executable precedence.
- Disclosure channels look overloaded → commenters blamed AI-amplified report volume for burying both low-quality submissions and legitimate findings.

### LLM perspective

- **View:** IDE trust modes are ineffective if basic project inspection performs ambient executable discovery before explicit trust is established.
- **Impact:** Until patched, managed systems can deny workspace execution; consumers should inspect untrusted repositories in disposable environments.
- **Watch next:** Verify a patch removes workspace lookup, adds provenance-aware prompts, and tests Git discovery across trusted and untrusted states.
