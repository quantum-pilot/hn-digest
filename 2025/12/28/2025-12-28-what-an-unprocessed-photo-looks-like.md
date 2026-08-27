# What an unprocessed photo looks like

- Score: 153 | [HN](https://news.ycombinator.com/item?id=46415225) | Link: https://maurycyz.com/misc/raw_photo/

### TL;DR

A camera’s sensor records linear intensity samples, not a finished color image. The author reconstructs a Christmas-tree photo by mapping black and white levels, interpreting its Bayer filter, demosaicing neighboring pixels, applying a nonlinear brightness curve, and correcting the sensor’s green bias through white balance. Even the in-camera JPEG is therefore a mathematical rendition, not an untouched ground truth. HN discussion connected Bayer’s extra green samples to luminance resolution, debated processing versus AI hallucination, and argued that deception depends more on intent than ordinary global adjustments.

### Comment pulse

- Green carries detail efficiently → human vision prioritizes luminance, supporting RGGB sampling and lower-resolution chroma reconstruction.
- Every photo is interpreted → sensor conversion necessarily embeds choices before any user opens an editor.
- Generative reconstruction crosses a disputed boundary → object-aware hallucination raises evidentiary risks beyond demosaicing or tone curves.

### LLM perspective

- View: “Unedited” usefully describes workflow, but cannot mean unprocessed or uniquely faithful to physical reality.
- Impact: Photographers, viewers, and courts need provenance language distinguishing global development from localized or generative alteration.
- Watch next: Camera metadata, content credentials, and forensic standards should document increasingly semantic image pipelines.
