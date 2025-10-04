# Microsoft CTO says he wants to swap most AMD and Nvidia GPUs for homemade chips

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45463642) | Link: https://www.cnbc.com/2025/10/01/microsoft-wants-to-mainly-use-its-own-ai-chips-in-the-future.html

- TL;DR
  - Microsoft CTO Kevin Scott says the company aims to run most AI data-center workloads on homegrown silicon (Maia accelerators, Cobalt CPUs) over time, optimizing full-stack systems—compute, networking, and novel microfluidic cooling—to cut cost and dependency on Nvidia/AMD amid a persistent compute crunch. They’ll still buy any chip meeting price-performance in the interim. HN notes Google’s TPU precedent and debates how much training still relies on GPUs, questions Microsoft’s hardware track record (Graphcore), and worries vertical integration limiting access—counterpoint: freeing GPUs could lower prices for others.

- Comment pulse
  - Google set the template: TPUs power scaled runs, but GPUs remain essential for prototyping, debugging, and compatibility—internal fleets still include vast numbers of Nvidia GPUs.
  - Skepticism on Microsoft’s execution: past bets (Graphcore) fizzled; credibility questioned—counterpoint: Maia 100 exists, plus Project Brainwave history shows sustained accelerator investment.
  - Vertical integration could strand everyone else on pricier Nvidia hardware; — counterpoint: hyperscalers shifting in-house may loosen supply and reduce GPU prices for smaller buyers.

- LLM perspective
  - View: This is cost, control, and energy optimization via vertical integration of silicon, networking, cooling, and software for AI workloads.
  - Impact: Long-term, reduces Nvidia/AMD leverage; near-term mixed fleets persist. Increases customer lock-in and fragmentation across cloud-specific accelerators.
  - Watch next: Independent Maia benchmarks vs Blackwell; production volumes; microfluidic deployment; PyTorch/ONNX compiler maturity; first frontier model trained primarily on Maia.
