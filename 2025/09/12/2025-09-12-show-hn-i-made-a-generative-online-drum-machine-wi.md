# Show HN: I made a generative online drum machine with ClojureScript

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45220069) | Link: https://dopeloop.ai/beat-maker/

TL;DR
An online, ClojureScript-based generative drum machine uses a declarative audio graph over the Web Audio API, letting users generate waveforms and patterns. HN feedback: improve timing under UI load; refine UX by relocating the play control, lightly shading every fourth step, adding configurable grid/colors and sample import; and swap new samples silently while playing to avoid off-grid hits. Desktop experience is smooth; mobile needs work. Some curiosity about the long-term choice of ClojureScript.
Content unavailable; summarizing from title/comments.

Comment pulse
- Use AudioWorklet for timing → Web Audio API scheduling can jitter under heavy UI; generative drums need sample-accurate processing — counterpoint: declarative virtual-audio-graph simplifies graph management.
- Improve grid UX → Move/duplicate play button near editor; lightly shade every 4th column; add configurable grid/colors and import-your-own samples.
- Replace sounds silently mid-play → Avoids off-grid hits when regenerating drum samples; current behavior distracts during composition.

LLM perspective
- View: Decouple UI from DSP; implement transactional sample swaps so regeneration never alters currently scheduled audio.
- Impact: If polished, it bridges browser toys and DAW-ready tools; ClojureScript proves viable for interactive audio UIs.
- Watch next: Latency/jitter benchmarks, AudioWorklet migration plan, mobile-first redesign, and config/export for grids, colors, and user samples.
