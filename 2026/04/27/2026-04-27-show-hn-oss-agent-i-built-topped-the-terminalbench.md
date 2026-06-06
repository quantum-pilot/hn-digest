# Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview

- Score: 289 | [HN](https://news.ycombinator.com/item?id=47920787) | Link: https://github.com/dirac-run/dirac

- TL;DR  
Dirac is an open-source coding agent (VS Code/CLI) optimized for token-efficient large refactors via AST-based context curation, hash-anchored edits, and multi-file batching. On TerminalBench 2 with Gemini‑3‑flash‑preview it tops the leaderboard, beating Google’s harness and other agents while cutting API cost by ~65%. HN discussion probes whether gains generalize beyond Gemini, and how much harness design matters versus model choice. Commenters debate hash-anchor efficiency, language coverage, and raise opt‑out telemetry and proxying concerns for a single‑dev project.

- Comment pulse  
  - Aggressive context tricks → hash-anchored edits, AST-based selection, batched tools, helper scripts; skeptics think file skeletons, not anchors, explain token savings — counterpoint: author disagrees.  
  - Benchmarks questioned → results currently Gemini‑only; commenters want cross-model runs, latency metrics, and harness-focused leaderboards given huge gains over Google’s official setup.  
  - Telemetry raises trust issues → tool sends machine ID, errors, web queries via Dirac servers default — counterpoint: author says data minimal, inherited from Cline.  

- LLM perspective  
  - View: Harness engineering (context curation, tool APIs) increasingly determines real-world coding performance, sometimes more than switching to a slightly better model.  
  - Impact: Teams shipping AI devtools should invest in AST-aware tooling, deterministic edits, and batching before chasing every new frontier model.  
  - Watch next: Independent evaluations across multiple model families, plus clearer privacy controls or telemetry-free builds, will decide whether Dirac becomes a trusted default.
