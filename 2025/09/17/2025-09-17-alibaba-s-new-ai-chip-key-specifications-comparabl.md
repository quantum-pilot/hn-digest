# Alibaba's new AI chip: Key specifications comparable to H20

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45273747) | Link: https://news.futunn.com/en/post/62202518/alibaba-s-new-ai-chip-unveiled-key-specifications-comparable-to

- TL;DR
  - Alibaba’s chip arm Pingtouge unveiled a PPU that, per CCTV, tops NVIDIA’s export A800 and nears H20: 96GB HBM2e, up to 700GB/s interconnect, PCIe 5.0, 400W (H20 uses HBM3, higher interconnect, 550W). China Unicom’s Sanjiangyuan center reportedly signed for 16,384 Pingtouge cards within 22,832 domestic cards (3,479P). HN debates center on CUDA/software moat and a 1.5–2 gen hardware lag, export controls lowering the target, and China’s reported Nvidia-order ban hastening ecosystem shifts amid smuggling and reliability concerns.

- Comment pulse
  - China’s Nvidia-order ban → domestic shift; smuggling likely; rental loopholes questioned — counterpoint: may slow China’s LLMs while easing GPU scarcity for others.
  - Nvidia’s moat is CUDA, not hardware; Chinese PPUs trail Blackwell ~1.5–2 gens and lack EUV; AMD competitive but constrained by TSMC capacity and weaker software/drivers.
  - Export limits lower the bar (H20-class parity); China signs large domestic deployments, yet integration hiccups (e.g., reported Huawei/DeepSeek delays) highlight software, driver, and reliability gaps.

- LLM perspective
  - View: Spec parity vs H20 doesn’t guarantee competitive training; software stack, kernels, and interconnect topology determine real throughput and utilization.
  - Impact: Chinese clouds redirect spend to domestic PPUs; Nvidia demand shifts abroad; open frameworks and CUDA translation layers gain funding.
  - Watch next: Independent training benchmarks, failure rates, kernel/compiler maturity, packaging yields, HBM supply, and rules on offshore rentals and smuggling.
