# Moebius: 0.2B image inpainting model with 10B-level performance

- Score: 215 | [HN](https://news.ycombinator.com/item?id=48630171) | Link: https://hustvl.github.io/Moebius/

### TL;DR
Moebius is a 226M-parameter diffusion model for image inpainting—filling in missing or removed regions of an image—that aims to match ~10B-parameter systems like FLUX.1-Fill-Dev. It restructures attention into compact “Local-λ Mix Interaction” blocks and uses latent-space distillation from a larger teacher to keep quality while slashing compute, reportedly achieving >15× faster inference with similar benchmark scores on Places2, CelebA-HQ, and FFHQ. HN readers are impressed but skeptical about “10B-level” claims, pointing out quality and resolution limits in real use.

---

### Comment pulse
- Inpainting = removing or filling parts of an image; real-world use hit snags with weird artifacts, strict aspect ratios, and low-resolution training data.  
- Browser and Hugging Face demos exist, including an ONNX-in-browser port; performance ranges from impressive to slow, with CPU spaces taking ~80 seconds per image.  
- Claims of parity with 10B models are questioned: users report smoother inpainted regions, trouble with novel objects, and a hard 512×512 limit — counterpoint: benchmarks still show strong results for its size.

---

### LLM perspective
- View: Distilling big diffusion teachers into small, task-specific students looks like a practical path for consumer hardware and web deployment.  
- Impact: Photo editors, ad-generators, and mobile apps can gain capable inpainting without cloud GPUs or huge downloads.  
- Watch next: Independent side-by-side tests on higher resolutions, complex objects, and varied aspect ratios to validate “10B-level” performance claims.
