# Show HN: Steerling-8B, a language model that can explain any token it generates

- Score: 313 | [HN](https://news.ycombinator.com/item?id=47131225) | Link: https://www.guidelabs.ai/post/steerling-8b-base-model-release/

### TL;DR
Steerling-8B is an 8B-parameter language model whose architecture is built for interpretability: every generated token can be decomposed into (1) influential prompt tokens, (2) explicit human-understandable concepts, and (3) contributing training-data sources. Using a causal discrete diffusion backbone and an embedding split into supervised concepts, learned concepts, and a residual, it routes predictions through linear concept paths, enabling exact per-concept logit attribution and real-time “knobs” to amplify/suppress concepts without fine-tuning. HN discussion centers on code attribution, alignment/safety value, and whether this granularity is practically useful or just coarse provenance metadata.

---

### Comment pulse
- Coding attribution for LLM agents → concept-level provenance could auto-generate ATTRIBUTION.md and steer away from tainted deps—counterpoint: firms won’t adopt unless regulation or strong incentives exist.  
- Alignment and safety → some see fine-grained concept toggling as essential for alignment/debugging; others argue alignment removes interesting behavior and doesn’t fix socio-technical harms.  
- Practicality of explainability → regulators in healthcare welcome structured explanations; skeptics say concept/source labels are coarse, don’t ensure truth, and resemble generic token-attribution methods.

---

### LLM perspective
- View: Architectures that encode interpretability constraints from the start are more promising than post-hoc probing for safety and debugging.  
- Impact: Most relevant for regulated domains, safety research, and enterprises needing provenance-aware coding and content generation.  
- Watch next: Independent audits of attribution fidelity, prompt-injection case studies, and head-to-head usability vs opaque 7B–13B models in real workflows.
