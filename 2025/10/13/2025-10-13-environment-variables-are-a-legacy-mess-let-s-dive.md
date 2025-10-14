# Environment variables are a legacy mess: Let's dive deep into them

- Score: 206 | [HN](https://news.ycombinator.com/item?id=45570537) | Link: https://allvpv.org/haotic-journey-through-envvars/

- TL;DR
  - The piece demystifies env vars: inherited via execve, placed on the stack, liberally formatted strings with size limits. Implementations differ: Bash uses stacked hashmaps; glibc a linear environ; Python mirrors glibc with one-way updates. POSIX only forbids '=' in names; uppercase is convention, not rule; author advises ^[A-Z_][A-Z0-9_]* with UTF-8 values. HN pivots to secrets: env vars are convenient yet leaky; vaults/Kubernetes/systemd credentials reduce exposure but add lock-in; setenv/getenv are unsafe—prefer setting env at exec.

- Comment pulse
  - Env vars are pragmatic for config; poor for secrets → inherit broadly, inspectable, subprocess leakage; vaults/Kubernetes/systemd credentials reduce exposure — counterpoint: add lock-in and fragility.
  - POSIX setenv/getenv are unsafe in libraries → raw pointer races; instead supply environment only via execve; some OSes provide thread-safe getenv_r clones.
  - Env layering is opaque in large orgs → tracing and schema tools help (Node --trace-env; Varlock, mise) to audit accesses and validate types.

- LLM perspective
  - View: Envvars are a lowest-common-denominator process boundary; fine for configuration knobs, but minimize use for secrets and interprocess signalling.
  - Impact: Standardize names/types early, isolate secret access to short-lived processes, and avoid mutating global environments after startup.
  - Watch next: Practical adoption of systemd credentials, memfd_secret, safer getenv_r APIs, and container runtimes offering clearer secret lifecycles.
