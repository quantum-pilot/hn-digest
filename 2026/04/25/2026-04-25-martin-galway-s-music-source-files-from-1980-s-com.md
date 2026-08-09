# Martin Galway's music source files from 1980's Commodore 64 games

- Score: 157 | [HN](https://news.ycombinator.com/item?id=47900398) | Link: https://github.com/MartinGalway/C64_music

### TL;DR

Commodore 64 composer Martin Galway has published GPL-3.0 assembly sources for the music systems behind Wizball and Game Over, inviting people to study, rebuild, modify, and create new music with attribution. The repository documents Ocean assembler directives and identifies Wizball’s player as his first-generation design, used from 1984 to mid-1987; a later engine began with Athena. HN celebrated the preservation value and childhood memories, while stressing that Galway’s sound lives in precisely timed SID-register changes—not merely melodies that can be transcribed into modern pattern notation.

### Comment pulse

- Wizball reportedly drives interrupts at 200 Hz on PAL and NTSC, exceeding the commonly assumed 50 Hz SID-driver cadence.
- Attempts to port melodies into Strudel were recognizable at best — counterpoint: web players wrapping original SID code preserved authenticity.
- Readers reconstructed obscure Ocean directives, identifying `DSP` as displacement and `DFC` as a PETSCII-producing data definition.

### LLM perspective

- Preservation should include assembler versions, build commands, memory maps, expected binaries, and emulator test fixtures.
- Separate musical data from playback code only if timing, modulation, envelopes, and filter automation remain representable.
- Additional rights-cleared sources could illuminate the transition between Galway’s player generations.
