# How Monero’s proof of work works

- Score: 227 | [HN](https://news.ycombinator.com/item?id=48009020) | Link: https://blog.alcazarsec.com/tech/posts/how-moneros-proof-of-work-works

### TL;DR

Monero’s RandomX proof of work replaces a fixed hash (like Bitcoin’s SHA-256) with “run a random, CPU-like program over lots of memory, then hash the result.” It builds a 2+ GiB dataset keyed to an old block, a cache-like scratchpad per attempt, generates 8 random VM programs, and chains them. This forces miners to behave like general-purpose CPUs, shrinking ASIC advantages and keeping mining accessible, while HN comments debate its real-world ASIC resistance, economics, and Monero’s ecosystem direction.

---

### Comment pulse

- RandomX vs ASICs → RandomX forces random code, heavy RAM, and 8 chained programs so an “ASIC” is basically a many-core CPU—counterpoint: history shows ASIC-resistance tends to erode over time.  

- Economics and purpose of crypto → PoW elegantly mints new coins and secures consensus; discussion branches into inflation/deflation, Bitcoin as money vs store-of-value, and how fiat money is actually created.  

- Monero in practice → Users mine on CPUs (Ryzen, old phones, TV boxes) and even as space heaters; RandomX seen as effective so far, but community worries about Carrot/view-key changes and wants clearer non-technical comms.

---

### LLM perspective

- View: RandomX is a rare PoW that explicitly optimizes for “general-purpose messiness” rather than mathematical elegance, to shape miner hardware economics.  

- Impact: Keeps hashrate on commodity CPUs, limiting miner centralization around a few ASIC vendors and encouraging hobbyist/home participation.  

- Watch next: RandomX v2 rollout, any genuinely superior RandomX ASICs, and whether exchanges/regulators pressure Monero’s privacy features via view-key policy.
