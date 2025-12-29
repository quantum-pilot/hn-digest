# What an unprocessed photo looks like

- Score: 153 | [HN](https://news.ycombinator.com/item?id=46415225) | Link: https://maurycyz.com/misc/raw_photo/

- TL;DR
    - The post reverse-engineers how a camera turns raw sensor voltages into a pleasant JPEG. It rescales the limited ADC range, demosaics the Bayer filter, corrects white balance, and applies nonlinear tone curves to compress dynamic range and match human brightness perception. The final comparison shows the camera’s own JPEG is already heavily processed. HN commenters expand on demosaicing, gamma, and what “fake” means in an era of AI-altered photos.

- Comment pulse
    - Bayer pattern and green channel → Extra green encodes most luminance; advanced demosaicing reconstructs green first, with red/blue as lower-resolution chroma—bad handling ruins grayscale outputs.
    - Defining “fake” → Discussion shifts to evidence standards; intent to mislead and localized object edits matter more than generic filters—counterpoint: AI hallucinations still undermine trust.
    - Gamma and dynamic range → Nonlinear curves aren’t just display hacks; they better allocate quantization across tones and match sensor/film response even without screens.

- LLM perspective
    - View: Tutorials like this demystify camera pipelines, making people more comfortable treating “editing” as normal scientific postprocessing, not cheating.
    - Impact: Photographers, journalists, and courts will need standards distinguishing algorithmic enhancement from content alteration, especially as AI tools blend both.
    - Watch next: Open raw-processing pipelines, sensor-level benchmarks, and camera metadata about steps used could anchor debates over authenticity and reproducibility.
