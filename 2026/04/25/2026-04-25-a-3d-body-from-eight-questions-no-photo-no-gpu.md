# A 3D Body from Eight Questions – No Photo, No GPU

- Score: 126 | [HN](https://news.ycombinator.com/item?id=47862541) | Link: https://clad.you/blog/posts/questionnaire-mlp/

### TL;DR

Clad maps eight questionnaire answers to 58 Anny body parameters using two small, gender-specific MLPs trained on tens of thousands of synthetic bodies. A differentiable body-model pass adds height, mass, and waist constraints, producing mean synthetic errors near 0.3 cm for height, under 0.5 kg for mass, and roughly 3–5 cm for major circumferences on CPU. The result is a population-average starting shape, not an exact twin. HN saw potential for fewer apparel returns but stressed that product adoption and manufacturing matter beyond benchmark accuracy.

### Comment pulse

- Levi’s earlier scanner-based custom-jeans program struggled with demographics, privacy, and factory tolerances, suggesting prediction alone does not guarantee adoption.
- An 85 KB model could run in-browser — counterpoint: the demo reportedly submits inputs to a server when generating.
- Torso-to-leg ratio is absent from inputs, limiting fit for bodies whose proportions differ from the model’s conditional average.

### LLM perspective

- Report real-person cohort size, demographic coverage, p95 errors, and calibration separately from synthetic validation.
- Evaluate size recommendation accuracy and return reduction; circumference MAE is only a proxy for commercial value.
- Interactive shape adjustment may capture user knowledge that categorical body-shape labels miss.
