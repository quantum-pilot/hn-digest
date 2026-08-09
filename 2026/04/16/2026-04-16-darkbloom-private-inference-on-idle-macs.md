# Darkbloom – Private inference on idle Macs

- Score: 468 | [HN](https://news.ycombinator.com/item?id=47788542) | Link: https://darkbloom.dev

### TL;DR

Darkbloom proposes an OpenAI-compatible marketplace that routes encrypted inference to idle Apple Silicon, claiming up to 70% lower prices and near-total operator revenue. Its design combines hardware-bound keys and attestation, signed responses, OS hardening, blocked debugging, and optional Hypervisor.framework isolation. Hacker News challenged both sides of the pitch: early operators saw no paid requests and broken model loads, projected earnings assume demand and utilization, installation involves MDM, and Macs lack a public enclave for arbitrary code, making “verifiable privacy” depend heavily on OS and hypervisor claims.

### Comment pulse

- Idle hardware lowers marginal compute cost — counterpoint: bursty demand and necessary overprovisioning sharply reduce utilization and operator earnings.
- An early installer received health checks but no inference jobs, while image and audio models failed to load.
- Attestation can verify binaries, but critics said Secure Enclave-backed identity does not prove confidential GPU execution against the machine’s owner.

### LLM perspective

- **View:** Darkbloom’s marketplace thesis is plausible; its privacy guarantee is the hardest requirement and needs adversarial proof, not presentation-level assurance.
- **Impact:** Mac owners monetize surplus capacity, users trade centralized providers for unfamiliar operators, and enterprises inherit a new trust model.
- **Watch next:** Independent memory-isolation audits, demand, utilization distributions, MDM permissions, installer maturity, request benchmarks, incident handling, and sustainable operator payouts.
