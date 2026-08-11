# The Xkcd thing, now interactive

- Score: 1102 | [HN](https://news.ycombinator.com/item?id=47230704) | Link: https://editor.p5js.org/isohedral/full/vJa5RiZWs

### TL;DR

The p5.js sketch turns XKCD’s Dependency diagram into a Matter.js physics simulation. Its labeled stack begins as static rectangles above a fixed floor; the first click makes every block dynamic, letting gravity collapse modern digital infrastructure while users grab and drag pieces. Coordinates reproduce the original layout, random fills distinguish bodies, and each frame redraws the background and updated positions. Commenters enjoyed how the unstable structure sharpens the joke, proposed BGP and other modern additions, and identified a practical drag bug when the pointer leaves the frame.

### Comment pulse

- An unstable initial stack improves the metaphor → even untouched infrastructure may eventually collapse from tiny implementation differences.
- Registering pointer movement on the window would preserve dragging after the cursor leaves the embedded canvas.
- Community remixes suggested BGP, AWS, AI, sharks, and a dependency manager appropriately named Jenga.

### LLM perspective

- **View:** Interactivity converts a familiar dependency metaphor from static satire into a small systems-behavior experiment.
- **Impact:** The sketch gives physics students a compact example combining assets, rigid bodies, input constraints, and animation.
- **Watch next:** Better out-of-frame dragging, deterministic starting conditions, touch support, and selectable dependency-stack variants.
