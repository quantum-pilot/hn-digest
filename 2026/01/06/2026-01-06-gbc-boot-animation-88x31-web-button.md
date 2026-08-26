# GBC Boot Animation 88×31 Web Button

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46507963) | Link: https://zakhary.dev/blog/gbc-web-button

### TL;DR

To create a retro 88×31 button, Zak captured the Game Boy Color boot animation by breaking on each vertical blank in SameBoy and saving 175 framebuffer screenshots. ImageMagick then assembled, cropped, resized, centered, and framed the GIF. Replacing white with period-appropriate gray introduced ghosting because the logo faded through blue-to-white transition colors, so he extracted their histogram, interpolated a blue-to-gray palette, and remapped each shade before compositing. Commenters enjoyed the nostalgic deep dive but suggested emulator capture, frame stepping, or lossless recording could simplify extraction.

### Comment pulse

- Readers welcomed web buttons as compact identity, advocacy, and handmade-site signals, recalling Notepad badges and forum userbars.
- Emulator users said native animation export, manual frame stepping, or lossless screen recording could avoid 175 debugger-driven screenshots.
- The author agreed capture was overcomplicated but valued the exercise because existing GBZ80 familiarity made the reverse-engineering path approachable.

### LLM perspective

- View: The project’s charm comes from solving a tiny aesthetic problem with unusually transparent technical archaeology.
- Impact: Reproducible command-line image pipelines let personal-web creators remix archival media without advanced drawing skills.
- Watch next: Automating frame extraction and palette substitution could preserve exact timing while shortening the workflow substantially.
