# Saving another 100TB of RAM

- Score: 199 | [HN](https://news.ycombinator.com/item?id=49758580) | Link: https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/

### TL;DR

Cloudflare says two changes to Pingora's consistent-hashing rings reclaimed more than 100 TB of RAM globally. Packing each hash and server index into six bytes cut per-point storage 25%; an exact variance analysis then showed the highest-weight servers gained almost nothing from their last 90,000 virtual points, enabling a 90% count reduction. Because replacing rings would remap cached requests and hammer origins, Cloudflare temporarily ran both versions and migrated traffic by data center. HN praised the optimization while debating complexity, engineering jobs, and whether shipping speed caused the waste.

### Comment pulse

- Small savings become infrastructure-scale wins → two bytes per point and fewer hashes matter when dozens of weighted rings run across thousands of servers.
- Mathematical validation made deletion safe → diminishing balance improvements and rising 32-bit collisions justified removing points rather than merely compressing them.
- Deep optimization still rewards expertise → readers admired work beyond one-shot coding — counterpoint: models may eventually automate similar measurement and search loops.

### LLM perspective

- View: The largest gain came from challenging a conservative constant with workload-specific mathematics, not from changing the hashing architecture.
- Impact: Cloudflare reduces memory use while preserving weighted routing and gradual rollback through Pingora's dual-ring support.
- Watch next: Observe cache balance after workload shifts and compare the v2 ring's memory, startup time, collisions, and routing variance.
