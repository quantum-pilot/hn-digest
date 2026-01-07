# GBC Boot Animation 88×31 Web Button

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46507963) | Link: https://zakhary.dev/blog/gbc-web-button

### TL;DR
A nostalgic web dev wanted a classic 88×31 “web button” using the Game Boy Color boot animation, so they reverse-engineered it from the boot ROM via an emulator. They stepped frame-by-frame using a vblank breakpoint, assembled 175 screenshots into a GIF, then used a carefully chained ImageMagick pipeline to crop, scale, frame, recolor, and finally remap the fade’s blue‑to‑white palette to blue‑to‑grey to avoid ghosting. HN readers loved the deep dive, reminisced about 90s web flair, and suggested simpler capture methods.

---

### Comment pulse
- Retro web buttons are fondly remembered → people recall boycott badges, “Made with Notepad” tags, forum userbars; one commenter even scraped and archived many classic buttons.  
- Detailed obsession with a tiny niche → readers enjoy long-form, process-focused posts about small aesthetic projects and subscribe hoping for more.  
- Capture workflow can be simpler → many emulators export GIF/APNG or support frame stepping; screen recorders plus frame extraction also work — counterpoint: author used debugger out of GBZ80 familiarity.

---

### LLM perspective
- View: This project exemplifies modern “retrocomputing craft”: mixing emulation, CLI tools, and light scripting to produce tiny, highly polished artifacts.  
- Impact: Encourages technically inclined folks to treat visual polish as a playground for learning debuggers, ROM internals, and image-processing pipelines.  
- Watch next: Tooling that automates “capture → palette-fix → web-buttonify” for classic UIs, and clearer norms around fair-use of boot screens in fan art.
