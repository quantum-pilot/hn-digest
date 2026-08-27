# APT Rust requirement raises questions

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46045972) | Link: https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/

### TL;DR

APT’s maintainer plans a hard Rust dependency from May 2026 for safer parsing, signature verification, and stronger testing, potentially leaving unofficial alpha, m68k, hppa, and sh4 ports on older APT versions. The article questions the unilateral deadline, whether niche parsers should instead leave APT’s core, and Debian’s unresolved handling of statically linked Rust dependencies and security rebuilds. Commenters largely separated Rust’s merits from governance: critics wanted consultation and cost-benefit analysis, while supporters argued obsolete ports should not indefinitely block modernization.

### Comment pulse

- Governance objection → a core maintainer imposed downstream work without prior consensus or a documented trade-off analysis.
- Architectural alternative → split rarely needed archive tools from core APT, allowing Rust where supported without excluding ports.
- Modernization case → memory safety and newer tooling justify progress — counterpoint: language choice does not supply tests or security automatically.

### LLM perspective

- View: Dependency policy is a social contract when one package anchors an entire distribution.
- Impact: Port maintainers and security teams inherit toolchain, rebuild, and vulnerability-tracking work beyond APT itself.
- Watch next: Seek Technical Committee review, Static-Built-Using policy, parser separation, test coverage, and port bootstrap plans.
