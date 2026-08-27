# Why do LLMs freak out over the seahorse emoji?

- Score: 669 | [HN](https://news.ycombinator.com/item?id=45487044) | Link: https://vgel.me/posts/seahorse/

### TL;DR

Popular language models confidently claim a seahorse emoji exists even though Unicode rejected a proposal in 2018. Using a logit lens on Llama 3.3, the author finds middle layers forming a combined “seahorse plus emoji” representation. For real emoji, the output projection maps such a concept to matching tokens; no seahorse token exists, so the nearest horse or aquatic emoji appears instead. Once that wrong token reenters context, models may correct themselves, ignore it, or spiral through repeated alternatives.

### Comment pulse

- The discussion mostly turned the nonexistent emoji into an elaborate collaborative SCP joke.
- The human false-memory phenomenon supports either training-data influence or convergent expectation from neighboring animal emoji.

### LLM perspective

- View: The case illustrates a mismatch between a learned concept and the discrete vocabulary available to express it.
- Impact: Autoregressive feedback can reveal an error, but recovery behavior is inconsistent and sometimes amplifies it.
- Watch next: Test whether rollout training, tool lookup, or vocabulary-aware probes improve self-correction systematically.
