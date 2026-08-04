# In praise of memcached

- Score: 252 | [HN](https://news.ycombinator.com/item?id=48638886) | Link: https://jchri.st/blog/in-praise-of-memcached/

### TL;DR

The author prefers Memcached when an application needs a cache because its constraints preserve that boundary: no disk persistence, client-side key distribution, cheap stateless instances, and clients that turn outages into cache misses. Redis can do caching well, but its richer data structures and persistence invite teams to treat a supposedly disposable service as an unmonitored database. HN largely endorsed choosing purpose-built, boring infrastructure and highlighted Memcached’s O(1) operations, while warning that any cache can create dependency, stampedes, hot keys, and operational complexity if applications lack resilient fallback paths.

### Comment pulse

- Use separate roles for separate guarantees → volatile caches need eviction; durable Redis workloads need persistence, replication, capacity planning, and stronger monitoring.
- Memcached’s simplicity improves tail behavior → every operation is O(1), avoiding arbitrary-complexity commands that can stall Redis’s single-threaded core.
- Constraints cannot prevent cache addiction → fail-open clients still expose databases to stampedes, hot-key amplification, and overload — counterpoint: disciplined fallbacks mitigate these failures.

### LLM perspective

- **View:** The best cache design treats complete loss as routine, making optionality an application invariant rather than a service promise.
- **Impact:** Platform teams gain simpler replacement and scaling; developers lose convenient structures that may conceal new persistence requirements.
- **Watch next:** Test cold-cache recovery, stampede controls, node churn, key skew, eviction behavior, and database headroom before selecting either system.
