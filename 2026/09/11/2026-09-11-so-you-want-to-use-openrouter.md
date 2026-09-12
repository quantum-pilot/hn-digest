# So you want to use OpenRouter?

- Score: 707 | [HN](https://news.ycombinator.com/item?id=49621546) | Link: https://mmoustafa.com/blog/so-you-want-to-use-openrouter/

### TL;DR

An operator reporting 18 million assistant messages argues that OpenRouter’s uniform API masks major provider differences. Their tests found wide benchmark gaps for identical model labels, broken vision support, ignored reasoning-effort settings, malformed tool calls, empty successful responses, incompatible history requirements, location-dependent rate limits, and unstable pinned routes. Declared quantization did not reliably predict quality. Commenters largely corroborate operational unreliability, especially caching and endpoint claims, while defending OpenRouter’s consolidated billing and interface as useful when providers are explicitly vetted and pinned.

### Comment pulse

- Model names do not guarantee equivalent service → provider middleware, precision, parsing, caching, and rate limits materially alter behavior.
- Pinning reduces randomness but not outages → previously reliable providers can throttle, remove models, or develop regressions.
- The intermediary still offers value → one balance and API simplify experimentation across providers despite required operational safeguards.

### LLM perspective

- View: OpenRouter behaves more like a marketplace than a transparent redundancy layer; production users must qualify each endpoint independently.
- Impact: Operators need provider-aware routing, response validation, retries, telemetry, and fallback policies that increase integration complexity.
- Watch next: Track workload-specific benchmarks, empty completions, cache rates, feature compliance, geographic throttling, and billing on failed responses.
