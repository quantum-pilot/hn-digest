# I regret building this $3000 Pi AI cluster

- Score: 400 | [HN](https://news.ycombinator.com/item?id=45302065) | Link: https://www.jeffgeerling.com/blog/2025/i-regret-building-3000-pi-ai-cluster

- TL;DR
    - Jeff Geerling’s 10-node Raspberry Pi CM5 blade cluster (~$3k, 160 GB RAM) was tedious to build and underwhelms. After fixing thermals it reached 325 Gflops at ~130 W—4× slower than a $8k Framework cluster, only slightly better in Gflops/W and worse $/flop. AI fares worse: no usable iGPU acceleration, CPU-only yields ~6 tok/s (3B) and 0.28–0.85 tok/s on 70B across nodes, fragile and 5–25× slower. Niche wins: dense, isolated nodes (CI, Tor). HN’s verdict: prefer one big box with VMs; scale-out overheads dominate; Pis shine for education/IO.

- Comment pulse
    - Scale up: one multi-core PC with VMs beats Pi clusters for learning and perf/W; simpler, cheaper, lower idle; good for practicing DB replication/Hadoop.
    - Parallel overheads: scale-out adds coordination costs beyond Amdahl; often faster to avoid work—single-node implementations win more often.
    - Pi intent: great for education/IO tinkering, poor CPU; — counterpoint: ecosystem and ease make it ideal for sensors, servos, full Linux projects.

- LLM perspective
    - View: Without usable GPU/NPU acceleration and higher memory bandwidth, ARM SBC clusters can’t compete for modern AI/HPC.
    - Impact: Spend $1–3k on a single x86 box with VMs or used GPUs; reserve Pis for dense, isolated edge workloads.
    - Watch next: llama.cpp Vulkan on Pi 5, NPU enablement, distributed inference frameworks’ scaling; compare Ceph/object-storage on Pis versus mini-PCs.
