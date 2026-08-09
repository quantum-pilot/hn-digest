# SPEAKE(a)R: Turn Speakers to Microphones for Fun and Profit [pdf] (2017)

- Score: 154 | [HN](https://news.ycombinator.com/item?id=47822805) | Link: https://www.usenix.org/system/files/conference/woot17/woot17-paper-guri.pdf

### TL;DR

Researchers demonstrate SPEAKE(a)R, malware that covertly converts connected headphones or earbuds into microphones by using software-controlled audio-jack retasking. Because dynamic speakers and microphones are physically reversible, a compromised PC can record even when its normal microphone is absent, muted, disabled, or taped. Tests found intelligible speech could be captured from nine meters away, though quality was below a proper microphone. The attack mainly affects passive transducers and retaskable audio codecs; proposed defenses include blocking output-to-input remapping, alerting on access, disabling audio hardware, or using one-way amplified devices.

### Comment pulse

- Musicians recognized the same principle in improvised vocal recording and “subkick” drum microphones.
- Several readers recalled recording through ordinary headphones with tape machines, computers, or alternate iPod firmware.
- One childhood anecdote described producing an entire album with discarded equipment and broken headphones.

### LLM perspective

- A nominally disabled sensor can remain available through adjacent hardware capabilities.
- Sensitive-room policies should treat passive headphones as potential recording devices.
- Strong controls must mediate signal direction below the application-permission layer.
