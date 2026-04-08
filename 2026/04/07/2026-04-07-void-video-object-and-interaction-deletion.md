# VOID: Video Object and Interaction Deletion

- Score: 180 | [HN](https://news.ycombinator.com/item?id=47627998) | Link: https://github.com/Netflix/void-model

### TL;DR
Netflix’s VOID is an open-source video inpainting system that can remove objects *and* the physical interactions they cause (e.g., a removed person no longer supporting a guitar, which then falls). It builds on CogVideoX with a quadmask representation (object, overlap, affected region, background), auto-generated via SAM2 + a Gemini-based VLM, plus optional manual refinement. A two-pass diffusion pipeline improves temporal consistency. HN discussion alternates between enthusiasm, questions about physical accuracy and artistic control, and concern over deepfake/censorship misuse.

---

### Comment pulse
- Creative potential → Enables re-editing or “choose your own adventure” style narratives by deleting characters or props from entire films.  
- Imperfect physics → Some examples update secondary motion (kettlebell/pillow) but fail on others (spinning tops), raising worries about opaque, language-driven control.  
- Tool vs misuse → VFX folks see a standard cinema tool; others fear easier deepfakes and censorship, arguing benefits to amateurs may not offset societal risks.

---

### LLM perspective
- View: Treat this as “Photoshop for video causality,” but expect edge-case failures where physics or intent are underspecified.  
- Impact: Lowers the bar for sophisticated VFX; simultaneously raises verification and authenticity challenges for news, evidence, and politics.  
- Watch next: Stronger control interfaces, provenance/watermarking standards, benchmark suites for interaction realism, and policy responses to synthetic video editing.
