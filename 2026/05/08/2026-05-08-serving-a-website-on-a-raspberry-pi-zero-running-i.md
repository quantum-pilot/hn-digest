# Serving a website on a Raspberry Pi Zero running in RAM

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48064312) | Link: https://btxx.org/posts/memory/

### TL;DR

A Raspberry Pi Zero v1.3 with 512 MB RAM serves a static site from Alpine Linux’s diskless mode, using only about 40 MB for the OS. A microSD card boots the machine and persists selected configuration through `lbu`; `darkhttpd`, Dropbear, and rsync handle serving and maintenance. A 128 MB, roughly $4/year VPS forwards traffic and its HAProxy terminates TLS. HN admired the resilient low-power appliance but questioned the premise: once a VPS performs the expensive public-facing work, it could host the tiny site itself.

### Comment pulse

- Offloaded TLS weakens the stunt → counterpoint: reverse-proxy termination is normal, and the project explicitly prioritizes experimentation over minimal architecture.
- Pi Zero exceeds 1990s servers and many personal-service needs → static HTTP barely tests its capacity.
- RAM-root Alpine reduces SD writes and survives power loss → small Linux appliances can run for years with easy image backups.

### LLM perspective

- **View:** The interesting lesson is diskless operational design, not compute scarcity.
- **Impact:** Hobbyists gain durable, inspectable self-hosting while accepting an external-ingress dependency.
- **Watch next:** Direct TLS benchmarks, proxy caching, VPN origin protection, card longevity, and restoration drills.
