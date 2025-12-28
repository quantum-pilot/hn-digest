# Show HN: Ez FFmpeg – Video editing in plain English

- Score: 326 | [HN](https://news.ycombinator.com/item?id=46400251) | Link: http://npmjs.com/package/ezff

- TL;DR  
ezff is a tiny Node.js CLI that turns plain-English commands like `ff convert video.mp4 to gif` into concrete ffmpeg invocations. It supports interactive prompts, dry runs, and common operations (convert, trim, compress, resize, merge, etc.), all offline with simple pattern-matching—not AI. HN likes the idea for infrequent users but criticizes oversimplified defaults: automatic re-encoding where remuxing is better, hidden quality settings, and naive GIF conversion. Discussion broadens into better ffmpeg frontends, natural-language CLIs, and using LLMs as “ffmpeg tutors.”

- Comment pulse  
ffmpeg is complex for a reason → wrappers that always re-encode, hide codecs/quality, and conflate remuxing risk wasting CPU and degrading output—counterpoint: casual users genuinely struggle with raw ffmpeg.  

Improve the abstraction, don’t abandon it → smart remux-vs-reencode logic, adjustable quality, and palettegen-style GIF defaults or gifski-like tooling would fix many complaints.  

Natural-language frontends are attractive → people imagine a whole OS CLI in plain English or use LLMs to draft commands, but ambiguity and hidden side effects worry power users.

- LLM perspective  
View: A curated, deterministic wrapper is valuable, but must make lossy operations and “expensive” choices visible and overridable.  

Impact: Helps occasional video editors more than experts; could become a standard “ffmpeg porcelain” if it gains safer defaults.  

Watch next: Add remux-first behavior, quality/codec flags, docs that explain generated commands, and compare UX against LLM-based ffmpeg helpers.
