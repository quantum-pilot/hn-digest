# Spectral Labs releases SGS-1: the first generative model for structured CAD

- Score: 302 | [HN](https://news.ycombinator.com/item?id=45319876) | Link: https://www.spectrallabs.ai/research/SGS-1

TL;DR
- Spectral Labs’ SGS-1 generates editable B‑Rep STEP parts from images/meshes and claims superior accuracy versus GPT‑5 and HoLa on a 75‑image benchmark. Demos show sketch‑to‑STEP, mesh‑to‑STEP, and assembly‑context part generation; limits include organic curvature, thin features, and one‑shot assemblies. HN applauds moving beyond meshes and potential for scan cleanup and reverse engineering, but challenges the “parametric” claim since STEP lacks feature history/constraints and reports geometry errors. Others want AI for repetitive CAD tasks; 3D spatial reasoning remains a sticking point.

Comment pulse
- STEP isn’t parametric → rationale: no feature tree; user test found misaligned holes/fillets — counterpoint: feature-recognition tools help; clean B‑Rep edits better than meshes.
- Biggest win is scan cleanup and mesh/point‑cloud to STEP → rationale: enables reverse engineering, object segmentation, metadata extraction.
- Next step is inferring constraints for native CAD → rationale: STEP→SolidWorks/NX with feature recognition; vendor says they’re considering it.

LLM perspective
- View: Promising B‑Rep generation, but “parametric” conflation warrants skepticism; needs third‑party audits and CAD‑pro workflows, not cherry‑picked demos.
- Impact: If robust, reduces hours spent on STL‑to‑STEP, sketch digitization, and assembly fit iterations in SMB manufacturing and prototyping shops.
- Watch next: Public benchmarks, failure modes, STEP cleanliness metrics, native‑CAD plugins, constraint inference, and physics‑RL proof improving thin features/organic curvature.
