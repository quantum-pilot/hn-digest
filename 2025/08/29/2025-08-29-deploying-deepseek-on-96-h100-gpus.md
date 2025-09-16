# Deploying DeepSeek on 96 H100 GPUs

- Score: 285 | [HN](https://news.ycombinator.com/item?id=45064329) | Link: https://lmsys.org/blog/2025-05-05-large-scale-ep/

- TL;DR
    - SGLang open-sourced a DeepSeek-V3 inference stack that nearly matches DeepSeek’s own throughput on 96 H100s. Using prefill–decode disaggregation, expert parallelism (DeepEP/DeepGEMM/EPLB), and two-batch overlap, they report ~52k prefill and ~22k decode tokens/sec per node (2k prompts), up to 5× over vanilla tensor parallelism. They estimate ~$0.20 per 1M output tokens on rented GPUs. HN debates true margins—utilization, regional constraints, cloud vs. owned hardware—and flags GB200/FP4 as the likely next speedup.

- Comment pulse
    - Utilization erodes margins → Peak/off-peak skew and data-residency rules push utilization to 10–20%; inference-only shops can’t backfill. — counterpoint: provision near-average, shed load, batch tiers.
    - Cloud pricing skews math → AWS p5 rates overstate costs; Atlas ~$1.8/H100/hr or RunPod ~$2/H100/hr imply ~$0.08/M input and ~$0.18–0.20/M output.
    - Owning hardware can win → 8×H100 node ≈$300k; 12 nodes ≈$4–5M; beats AWS after ~18 months but adds failures, networking, colo, operations.

- LLM perspective
    - View: Open-source PD disaggregation + DeepEP/DeepGEMM/EPLB shows MoE inference scales best with DP-heavy layouts, not large TP.
    - Impact: Lower per-token cost and memory enable 4× larger batches; smaller teams can self-host DeepSeek-class models competitively.
    - Watch next: TTFT/ITL cuts, DP-attention with MTP, EPLB under distribution shift, and Blackwell FP4/GB200 benchmarks and kernels.
