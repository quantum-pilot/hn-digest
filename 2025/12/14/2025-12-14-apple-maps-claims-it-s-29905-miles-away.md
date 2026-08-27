# Apple Maps claims it's 29,905 miles away

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46262950) | Link: https://mathstodon.xyz/@dpiponi/115651419771418748

### TL;DR

A brief post reports an AirTag moving around Guatemala City while Apple Maps displays a 29,905-mile distance—greater than Earth’s circumference—and argues that basic magnitude checks matter. The supplied material does not establish the bug’s cause. Commenters proposed accumulated route costs, closures represented by inflated weights, altitude mistakes, or routing rather than straight-line distance. Comparable vehicle-navigation stories showed GPS, dead reckoning, map matching, and ferry movement can produce persistent contradictions when systems distrust a new fix.

### Comment pulse

- Skeptics doubted interview estimation questions would prevent bugs rooted in routing representations, closures, or numerical accumulation.
- Vehicle anecdotes showed map matching can prefer impossible road continuity over fresh GPS evidence after ferries or parallel-road ambiguity.
- A disappearing scale bar drew criticism as a UI decision that makes simple distance sanity checks unnecessarily difficult.

### LLM perspective

- View: The screenshot indicates missing plausibility checks, but cannot distinguish display, geodesic, routing, or location-state failure.
- Impact: Absurd outputs erode trust and can hide safety-relevant navigation errors behind otherwise polished interfaces.
- Watch next: Reproduce inputs, compare straight-line and route distance, inspect closure penalties, and test coordinate normalization.
