# Benchmarking OpenTelemetry: Can AI trace your failed login?

- Score: 137 | [HN](https://news.ycombinator.com/item?id=46811588) | Link: https://quesma.com/blog/introducing-otel-bench/

### TL;DR

Quesma’s open-source OTelBench tested 14 models on 23 OpenTelemetry instrumentation tasks across 11 languages, using 966 runs and $522 in tokens. Claude Opus 4.5 led at 29%, GPT-5.2 reached 26%, and Gemini 3 Flash offered a strong cost-speed tradeoff at 19%. Tests checked semantic correctness—including span names, parent-child structure, trace IDs, and context propagation—not merely compilation. Models often merged distinct user journeys. HN commenters question whether vague prompts, current-library access, and tiny services make this a meaningful SRE benchmark.

### Comment pulse

- Benchmark scope disappoints some readers → adding instrumentation differs from diagnosing failures through real traces, metrics, logs, and production tools.
- Simple is contested → experienced operators call tasks basic, while others say multi-service instrumentation requires domain knowledge and precise requirements.
- Limited public training data may explain weakness → production debugging expertise usually comes from years of incident response.

### LLM perspective

- View: The benchmark exposes a semantic integration gap: code can compile while tracing the wrong operational story.
- Impact: Teams still need experienced reviewers before trusting AI-written observability code in production systems.
- Watch next: Add diagnosis tasks, document tool and library access, compare human baselines, and expand each language’s sample.
