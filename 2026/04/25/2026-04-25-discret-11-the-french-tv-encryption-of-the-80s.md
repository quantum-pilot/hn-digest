# Discret 11, the French TV encryption of the 80s

- Score: 143 | [HN](https://news.ycombinator.com/item?id=47900478) | Link: https://fabiensanglard.net/discret11/

### TL;DR

Canal+’s Discret 11 scrambled 1980s French SECAM television with inexpensive analog tricks rather than full encryption. An 11-bit LFSR chose whether each visible scanline shifted right by 0, 13, or 26 pixels; black safe-area margins made the lost edge recoverable. Separate sync lines reset six-frame sequences and selected audience levels, while audio used reversible frequency-band swapping without a key. Monthly eight-digit subscriber codes combined with each decoder’s serial number. HN commenters recalled homemade decoders, IRC code sharing, and even learning to interpret the distorted picture and sound.

### Comment pulse

- One childhood project brute-forced a software decoder using a Mac A/V card and CodeWarrior, turning piracy into systems-programming education.
- Some disputed calling 1984–1995 short-lived; eleven years felt substantial during early European terrestrial pay-TV.
- Nostalgia centered on Canal+’s bumper music and Saturday-night broadcasts, whose scrambling viewers sometimes tolerated rather than defeated.

### LLM perspective

- The design shows how analog constraints can substitute transformations for computationally expensive cryptography.
- Per-device code derivation discouraged sharing, but leaked schematics and a small state space undermined secrecy.
- A faithful emulator should model interlacing, safe areas, timing, audio inversion, and monthly code derivation.
