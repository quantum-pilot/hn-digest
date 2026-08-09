# SSH has no Host header

- Score: 151 | [HN](https://news.ycombinator.com/item?id=47421828) | Link: https://blog.exe.dev/ssh-host-header

### TL;DR

exe.dev gives each VM one hostname for web and SSH access while sharing scarce public IPv4 addresses. HTTP proxies can route by Host or TLS SNI, but SSH sends no destination hostname. Its solution allocates each owner’s VMs distinct addresses from a shared pool; the destination IP identifies one VM within that owner, while the presented public key identifies the owner. The `{user, IP}` tuple therefore selects the backend without client configuration. HN debated IPv6, jump hosts, ports, and SRV records, but each alternative weakens the same-hostname, zero-setup goal.

### Comment pulse

- IPv6 would remove address scarcity, but exe.dev’s author argued unreliable client reachability still blocks a universal product.
- ProxyJump, custom ports, and SRV records can encode routing — counterpoint: each sacrifices default clients or the single-hostname experience.
- Commenters questioned public-key identity and key reuse, making future authentication changes the tuple design’s main constraint.

### LLM perspective

- **View:** The design turns address scarcity into a composite namespace using information SSH already exposes.
- **Impact:** Users keep ordinary commands; operators inherit careful address allocation and destination-aware proxying.
- **Watch next:** IPv6 adoption, multiple-key semantics, NAT deployment details, and pool-exhaustion behavior.
