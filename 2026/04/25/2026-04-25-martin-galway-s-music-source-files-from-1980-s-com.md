# Martin Galway's music source files from 1980's Commodore 64 games

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47900398) | Link: https://github.com/MartinGalway/C64_music

## TL;DR
Veteran C64 composer/programmer Martin Galway has released GPL-licensed 6502 assembly source for his classic SID soundtracks, exposing the underlying music drivers he used across the 1980s. The repository is intended for study, modification, and new compositions, and documents the evolution from his first- to second-generation players. Hacker News discussion focuses on how these custom, timing-critical sound engines define the music’s character, the difficulty of mapping them into modern pattern languages or AI workflows, and strong nostalgia around C64-era audio.

## Comment pulse
- Fans still enjoy these tunes via online SID players and videos → some once used C64 monitor cartridges to rip and dissect Galway’s music by hand.

- SID engines are interrupt‑driven trackers → they tweak filters/envelopes/ring‑mod per frame; pattern transcriptions lose timing. — counterpoint: Wizball’s driver reportedly ticks at 200 Hz.

- Experimenters use Claude and GPT as tooling → they fetch .sid files, build players or JS reimplementations, but Strudel/Tidal conversions still sound unlike the originals.

## LLM perspective
- View: Treat these annotated drivers as a benchmark dataset for learning how low‑level synthesis techniques map to perceived musical style.  

- Impact: Emulator authors, tracker developers, and chip‑music composers gain reference implementations clarifying timing, data formats, and hardware‑pushing tricks.  

- Watch next: Toolchains that assemble and play these sources in browsers/DAWs, plus objective audio similarity metrics versus original game soundtracks.
