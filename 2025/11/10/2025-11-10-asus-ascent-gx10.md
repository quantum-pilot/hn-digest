# Asus Ascent GX10

- Score: 182 | [HN](https://news.ycombinator.com/item?id=45877149) | Link: https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/

- TL;DR
  - ASUS’s Ascent GX10 is a compact desktop built on NVIDIA’s GB10 Grace Blackwell (DGX Spark) platform: up to 1 PFLOP FP4, 128GB unified LPDDR5X, NVLink‑C2C, and ConnectX‑7 to link two nodes (advertised support up to 405B Llama). It ships with DGX OS and NVIDIA’s AI stack for turnkey prototyping, fine‑tuning, and inference. HN fixes gaps in ASUS’s vague FAQ (memory bandwidth ~273–300 GB/s), debates Carmack’s performance critique, and compares pricing and early benchmarks against AMD Ryzen AI Max mini‑PCs.

- Comment pulse
  - Specs opaque: FAQ dodges memory bandwidth; real is ~273–300 GB/s (LPDDR5X 256‑bit), far below HBM. — counterpoint: secondary ASUS FAQ cites 273 GB/s.
  - Essentially a DGX Spark variant; slightly cheaper storage configs. Carmack’s “half-spec” claim disputed; sustained performance hinges on thermals and CPU+GPU power budget.
  - Early benchmarks (ServeTheHome, GMKtec) show mixed results vs Ryzen AI Max minis: NVIDIA wins some models, loses others; first-token latency and throughput trade off.

- LLM perspective
  - View: 128GB unified-memory GB10 boxes suit on-desk prototyping and quantized LLM fine‑tuning; inadequate for full training of large models.
  - Impact: Brings NVLink‑C2C coherence and NVIDIA AI stack to desks; reduces reliance on shared clusters and cloud for mid-scale workloads.
  - Watch next: Independent sustained-performance, memory-bandwidth, and thermals; Linux stack stability; pricing of ASUS vs Dell/Lenovo; dual-node scaling with ConnectX‑7.
