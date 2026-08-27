# Ray Marching Soft Shadows in 2D (2020)

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46066695) | Link: https://www.rykap.com/2020/09/23/distance-fields/

### TL;DR

The tutorial builds fast 2D shadows from a distance field, which tells each pixel how far it is from the nearest shape. A ray can safely advance by that distance, avoiding both one-pixel stepping and missed obstacles. Hard shadows become soft by tracking the minimum ratio of shape distance to ray progress, then applying quadratic light falloff. The effect is deliberately nonphysical but visually effective. A fixed step limit prevents pathological cost, while improved distance estimates and randomized shorter steps trade banding for grain.

### Comment pulse

- Readers noted that several illustrations are interactive but insufficiently labeled, particularly on mobile.
- Discussion suggested gradients might permit larger safe steps, though curved surfaces require more information to preserve correctness.

### LLM perspective

- View: The tutorial succeeds by exposing the approximation and its aesthetic goal instead of claiming physical accuracy.
- Impact: Distance fields turn expensive visibility checks into adaptive steps suitable for responsive visual effects.
- Watch next: Better artifact suppression, clearer interactive affordances, and performance comparisons across mobile hardware.
