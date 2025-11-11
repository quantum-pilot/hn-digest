# LLM policy?

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45871531) | Link: https://github.com/opencontainers/runc/issues/4990

- TL;DR
  - Runc maintainer cyphar proposes an LLM policy: close LLM-written issues as spam, and only accept code when authors can explain it themselves; he also flags DCO risks. Co-maintainers are okay with LLMs for translation, grammar, and trivial boilerplate. Commenters argue to judge by quality rather than origin, but maintainers stress the review burden and deceptive volume of LLM output. HN debates quality-versus-source rules, whether stronger testing beats bans, and how volume shifts maintainers’ time from mentoring to triage.

- Comment pulse
  - Ban LLM submissions to reduce load → maintainers can't trust issue accuracy; mentorship fails for machine output — counterpoint: judge quality or use testing; volume hurts.
  - Platform risk → GitHub's AI features encourage spam; projects may migrate to Codeberg for fewer AI buttons and stricter moderation; Copilot prompts in issue highlight misalignment.
  - Standards-washing politics → PRs mask agendas (e.g., renaming Taiwan via ISO 3166); AI code review caught errors; proposals for bots to detect propaganda patterns.

- LLM perspective
  - View: Ban LLM issues; require author comprehension for code feels enforceable and aligns with maintainer time constraints.
  - Impact: Projects without policies risk triage burnout; inconsistent stances across repos will incentivize spam to migrate.
  - Watch next: Concrete CONTRIBUTING updates, an LLM-use disclosure tag, and CI checks flagging likely AI text before maintainers engage.
