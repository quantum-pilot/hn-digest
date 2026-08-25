# Booting from a vinyl record (2020)

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46730885) | Link: https://boginjr.com/it/sw/dev/vinyl-boot/

### TL;DR

A custom option ROM lets an IBM 5150 load a 64K read-only RAM disk from audio cut onto a 10-inch record. The stock cassette interface and BIOS demodulation routines decode the signal, then boot a trimmed FreeDOS kernel, tiny command shell, and patched file-transfer utility. Playback needed amplifier equalization and a clean groove; pops or dropouts break the stream, although small speed variation works. Commenters connected the experiment to flexidisc software, radio-broadcast programs, cassette computers, and the tangible unreliability of older storage.

### Comment pulse

- Analog media can carry executable data → cassette protocols treat any sufficiently clean audio source as a stream of bits.
- Distribution once used ordinary audio channels → commenters recalled software on flexidiscs, broadcast radio, cassettes, and even VHS.
- Physical storage exposed its failure modes → users could hear degradation, but worn discs and bad floppies repeatedly destroyed loads.

### LLM perspective

- View: A modem protocol cares about signal integrity, not whether audio comes from tape or grooves.
- Impact: Retrocomputing enthusiasts gain a reproducible bridge between physical music media, firmware, and DOS.
- Watch next: Error correction, alternate sound inputs, additional cassette-capable machines, pressing durability, and higher-capacity encodings.
