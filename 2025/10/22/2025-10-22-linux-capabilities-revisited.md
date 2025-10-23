# Linux Capabilities Revisited

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45669142) | Link: https://dfir.ch/posts/linux_capabilities/

- TL;DR
    - The post shows how Linux file capabilities can quietly grant powerful privileges: adding cap_setuid+ep to /usr/bin/python lets any user spawn a root shell without SUID. It walks defenders through discovery (getcap, /proc Cap*, capsh, getpcaps), removal (setcap -r), and where data lives (security.capability xattr), plus detections (Elastic rule) and LinPEAS checks. HN debates whether Linux’s flags are “real” capabilities, noting they’re coarse, ambient, and hard to reason about; alternatives like fd-based handles, Capsicum/Pledge, and centralized management are favored.

- Comment pulse
    - Linux capabilities aren’t object capabilities → Coarse, ambient, inherited flags; prefer explicit, transferable fd-like handles; point to Capsicum/Pledge — counterpoint: strict parent-child inheritance can reduce usability.
    - Global namespaces impede reasoning → Need scoped namespaces and hierarchical capability delegation; retrofitting POSIX is hard, true capability systems benefit from capability-first kernel design.
    - Fine-grained ACLs risk escalation paths → Mis-scoped rights become privilege bridges; answer is rigorous audits and a centralized, diffable capability registry.

- LLM perspective
    - View: Treat file capabilities as a high-signal persistence/escalation vector; restrict who can set them and alert on any change to security.capability.
    - Impact: Blue teams, distro maintainers, and container builders should baseline allowed capabilities and fail CI/CD when unexpected caps appear.
    - Watch next: Whitelisted-capability policies, package-manager verification of caps, and routine fleet scans comparing /proc capability sets to baselines.
