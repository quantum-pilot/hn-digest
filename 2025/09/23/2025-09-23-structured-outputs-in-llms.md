# Structured Outputs in LLMs

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45345207) | Link: https://parthsareen.com/blog.html#sampling.md

### TL;DR

The article connects structured output to token sampling. After top-k, temperature, softmax, top-p, and min-p transformations, Ollama converts JSON schemas into grammars and masks tokens that would violate them, guaranteeing syntactic validity at some performance cost. Precomputed finite-state graphs and parallel mask computation can reduce overhead, while thinking models complicate when constraints should begin. Commenters stressed that valid JSON is not necessarily truthful data: forced schemas can skew probability distributions, turn detectable failures into plausible corruption, or encourage invented fields such as URLs.

### Comment pulse

- Grammar masking guarantees form, not meaning → a syntactically valid field can remain hallucinated or semantically wrong.
- Schema design shapes model behavior → simpler staged fields can reduce forced guesses and improve extraction reliability.
- Mask computation can overlap inference → optimized parsers may constrain decoding with negligible marginal latency.

### LLM perspective

- View: Structured output is a decoding contract, not evidence of model understanding.
- Impact: Developers gain reliable parsing but must validate values, optionality, and distribution shifts separately.
- Watch next: Benchmark latency, semantic accuracy, schema ordering, refusal behavior, thinking compatibility, and unconstrained baselines.
