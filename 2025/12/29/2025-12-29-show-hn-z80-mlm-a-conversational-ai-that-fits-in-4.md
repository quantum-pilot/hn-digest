# Show HN: Z80-μLM, a 'Conversational AI' That Fits in 40KB

- Score: 463 | [HN](https://news.ycombinator.com/item?id=46417815) | Link: https://github.com/HarryR/z80ai

### TL;DR
A hobbyist project trains a tiny 2‑bit–quantized neural network that runs entirely on a vintage 4 MHz Z80 with 64 KB RAM, packaged as a 40 KB CP/M `.COM` file. It uses trigram hash encoding into 128 buckets and fully integer 16‑bit inference to generate short, personality‑laden character responses. Included demos are a minimalist chatbot and a 20‑questions game. HN discussion revolves around “minimal viable LLMs,” retro alternate histories, and what such tiny models imply for secrecy and interpretability.

---

### Comment pulse
- Retro ML delight → People with FORTRAN neural nets and CP/M emulators see this as the “road not taken” for 60s–90s hardware.  
- Minimal cognitive core → Thread explores ultra‑small conversational models, huge contexts, and Karpathy’s “cognitive core” idea—counterpoint: such tiny nets likely hit hard limits on reasoning depth.  
- Secrets and backdoors → Question whether a trained‑in passphrase is recoverable from weights; replies point to backdoor research and note that tiny networks are especially easy to analyze.

---

### LLM perspective
- View: Clever combo of aggressive quantization and lossy trigram hashing to make “LLM‑like” behavior fit absurdly small footprints.  
- Impact: Inspires educational demos, retro ports, and tinyML deployments on MCUs without FPUs or large RAM.  
- Watch next: Benchmarks versus simple n‑gram baselines, ports to 6502/AVR, and generalized tooling for training similar micro‑models.
