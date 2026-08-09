# What if AI doesn't need more RAM but better math?

- Score: 162 | [HN](https://news.ycombinator.com/item?id=47561297) | Link: https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more

### TL;DR

TurboQuant compresses transformer KV caches by combining PolarQuant, which maps high-dimensional vectors into a quantization-friendly polar representation, with QJL, a sign-bit random projection intended to correct inner-product error. The cited paper reports 3.5 bits per channel with no measured quality loss on selected Gemma, Mistral, and Llama benchmarks, roughly 6× less KV memory, and up to 8× H100 speedup versus 32-bit keys. The author extrapolates to cheaper long contexts, higher concurrency, local inference, and vector search, but production adoption, generalized accuracy, and any causal link to memory stocks remain unproven.

### Comment pulse

- RaBitQ’s authors allege TurboQuant misstates their work and compares theory misleadingly despite pre-submission notice; the provided OpenReview link required correction.
- Commenters expect freed memory to fund bigger models and workloads — counterpoint: lower per-gigabyte willingness to pay could still squeeze vendor margins.
- Because the paper predated the RAM rally by nearly a year, readers doubted Google’s blog alone caused the stock selloff.

### LLM perspective

- **View:** This is a strong research result whose market narrative outruns demonstrated deployment and independent reproduction.
- **Impact:** Compression may shift scarce memory toward longer contexts and concurrency, producing rebound demand instead of absolute savings.
- **Watch next:** Production kernels, workload-level latency, quality across architectures, RaBitQ rebuttal resolution, and HBM pricing power.
