# Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46629682) | Link: https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/

- TL;DR  
  Raspberry Pi’s AI HAT+ 2 adds a Hailo 10H NPU with 8GB LPDDR4X so it can run LLMs without using Pi system RAM. Benchmarks show the Pi 5’s CPU is usually faster for LLM inference, with the NPU only slightly more efficient and constrained by its 8GB. The HAT shines for low‑power vision workloads but overlaps with cheaper Pi AI boards, and mixed vision+LLM mode is currently unstable. HN discussion centers on Pi’s shifting mission, realistic edge‑AI uses, and AI marketing inflation.

- Comment pulse  
  - 8GB NPU RAM feels tiny for LLMs → contrast between hyping an 8GB hat while 96GB laptops are deemed “not enough” illustrates skewed expectations.  
  - Raspberry Pi lost its “revolutionary” feel → critics see aimless bandwagoning; defenders cite unmatched software, availability, GPIO, and natural evolution toward AI workloads.  
  - Hailo hats shine at object detection → practical use is multi‑camera vision (home/garden monitoring), not text LLMs—counterpoint: “AI” branding invites unrealistic chatbot expectations.

- LLM perspective  
  - View: This is mainly an edge-vision plus small‑LLM dev board, not a general-purpose local‑AI accelerator for consumers.  
  - Impact: Benefits industrial and hobbyist projects needing always‑on, low‑power vision; less compelling than a 16GB Pi for pure LLM work.  
  - Watch next: Software stack maturity (mixed workloads), real‑app benchmarks, and whether future Pi/NPUs unify memory to handle mid‑size models.
