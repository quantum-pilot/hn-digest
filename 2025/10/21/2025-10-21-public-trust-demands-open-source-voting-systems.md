# Public trust demands open-source voting systems

- Score: 186 | [HN](https://news.ycombinator.com/item?id=45657431) | Link: https://www.voting.works/news/public-trust-demands-open-source-voting-systems

- TL;DR
  - VotingWorks argues Dominion’s sale to Liberty Vote underscores a trust crisis solvable by transparency: U.S. voting systems should be fully open-source. They cite Signal and DoD guidance, and claim to be the only U.S. open-source vendor. HN debates eliminating software entirely in favor of hand-counted paper, criticizes sprawling dependency lockfiles, and adds missing context: VotingWorks’ offline ballot-marking prints paper ballots for audits. Tradeoffs raised: accessibility and multilingual ballots, speed vs integrity, minimal complexity, and strong voter-roll hygiene.

- Comment pulse
  - Paper-only elections → simple, observable, recountable; examples: Ireland, Netherlands. — counterpoint: ADA/multilingual needs and complex ballots favor BMDs; paper audits reduce machine risk.
  - Massive dependency lockfiles → opaque supply-chain risk; trust demands minimal, verifiable code and reproducible builds.
  - Hybrid open-source + paper audits → offline ballot-marking prints verifiable ballots; risk-limiting audits validate tabulation; still debate speed vs integrity.

- LLM perspective
  - View: Open-source plus voter-verified paper and RLAs is pragmatic; ban network connections; minimize dependencies; publish SBOMs and reproducible builds.
  - Impact: State procurement and certification (EAC/VVSG), vendors like Liberty Vote, and accessibility advocates would need to adapt processes, tooling, and timelines.
  - Watch next: Liberty Vote’s stance on source release; states piloting RLAs; independent build verification and hash-signing of deployed binaries.
