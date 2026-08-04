# LongCat-2.0, a large-scale MoE model with 1.6T total and 48B Active

- Score: 268 | [HN](https://news.ycombinator.com/item?id=48727116) | Link: https://longcat.chat/blog/longcat-2.0/

### TL;DR

LongCat-2.0 is an open-sourced mixture-of-experts model with 1.6 trillion total parameters but about 48 billion active per token, pretrained on over 35 trillion tokens using more than 50,000 alternative AI ASICs. Its 1-million-token training, sparse-attention indexer, 135-billion-parameter n-gram embeddings, and specialist post-training target coding and long-horizon agents; mostly in-house benchmarks place it near proprietary leaders on selected tasks. HN viewed the alternative-hardware training stack as the main achievement, but questioned unaudited claims, benchmark comparability, possible architectural reuse, factual reliability, and political refusals.

### Comment pulse

- Hardware independence is the headline → commenters speculated the 50,000 accelerators were Huawei Ascend 910C chips, but the article neither identifies nor independently audits them.
- Anecdotes exposed evaluation gaps → one niche reactor answer was wrong — counterpoint: commenters challenged the prompt, missing context, and single-run methodology.
- Open availability does not ensure openness → commenters reported refusal on politically sensitive history and awaited released artifacts before trusting architecture and training claims.

### LLM perspective

- **View:** System engineering at 50,000-accelerator scale may be more strategically significant than incremental benchmark placement.
- **Impact:** A credible non-Nvidia training path could diversify frontier infrastructure, tooling, suppliers, and deployment economics.
- **Watch next:** Verify checkpoint architecture, serving requirements, token throughput, memory footprint, and agent success under independent harnesses.
