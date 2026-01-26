# A macOS app that blurs your screen when you slouch

- Score: 433 | [HN](https://news.ycombinator.com/item?id=46754944) | Link: https://github.com/tldev/posturr

### TL;DR
- Posturr is an open-source macOS menu-bar app that uses the camera and Apple’s Vision framework to track head/shoulder position and infer slouching. As posture worsens it progressively blurs all displays; sitting up clears the blur immediately. Users can tune sensitivity, dead zone, calibration, and a compatibility blur mode that avoids private CoreGraphics APIs; all processing is local with no accounts or cloud. HN discussion questioned “good posture” dogma and praised LLMs for making such indie apps feasible.

### Comment pulse
- Slouching correlates with “in the zone” deep work for many; they’d rather blur the screen when context-switching to distracting apps than when slouching.  
- App illustrates the “great‑AI‑unlock”: strong programmers in other stacks can now ship polished native tools quickly by offloading API boilerplate and exploration to LLMs.  
- Several argue there’s no single scientifically backed “good posture”; movement and varied positions matter more—counterpoint: others find neutral‑spine setups and monitor height crucial for comfort.  

### LLM perspective
- View: Shows a neat pattern: single‑file Swift app, computer vision, and a novel UX nudge packaged as a tiny menu utility.  
- Impact: Lowers barrier for ergonomic experiments; expect clones that detect fatigue, eye‑strain, or distraction signals rather than just posture.  
- Watch next: Interesting testbed for Apple policy: private blur APIs vs App‑Store‑safe paths, and whether similar wellness tools appear on other platforms.
