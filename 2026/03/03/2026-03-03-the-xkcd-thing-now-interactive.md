# The Xkcd thing, now interactive

- Score: 1102 | [HN](https://news.ycombinator.com/item?id=47230704) | Link: https://editor.p5js.org/isohedral/full/vJa5RiZWs

### TL;DR
An XKCD-style “internet/stack” diagram has been turned into an interactive physics toy: you can drag components around like a wobbly Jenga tower and watch infrastructure, clouds, cables, and “whatever Microsoft is doing” collapse. HN enjoys the humor (especially bits like AWS towering over unpaid developers and sharks biting undersea cables), notes that the author is using it to teach motion/physics with Matter.js, and offers small JS-UX fixes plus pedantic infra tweaks (e.g., DNS vs BGP).

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Interactive parody of infrastructure hits home → gags like AWS over unpaid devs, AI crank, sharks on cables mirror real ecosystem tensions—counterpoint: infra labeling (DNS vs BGP) irks purists.  
- Implementation could be smoother → binding drag mousemove to `window` avoids losing events when cursor leaves frame, a common front-end gotcha.  
- Educational angle appreciated → author uses Matter.js in a p5.js course; slightly unstable “starting state” sparks discussion on floating point and JS determinism.

---

### LLM perspective
- View: Playful, interactive diagrams of complex stacks explain modern infra dynamics better than static memes or dense architecture docs.  
- Impact: Helps students, junior engineers, and non-tech stakeholders internalize dependency fragility and platform concentration risks.  
- Watch next: Similar interactives for supply chains, AI model stacks, or cloud billing layers, ideally with toggles for “realistic” vs “satirical” modes.
