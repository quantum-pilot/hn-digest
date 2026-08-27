# Using FreeBSD to make self-hosting fun again

- Score: 189 | [HN](https://news.ycombinator.com/item?id=45789424) | Link: https://jsteuernagel.de/posts/using-freebsd-to-make-self-hosting-fun-again/

### TL;DR

After self-hosting became joyless, the author moved a new server to FreeBSD, using BastilleBSD for jails and vm-bhyve for virtual machines. Starting without a settled design restored the pleasure of learning. They praise BSD's coherent simplicity, man pages, long compatibility, and helpful community, while admitting confusion around base-system releases versus packages and ports. Commenters echoed the appeal of jails, ZFS, pf, and straightforward configuration, but noted hardware gaps such as incomplete big.LITTLE scheduler support and often retained Linux for KVM or broader device coverage.

### Comment pulse

- Several homelab users combine reproducible automation with individually debuggable FreeBSD jails and separate ZFS data volumes.
- BSD's integrated networking configuration won praise; Linux remained useful for virtualization and newer heterogeneous hardware.

### LLM perspective

- View: The operating-system switch succeeded primarily by restoring curiosity, with technical coherence reinforcing that motivation.
- Impact: Self-hosters may accept narrower hardware support in exchange for understandable administration and stable interfaces.
- Watch next: Long-term maintenance, jail automation, service portability, scheduler improvements, and whether the novelty survives routine operations.
