# CERN uses ultra-compact AI models on FPGAs for real-time LHC data filtering

- Score: 299 | [HN](https://news.ycombinator.com/item?id=47552562) | Link: https://theopenreader.org/Journalism:CERN_Uses_Tiny_AI_Models_Burned_into_Silicon_for_Real-Time_LHC_Data_Filtering

- TL;DR  
CERN’s LHC produces tens of thousands of exabytes of collision data yearly, so only ~0.02% can be saved. To decide in tens of nanoseconds which events are worth keeping, CERN runs ultra-compact neural networks directly on Level-1 trigger FPGAs, with weights hard‑wired into the fabric and heavy use of lookup tables for near-instant responses. Models like AXOL1TL and CICADA perform anomaly detection on detector signals; a CPU/GPU farm then does higher-level filtering. Work is being scaled up for the High-Luminosity LHC.

- Comment pulse  
  - “Burned into silicon” is misleading → models live on reprogrammable FPGAs with hard-wired, heavily quantized weights and distributed-arithmetic tricks.  
  - Algorithms matter → these are small VAEs (plus VICReg/distillation) for anomaly detection; omission of details feels like AI buzzwording — counterpoint: public papers/slides fill that gap.  
  - Not unprecedented → HEP has used FPGAs and even neural triggers for decades; CPUs already embed tiny perceptrons for branch prediction.

- LLM perspective  
  - View: This is a flagship example of “tiny, specialized AI” beating general-purpose accelerators under extreme latency and power constraints.  
  - Impact: Pushes EDA, quantization-aware training, and FPGA ML tooling; useful for telecoms, radar, embedded vision, and safety-critical controllers.  
  - Watch next: Open-source hls4ml flows, HL-LHC trigger designs, and ASIC versions of these anomaly detectors for even harsher environments.
