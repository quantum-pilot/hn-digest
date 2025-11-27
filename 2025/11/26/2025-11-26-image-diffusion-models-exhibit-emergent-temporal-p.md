# Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

- Score: 110 | [HN](https://news.ycombinator.com/item?id=46055177) | Link: https://arxiv.org/abs/2511.19936

- TL;DR  
Researchers show that standard text-to-image diffusion models, trained only on still images, contain attention patterns that can act as label-propagation kernels across video frames. Their DRIFT framework uses these internal features, plus test-time tricks and SAM-based refinement, to perform state-of-the-art zero-shot video object tracking from a single annotated frame, no video training needed. HN commenters highlight this as another emergent capability of old diffusion models and discuss better soft IoU-style metrics for evaluating segmentations.

- Comment pulse  
  - Diffusion models encode rich semantics; even 2022-era Stable Diffusion can be repurposed and hacked for new tasks—counterpoint: dedicated flow-based models might ultimately outperform such retrofitting.  
  - Paper shows text-to-image diffusion’s attention maps can segment objects and propagate labels frame-to-frame, enabling zero-shot video object tracking from a single annotated frame.  
  - Commenter argues soft IoU and fuzzy operators yield more reliable segmentation metrics than hard thresholds, urging authors to consider non-binary ground truths.

- LLM perspective  
  - View: Repurposing frozen diffusion models for dense perception suggests multimodal foundation models may unify generation and understanding without separate architectures.  
  - Impact: Cheaper video analytics and tracking in domains lacking labeled video—robotics, surveillance, sports—by leveraging existing image generators plus test-time optimization.  
  - Watch next: Benchmarks comparing diffusion-based trackers to specialized video transformers; robustness studies under occlusion, motion blur, and long-horizon propagation.
