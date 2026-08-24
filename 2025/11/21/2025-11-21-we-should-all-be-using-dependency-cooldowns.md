# We should all be using dependency cooldowns

- Score: 257 | [HN](https://news.ycombinator.com/item?id=46005111) | Link: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns

### TL;DR

Most mass supply-chain compromises become visible only when malicious releases reach registries, after which detection and removal often take hours or days. The author proposes delaying published dependency versions by seven to fourteen days, using package-manager controls or update bots, so defenders can flag poisoned releases before projects ingest them. Eight of ten cited incidents had exploitation windows under one week; fourteen days would have blocked all but the unusually patient xz campaign. Cooldowns remain a default risk tradeoff, not protection against stealthy attacks or urgent disclosed vulnerabilities.

### Comment pulse

- Waiting reduces exposure to poisoned releases → most cited campaigns were discovered quickly — counterpoint: urgent security fixes may require immediate adoption.
- Dependency count is an imperfect risk metric → maintainer trust relationships matter more than package quantity alone.

### LLM perspective

- View: Release age is a cheap security signal, not proof of safety.
- Impact: Sensible defaults could prevent many opportunistic compromises without buying another security product.
- Watch next: Native package-manager support, advisory bypasses, transitive enforcement, ecosystem adoption, and attacker adaptation.
