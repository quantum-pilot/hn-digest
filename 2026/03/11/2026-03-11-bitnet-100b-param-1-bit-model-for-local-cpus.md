# BitNet: 100B Param 1-Bit model for local CPUs

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47334694) | Link: https://github.com/microsoft/BitNet

### TL;DR

Microsoft's bitnet.cpp is an inference framework for ternary 1.58-bit LLMs on CPUs and GPUs, with NPU support planned. It claims 2.37–6.17× x86 CPU speedups and 71.9–82.2% energy reductions, plus 100B-class inference at 5–7 tokens per second on one CPU. The crucial caveat: no trained 100B model is released; Microsoft's official model is 2.4B. HN saw promising memory-bandwidth economics but criticized the recycled headline, limited models, from-scratch training requirement, and weak evaluation evidence.

### Comment pulse

- Ternary weights replace many multiplications with additions → custom inference hardware could be simpler and more memory-bandwidth efficient.
- Parameter efficiency may lag FP16 → one cited paper suggests roughly 4–5× more parameters, complicating headline comparisons.
- Five-to-seven tokens per second is usable but not fluid → several users target about ten for comfortable reading.

### LLM perspective

- **View:** This is an infrastructure milestone awaiting proof from a competitive large trained model.
- **Impact:** Local inference could trade model selection and quality for sharply lower RAM and energy needs.
- **Watch next:** A trained 100B release, evaluations, reproducible throughput, and comparisons against four-bit post-training quantization.
