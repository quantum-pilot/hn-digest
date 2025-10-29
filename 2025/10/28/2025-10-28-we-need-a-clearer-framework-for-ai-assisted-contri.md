# We need a clearer framework for AI-assisted contributions to open source

- Score: 231 | [HN](https://news.ycombinator.com/item?id=45731321) | Link: https://samsaffron.com/archive/2025/10/27/your-vibe-coded-slop-pr-is-not-welcome

- TL;DR
  - Sam Saffron (Discourse) argues AI makes code generation cheap but shifts costs to maintainers forced to review unfinished “vibe‑coded” PRs. He proposes a binary framework: share AI prototypes as branches or videos for idea exploration, but only open “ready‑for‑review” PRs you personally vouch for, with tests and guideline compliance. Maintainers should timebox triage and close prototype PRs, redirecting discussion to issues. HN highlights rising asymmetric slop, calls for norms/tooling, and sees LLMs strong at debugging/pattern completion yet weak at choosing designs.

- Comment pulse
  - Projects need norms and reputation gating → AI slop creates asymmetric review costs; PR gating by history may cut drive‑bys — counterpoint: risks excluding newcomers.
  - LLM value is real but limited → great for debugging/context and “rubber ducking”; weak for designing features; some see progress with LSP‑aware agents.
  - AI excels at pattern completion, not intent → can produce perfect helpers/tests once direction is set; but choosing formats/constraints still requires human judgment.

- LLM perspective
  - View: Adopt a two-lane workflow: Prototype branches for exploration; Ready-for-review PRs require author attestation, tests, and adherence to guidelines.
  - Impact: Maintainers regain scarce review bandwidth; contributors get clearer expectations; platforms can add gates: PR attestation, size thresholds, prototype labels.
  - Watch next: Tooling to detect vibe-coded PRs; GitHub-level prototype branch sharing with videos; security benchmarks on AI-generated code in CI.
