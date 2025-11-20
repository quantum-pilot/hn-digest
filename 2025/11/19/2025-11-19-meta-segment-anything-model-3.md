# Meta Segment Anything Model 3

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45982073) | Link: https://ai.meta.com/sam3/

- TL;DR  
Meta’s Segment Anything Model 3 (SAM 3) is a unified, promptable vision model that segments and tracks objects in images and video using text, exemplar boxes, or clicks, with state‑of‑the‑art accuracy across many domains. It’s open-sourced and slated to power Instagram editing tools and Meta’s apps. Hacker News users praise its zero-shot text segmentation and auto-labeling potential, are impressed by the optional 3D mesh tool, but note weaknesses on very precise industrial and illustration tasks and open questions around latency.

- Comment pulse  
  - Zero-shot segmentation rivals specialist models → Users say SAM 3 nears custom YOLO performance and can autolabel ~90% of datasets, leaving humans mainly for correction.  
  - SAM 3D’s fast mesh extraction impresses → Demo handles occlusion and separates objects cleanly, though some are confused about exporting meshes versus only videos.  
  - Niche, high-precision tasks remain challenging → Circuit boards and kids’ drawings show rough edges; some worry about latency—counterpoint: Meta reports ~30 ms per image on GPUs.

- LLM perspective  
  - View: SAM 3 unifies language, exemplar, and click-based segmentation, pushing open-vocabulary perception beyond prior general-purpose vision-language models.  
  - Impact: Annotation-heavy fields—autonomous driving, medical imaging, environmental monitoring—could cut labeling costs dramatically and standardize teacher-model pipelines.  
  - Watch next: Open benchmarks on industrial CAD, documents, and child art, plus real-time video performance metrics on consumer hardware.
