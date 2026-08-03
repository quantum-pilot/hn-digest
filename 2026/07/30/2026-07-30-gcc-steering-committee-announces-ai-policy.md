# GCC steering committee announces AI policy

- Score: 231 | [HN](https://news.ycombinator.com/item?id=49108685) | Link: https://lwn.net/Articles/1086041/

### TL;DR

GCC will reject legally significant contributions containing or derived from LLM output, using the GNU guideline of roughly 15 lines of code or text as the copyright threshold. Maintainers may accept generated test cases, and models remain allowed for research, analysis, bug discovery, reporting, or review when their output is absent from submissions. The committee plans periodic review. HN commenters welcomed a clear defense against unattended, low-quality agent PRs, but critics said the blanket rule excludes careful AI-assisted work; others stressed copyright and licensing uncertainty.

### Comment pulse

- Maintainers report autonomous contribution spam → agents open redundant or oversized patches and answer reviews without human oversight, transferring long-term maintenance costs.
- Thoughtful contributors object to categorical exclusion → disclosure, small diffs, and accountable human review do not make otherwise acceptable AI-assisted patches eligible.
- Copyright interpretations diverge → some see GPL compatibility risk in non-copyrightable or sourced output — counterpoint: users may hold rights in tool-assisted results.

### LLM perspective

- View: The policy prioritizes provenance certainty and maintainer capacity over case-by-case quality judgments, making enforcement simple but intentionally overinclusive.
- Impact: Contributors must keep model-generated expression out of patches, while maintainers gain a uniform basis for declining agent submissions.
- Watch next: Track clarifications on derivation, test-case exceptions, disclosure expectations, and evidence that spam declines without losing valuable contributors.
