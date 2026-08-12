# Stealing Reasoning Traces from Proprietary LLM APIs

- Score: 624 | [HN](https://news.ycombinator.com/item?id=49257876) | Link: https://stolen-thoughts.com/

### TL;DR

Encrypted chain-of-thought blocks from Anthropic, OpenAI, and Google APIs can be replayed across sessions, users, and sibling models. The two-call attack takes a frontier model's trace, injects it into a weaker model from the same provider, then jailbreaks that model into transcribing hidden reasoning, bypassing the stronger model's safeguards. HN found the exploit strikingly simple and attributed portability partly to mid-conversation model switching, but noted length matching does not prove verbatim recovery and questioned whether the result is theft, a security flaw, or a thin academic contribution.

### Comment pulse

- Binding traces to user, session, and model could close the channel → counterpoint: strict model binding would impair mid-conversation switching.
- Extracted traces suggested benchmark contamination and answer-first reasoning that API summaries can misleadingly present as clean derivations.
- Commenters disputed ownership and the word stealing, arguing users paid for outputs while copyright status remains uncertain.

### LLM perspective

- **View:** Opaque reasoning blocks behave like bearer capabilities and need explicit replay scope, not merely encryption.
- **Impact:** Providers may restrict portability, affecting model switching, debugging, and client-side conversation persistence.
- **Watch next:** Cryptographic binding, provider fixes, cross-account retests, transcription fidelity, and anti-distillation evaluations.
