# Agent Skill to Force Docs in ASD-STE100 Simplified Technical English

- Score: 152 | [HN](https://news.ycombinator.com/item?id=49114639) | Link: https://github.com/AminBlg/SimpleEnglish

### TL;DR

This MIT-licensed agent skill applies 53 paraphrased ASD-STE100 rules to technical documentation, error messages, runbooks, incident reports, release notes, and prompts. It favors short active sentences, consistent terminology, explicit conditions, and one instruction per sentence, while excluding marketing. Across 96 generations from six Claude models and eight tasks, the author reports 72.9% fewer violations per 100 words, shorter sentences, and fewer tokens. Commenters question whether a large skill beats simply requesting ASD-STE100, while others argue increasingly capable coding models still produce prose that needs enforceable constraints.

### Comment pulse

- Packaging is disputed → a direct rewrite request produced acceptable output — counterpoint: others want enforceable help as model explanations grow less comprehensible.
- Style tooling is broader than STE → one commenter built an Economist guide skill, while another flagged STE’s misapplication and limited adoption.

### LLM perspective

- View: A reusable skill is most defensible when it encodes auditable rules, not merely a named style.
- Impact: Documentation teams gain consistent constraints across multiple harnesses; casual users may prefer a short prompt.
- Watch next: Compare the full skill against minimal prompts on unseen models, domains, and human comprehension.
