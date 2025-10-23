# Starcloud

- Score: 162 | [HN](https://news.ycombinator.com/item?id=45667458) | Link: https://blogs.nvidia.com/blog/starcloud/

- TL;DR
    - Starcloud, an NVIDIA-backed startup, proposes space-based data centers powered by constant solar and cooled via radiative heat sinks, starting with a November launch of an H100-equipped satellite. They tout 10x cheaper energy, large water savings, and near-instant in-orbit inference for Earth-observation workloads, scaling to a 5‑GW platform with kilometer-scale panels and future Blackwell GPUs. HN pushes back: cooling area, launch/maintenance, radiation bit flips, latency/bandwidth, debris, and bold timelines look prohibitive—though some see niche value in off-Earth jurisdiction and continuous solar.

- Comment pulse
    - Radiative cooling bottlenecks → Stefan–Boltzmann limits demand kilometer-scale radiators for multi‑GW heat; shading, orientation, and deployment negate “free” space energy.
    - Ops/robustness are hard → radiation upsets, debris, stationkeeping, no maintenance force redundancy, increasing mass/cost — counterpoint: niche high-security, extra-sovereign use could pay.
    - Water/cooling narrative debated → datacenter water is often evaporated and can harm ecosystems; others say impacts are overstated but politically potent, fueling local opposition.

- LLM perspective
    - View: Technically intriguing, but economics hinge on radiator mass/area, autonomous servicing, and reliable high-throughput downlink; otherwise it’s a marketing demo.
    - Impact: If viable, shifts energy/cooling externalities off-grid, but increases orbital risk, favors sovereign-poor actors, and concentrates power with launch-capable ecosystems.
    - Watch next: Thermal budget per kW, H100 SEU rates, sustained downlink >10 Gbps, radiator density <5 kg/m², debris/insurance, licensing.
