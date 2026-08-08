# How Monero’s proof of work works

- Score: 227 | [HN](https://news.ycombinator.com/item?id=48009020) | Link: https://blog.alcazarsec.com/tech/posts/how-moneros-proof-of-work-works

### TL;DR

Monero’s RandomX replaces a fixed hash loop with randomly generated, CPU-like programs. An older block hash builds a 256 MiB Argon2d cache and roughly 2 GiB dataset; each nonce seeds a 2 MiB scratchpad and VM that runs eight chained programs mixing integer, floating-point, branch, cache, and DRAM work before Blake2b produces the candidate hash. This makes custom hardware resemble a general-purpose CPU, reducing ASIC advantage while retaining a lighter verification mode. Commenters found the design compelling but asked for evidence that mining is actually decentralized and hardware-neutral.

### Comment pulse

- Monero contributors said the closest commercial “ASIC” is many RISC-V CPUs — counterpoint: resistance history suggests economic advantage needs continuous measurement.
- Miners reported viable Ryzen, Apple, smartphone, and old-Xeon participation, though profitability and efficiency differ sharply.
- Newcomers used the design to revisit proof-of-work’s dual role: transaction consensus plus decentralized currency issuance.

### LLM perspective

- Publish hashrate concentration by pool, geography, hardware class, and manufacturer; algorithm design alone cannot prove decentralization.
- Benchmark ASIC-equivalent hardware against commodity CPUs on hashes per watt, capital cost, and availability.
- Watch RandomX V2’s verification savings and whether changes preserve existing miner diversity.
