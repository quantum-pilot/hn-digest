# Anthropic's ‘watermark’ text adulteration in Claude is a perversion of writing

- Score: 818 | [HN](https://news.ycombinator.com/item?id=49324087) | Link: https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing

### TL;DR

Anthropic plans to globally watermark Claude-generated text over roughly 200 tokens to meet an EU transparency code, using secret-key SynthID-style token selection rather than invisible characters. Longer outputs carry stronger statistical signals; lightly proofread text may or may not remain detectable. Anthropic says testing found no practical quality loss, but the author argues hidden influence on wording corrupts prose, unfairly marks harmless assistance, enables false accusations, and is weakened by paraphrasing. Commenters disputed his technical premise: non-distortionary sampling can preserve the token distribution, though detection raises privacy and governance concerns.

### Comment pulse

- Detection may require submitting confidential text to multiple providers, exposing unpublished research or legal drafts and centralizing adjudication.
- Critics noted LLM output already samples probabilistically—counterpoint: implementations differ, and low distortion is not automatically zero semantic effect.
- Probabilistic scores invite subjective thresholds and false positives; motivated evaders can paraphrase while honest proofreading users remain exposed.

### LLM perspective

- View: Quality effects remain disputed, but secret centralized detection creates an independent verifiability problem.
- Impact: Schools, publishers, and employers could outsource authorship judgments to vendors without transparent evidence or consistent thresholds.
- Watch next: Error rates by length and editing, public verification, private detection, regional scoping, and blinded quality tests.
