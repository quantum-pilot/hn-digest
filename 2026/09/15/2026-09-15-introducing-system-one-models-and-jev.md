# Introducing System One Models and Jev

- Score: 1827 | [HN](https://news.ycombinator.com/item?id=49717558) | Link: https://typesafe.ai/blog/introducing-system-one-models-and-jev

### TL;DR

TypeSafe AI presents Jev as a non-generative System One model for fast, typed probabilistic decisions inside software workflows. It claims 70–500ms latency, $0.042 per million input tokens, parallel output, calibrated confidence, and guaranteed schema validity, while acknowledging internal benchmark bias and narrower capabilities than string-generating models. Jev is in early access for classification, routing, scoring, and verification. Commenters found the approach promising but challenged the hallucination wording, comparisons with general-purpose LLMs, cloud dependence, and workflow boilerplate.

### Comment pulse

- Jev is specialized, not generative → readers saw value in semantic branching but rejected comparisons implying equivalence with code-producing models.
- Type safety is not factual accuracy → valid structured values can still be wrong, even when accompanied by confidence estimates.
- Practical demos clarified the pitch → home automation and contracts showed potential, alongside privacy, cloud, and orchestration concerns.

### LLM perspective

- View: Jev’s compelling proposition is cheap semantic control flow, not a replacement for language generation or deterministic logic.
- Impact: High-volume workflows could reserve larger models for ambiguous cases while handling routine decisions at lower latency.
- Watch next: Seek independent calibration tests, workload-neutral benchmarks, local deployment options, and evidence that pricing is sustainable.
