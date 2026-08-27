# Show HN: Ez FFmpeg – Video editing in plain English

- Score: 326 | [HN](https://news.ycombinator.com/item?id=46400251) | Link: http://npmjs.com/package/ezff

### TL;DR

Ez FFmpeg wraps common video operations in plain-English commands and an interactive prompt, translating conversion, compression, trimming, resizing, merging, and effects into local ffmpeg invocations without AI or APIs. A dry-run reveals the generated command. HN welcomed easier access for infrequent users but identified dangerous simplifications: container changes may trigger unnecessary lossy re-encoding, audio extraction forces MP3, and hidden quality defaults obscure important tradeoffs. The strongest alternative proposed guided command construction that explains choices and favors stream copying.

### Comment pulse

- Occasional users need assistance → ffmpeg’s huge option space makes infrequently used syntax difficult to retain.
- Oversimplification can damage output → hidden re-encoding wastes compute and quality when remuxing or copying streams would suffice.
- Guidance beats opacity → commenters want interactive commands that expose reasoning, quality settings, and safe defaults.

### LLM perspective

- View: The useful abstraction is constrained multimedia intent, provided it teaches rather than conceals consequential decisions.
- Impact: Beginners finish routine edits faster, while experts risk troubleshooting surprising output produced by fixed heuristics.
- Watch next: Add stream-copy detection, codec compatibility checks, quality controls, command explanations, tests, and accessible source hosting.
