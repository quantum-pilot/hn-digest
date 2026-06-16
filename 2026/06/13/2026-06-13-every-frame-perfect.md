# Every Frame Perfect

- Score: 844 | [HN](https://news.ycombinator.com/item?id=48516251) | Link: https://tonsky.me/blog/every-frame-perfect/

- TL;DR  
The article argues that UI animations should be designed so any single frame—if screenshotted mid-motion—still “makes sense,” because visual polish strongly shapes user trust. The author shows macOS and YouTube transitions where elements move out of sync or jump oddly, creating misleading or confusing intermediate states. Hacker News debates whether judging animations frame-by-frame matches how humans actually perceive motion, how much motion is necessary at all, and whether the author’s maxim is realistic or meaningfully justified.

- Comment pulse  
  - Motion-perception focus → Human vision integrates over time; a “wrong” still can be optimal in motion, like motion blur in film — counterpoint: unlike film, UI in-betweens are fully designed.  
  - Motion vs minimalism → Some want snappy, mostly-static UIs; others say careful animation aids orientation, hides latency, and is standard in well-crafted game UIs.  
  - Quality, latency, and critique → Nostalgia for old Apple smoothness; some insist low latency beats polish; one critic calls the piece shallow, another defends it as a useful design prompt.

- LLM perspective  
  - View: Use “every frame perfect” as a heuristic: intermediate states must be logically consistent, even if not individually beautiful.  
  - Impact: Stronger animation guidelines in design systems and UI frameworks could prevent desynchronization without increasing latency.  
  - Watch next: Empirically compare user trust and task performance for instant transitions vs refined animations under realistic network and device conditions.
