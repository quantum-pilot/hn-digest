# AMD Strix Halo RDMA Cluster Setup Guide

- Score: 222 | [HN](https://news.ycombinator.com/item?id=48703258) | Link: https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md

### TL;DR
Guide explains how to cluster AMD Strix Halo / AI Max 395+ machines over RDMA so their large unified memories (128–256GB) can jointly serve quantized LLMs using tools like ds4 and vLLM. Commenters are excited about “provider-like” local AI on prosumer boxes, but note steep hardware inflation and costly 100Gb NICs. Benchmarks show usable but underwhelming throughput versus Apple M4/M5 laptops and GPU rigs, so many still see cloud frontier models as more cost-effective short term.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Strix Halo RDMA clusters enable serious local LLMs → 128–256GB unified RAM plus ds4 spans nodes for 4-bit models—counterpoint: NICs and base units stay expensive.  
- Hardware cost explosion deters many → 128GB Strix laptops rose from ~€2.5k to €7k; buyers fear rapid obsolescence versus cheap, fast frontier models via APIs.  
- Performance trails Apple Silicon and midrange GPUs → reported 50 tok/s prefill and low tps; reviewers see M4 laptops achieving ~400 prefill, 20 tok/s generation.  

---

### LLM perspective
- View: Strix Halo clusters show a viable template for memory-heavy local inference, but not yet a clear value win.  
- Impact: Homelabbers and small teams can prototype agentic systems without GPUs, trading energy and latency for data control.  
- Watch next: better RDMA support on Apple/PC laptops, DS4 optimizations, and vendor mini-clusters with integrated high-speed networking.
