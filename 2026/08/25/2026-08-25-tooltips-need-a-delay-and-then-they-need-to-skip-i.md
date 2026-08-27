# Tooltips need a delay, and then they need to skip it

- Score: 224 | [HN](https://news.ycombinator.com/item?id=49436786) | Link: https://blog.master.dev/tooltips-need-a-delay-and-then-they-need-to-skip-it/

### TL;DR

A polished tooltip should wait about 200ms on the first hover, preventing accidental popups as a cursor crosses the page. Once one opens, the interface becomes “warm”: nearby tooltips appear instantly during a 300ms window, then revert to delayed behavior. The React example shares this state through a provider and refs, avoiding mass rerenders. HN recognized the pattern as longstanding desktop-interface hysteresis, praised its usability, and questioned reinventing native behavior and the article’s demonstration quality.

### Comment pulse

- The pattern is proven, not novel → classic Apple and Windows interfaces already used delayed-then-instant tooltips.
- Shared temporal state creates polish → hysteresis distinguishes intentional exploration from incidental cursor travel.
- Native controls may suffice → custom tooltips can recreate solved problems or obstruct primary interactions.

### LLM perspective

- View: Small timing rules encode user intent more effectively than visually elaborate animation.
- Impact: Dense interfaces become calmer during transit yet remain fast during deliberate inspection.
- Watch next: Test keyboard, touch, screen-reader, reduced-motion, and pointer-speed behavior.
