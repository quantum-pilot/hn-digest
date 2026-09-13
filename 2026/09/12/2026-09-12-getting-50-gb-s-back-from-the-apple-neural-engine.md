# Getting 50 GB/S Back from the Apple Neural Engine

- Score: 151 | [HN](https://news.ycombinator.com/item?id=49636479) | Link: https://eiln.github.io/posts/ane-dma.html

### TL;DR

An independent investigation reports that M3 Neural Engine weight transfers at exact 1 MiB multiples collapse from roughly 45–60 GB/s to 17–19 GB/s. The author measured periodic recovery within 256 cache lines and hypothesizes a 14-bit prefetch-ring pointer that mistakes a full revolution for empty, starving speculative requests. Splitting problematic transfers into two 512 KiB chunks reportedly raised Llama 3.2 1B from 10.0 to 24.3 tokens per second and Qwen3-8B from 1.36 to 2.97. HN praised the analysis but questioned the unverified RTL explanation.

### Comment pulse

- Exact power-of-two slowdowns suggest wraparound → repeated 1 MiB notches and 16 KiB recovery windows fit the proposed prefetch-credit model.
- The workaround is compiler-friendly → splitting transfers avoids the pathological size without changing numerical results.
- Hardware scope remains limited → commenters reported M1 and M5 Max unaffected, and emphasized that the shown RTL is hypothetical.

### LLM perspective

- View: Strong measurement isolates a reproducible performance defect even when the internal hardware mechanism remains inferred.
- Impact: ANE model compilers can recover substantial throughput through transfer shaping rather than new kernels or hardware.
- Watch next: Independent M3-family reproduction, Apple confirmation, affected-model inventory, compiler patches, and tests across tensor layouts.
