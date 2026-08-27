# Seven diabetes patients die due to undisclosed bug in Abbott's glucose monitors

- Score: 440 | [HN](https://news.ycombinator.com/item?id=46388040) | Link: https://sfconservancy.org/blog/2025/dec/23/seven-abbott-freestyle-libre-cgm-patients-dead/

### TL;DR

Software Freedom Conservancy's Bradley Kuhn says recalled Abbott FreeStyle Libre sensors produced dangerously incorrect glucose readings, with 736 severe adverse events and seven deaths reported as potentially associated. He argues opaque medical devices prevent independent investigation and that public hardware specifications plus corresponding source would enable broader safety review, though FOSS cannot guarantee correctness. Diabetic commenters question the headline's causal certainty and whether the defect was software, hardware, or manufacturing, while explaining how sustained false readings can trigger harmful insulin decisions.

### Comment pulse

- Causality is not established → Abbott reported deaths potentially associated with the issue, not proven to have been caused by it.
- CGMs require verification → experienced users check surprising readings with fingersticks and bodily symptoms, though vulnerable patients may not manage that reliably.
- Error direction matters → false highs risk insulin overdose; prolonged false lows can suppress insulin and contribute to ketoacidosis.

### LLM perspective

- View: Transparency would improve independent diagnosis, but the evidence supplied cannot localize the defect or prove seven causal deaths.
- Impact: Patients need clearer failure guidance while regulators and researchers need technical incident data.
- Watch next: Abbott and regulators should publish affected lots, error modes, causal analyses, mitigations, and software-versus-hardware findings.
