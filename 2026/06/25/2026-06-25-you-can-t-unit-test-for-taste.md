# You can't unit test for taste

- Score: 238 | [HN](https://news.ycombinator.com/item?id=48657049) | Link: https://dev.karltryggvason.com/you-cant-unit-test-for-taste/

- TL;DR  
  The discussion argues that “taste” in software and product design—things like subtle code quality, UX friction, or legal risk appetite—can’t be fully captured in specs or unit tests. You can externalize parts of it via docs, design records, or tooling, but debugging and encoding human judgment quickly exceeds what can be formalized. LLMs and agents are powerful support tools and “vibe-coders,” yet still need human gates for evaluation, UX, and risk, plus raise IP concerns when skills are fully codified.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  Taste resists full formalization → specs and tests can cover correctness, but nuance still needs human review or explicit validation gates—counterpoint: partial externalization via comments/AST metrics still helps.  
  LLMs work best as supervised assistants → “vibe-coding” with plan/revise cycles and human steering yields good results, but models remain poor at UX and beta-testing judgment.  
  Externalizing taste has ownership risks → once encoded as agent skills, employers may claim IP; side threads critique LLMs’ “tasteless” legal strategies and some geospatial tech choices.

- LLM perspective  
  View: Treat “taste” as a human-in-the-loop signal, not a unit-testable property; build workflows that assume irreducible tacit judgment.  
  Impact: Dev, UX, and legal work shift toward guiding and auditing agents, with personal “taste” becoming a differentiating skill.  
  Watch next: Preference-learning models, automated UX probes, and agent frameworks with first-class human approval stages and transparent IP boundaries.
