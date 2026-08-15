# Google is making private AI practical with homomorphic encryption

- Score: 359 | [HN](https://news.ycombinator.com/item?id=49300314) | Link: https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/

### TL;DR

Google introduced HEIR, an open-source compiler toolchain that converts pretrained models to run inference directly on homomorphically encrypted inputs, returning encrypted outputs without exposing user data or shipping proprietary models to devices. Demonstrations cover recommendations, card-fraud detection, encrypted-traffic anomaly detection, and hotword recognition, with accelerator partnerships intended to reduce latency. Commenters challenged the omission of clear conventional baselines: cited workloads remain orders of magnitude slower, potentially limiting HEIR to valuable classification tasks, while local models and secure enclaves offer different privacy, efficiency, and trust tradeoffs.

### Comment pulse

- Commenters cited roughly thousand-fold or greater inference overhead, with some encrypted primitive operations taking seconds rather than milliseconds.
- That penalty may still suit valuable classifiers — counterpoint: complex agentic workflows multiply intermediate encrypted operations and could remain impractical.
- Local inference avoids cloud exposure, while shared datacenters improve utilization and secure enclaves offer lower overhead with hardware-based trust.

### LLM perspective

- View: HEIR lowers the cryptographic expertise barrier, but compilation usability and runtime practicality are separate achievements.
- Impact: Finance, healthcare, and threat detection gain an option when secrecy outweighs latency, compute, and energy costs.
- Watch next: End-to-end baseline publication, accelerator demonstrations, supported architectures, accuracy effects, and production evidence beyond narrow classifiers.
