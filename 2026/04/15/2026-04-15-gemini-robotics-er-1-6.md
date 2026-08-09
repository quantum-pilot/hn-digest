# Gemini Robotics-ER 1.6

- Score: 204 | [HN](https://news.ycombinator.com/item?id=47779094) | Link: https://deepmind.google/blog/gemini-robotics-er-1-6/

### TL;DR

Google DeepMind released Gemini Robotics-ER 1.6 as a high-level embodied-reasoning model that can call search, vision-language-action systems, or user tools. It improves pointing, counting, task planning, multiview success detection, and physical-safety compliance, while adding instrument reading for gauges and sight glasses. Agentic vision zooms, points, and executes code, lifting the reported instrument-reading score from 86% to 93%, versus 23% for version 1.5. It is available through the Gemini API and AI Studio. Commenters saw industrial inspection value but questioned inference latency, underspecified goals, and whether cameras outperform direct sensor upgrades.

### Comment pulse

- Fast inference was seen as the missing ingredient for richer perception-planning loops — counterpoint: replicating human behavior may be the wrong robotics target.
- A vague land-care prompt exposed specification risk: valid farming practices depend on ecology, history, locality, and the operator’s actual goals.
- Analog-gauge reading sounded redundant — counterpoint: retrofitting industrial sensors can require costly hardware, shutdowns, permits, wiring, and control-system integration.

### LLM perspective

- **View:** Instrument reading is compelling because it overlays intelligence on legacy infrastructure without modifying safety-critical equipment.
- **Impact:** Better success detection can reduce brittle task scripts, but latency and false positives matter more when machines act physically.
- **Watch next:** Independent benchmark replication, end-to-end latency, calibration drift, failure detection under occlusion, and field results from Boston Dynamics deployments.
