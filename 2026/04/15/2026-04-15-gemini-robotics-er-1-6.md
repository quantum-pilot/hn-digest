# Gemini Robotics-ER 1.6

- Score: 204 | [HN](https://news.ycombinator.com/item?id=47779094) | Link: https://deepmind.google/blog/gemini-robotics-er-1-6/

### TL;DR
Google DeepMind’s Gemini Robotics‑ER 1.6 is a robot-focused Gemini variant that improves spatial reasoning, multi‑camera success detection, and a new capability: precise analog instrument reading, using “agentic vision” (zooming, pointing, and code execution) to interpret dials and sight glasses. It also tightens safety around hazardous actions and constraint following, and is accessible via Gemini API/AI Studio. HN discussion centers on speed bottlenecks for embodied AI, retrofit value in analog-heavy industries, and fuzzy objectives in autonomous land management.

### Comment pulse
- Robotics needs 100–1000× faster inference for continuous control; ASIC-style LLMs show promise but today’s embedded models are tiny and low-quality — counterpoint: inevitable scaling.  
- Autonomous land-steward robots sound appealing, but real "care" is hyper-local, value-laden traditional practice; there’s no single correct objective for ecology or agriculture.  
- Reading legacy analog gauges via cameras plus cloud AI can beat retrofitting digital sensors, avoiding plant shutdowns, rewiring, and expensive industrial transmitters.  

### LLM perspective
- View: Treating LLMs as high-level planners over toolchains is becoming the standard pattern for embodied agents, not end-to-end learned policies.  
- Impact: Near-term winners: inspection, monitoring, and retrofit automation in brownfield facilities, where sensor upgrades are cost-prohibitive but cameras are cheap.  
- Watch next: Benchmark real-world autonomy: mean time between human interventions, safety incidents per operating hour, and cost per task versus manual and traditional automation baselines.
