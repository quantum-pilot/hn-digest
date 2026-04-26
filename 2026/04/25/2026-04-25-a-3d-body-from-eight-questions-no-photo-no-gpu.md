# A 3D Body from Eight Questions – No Photo, No GPU

- Score: 126 | [HN](https://news.ycombinator.com/item?id=47862541) | Link: https://clad.you/blog/posts/questionnaire-mlp/

### TL;DR
Clad shows you can reconstruct a realistic 3D body from just eight form questions (height, weight, build, shape, cup, gender, ancestry, etc.), using a tiny MLP plus a physics-aware loss that enforces correct volume, mass, and height via a differentiable body model. On synthetic and taped real bodies, it predicts height and weight almost exactly and bust/waist/hips within a few centimeters—outperforming both simple height+weight regressions and their own photo-based pipeline—while avoiding photos, GPUs, and most privacy friction.  
*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Impressive numbers, but height is an input → the metric reflects how well the generated mesh’s physical height matches the user’s stated height.  
- Past 3D-scanner jeans efforts failed from privacy, demographics, and manufacturing tolerance; a looser, questionnaire-based system could still cut returns—counterpoint: looser fits may just oversize.  
- Users notice ~10s latency in the demo; suggest precomputing a grid of measurement outputs, and note missing factors like torso–leg ratio as acknowledged limitations.

---

### LLM perspective
- View: Clever combination of synthetic data, anthropometric domain knowledge, and differentiable geometry beats “bigger model” photo pipelines for sizing.  
- Impact: Apparel e-commerce, virtual try-on, and made-to-measure workflows can get near-body-accurate sizing without cameras or heavy compute.  
- Watch next: Client-side inference, better attribute UX (interactive sliders vs “body shape”), and independent validation on diverse real-world populations.
