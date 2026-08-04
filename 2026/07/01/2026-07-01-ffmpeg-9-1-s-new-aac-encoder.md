# FFmpeg 9.1's new AAC encoder

- Score: 260 | [HN](https://news.ycombinator.com/item?id=48747116) | Link: https://hydrogenaudio.org/index.php/topic,129691.0.html

### TL;DR

FFmpeg 9.1 receives a ground-up AAC encoder rewrite covering rate control, rate-distortion optimization, and PNS, TNS, intensity-stereo, and mid/side tools. On 3,000 music tracks, its strict-CBR mode reportedly beats FDK-AAC and Apple’s encoder on Zimtohrli and ViSQOL metrics, though speech testing is limited, exact downmix settings matter, and 48 kHz is best tuned. HN noted Opus still scores much better, but AAC remains essential for RTMP streaming and broad device support; replacing FFmpeg’s artifact-prone encoder could therefore improve many default workflows.

### Comment pulse

- Compatibility preserves AAC’s relevance → YouTube, Twitch, OBS, and many clients still assume H.264 video paired with AAC audio.
- Benchmark leadership needs broader validation → Apple TVBR may remain competitive, and speech plus user-supplied artifact samples are under-tested.
- PNS exposed decoder defects → combining synthetic noise with TNS or stereo tools could distort noise and collapse imaging.

### LLM perspective

- **View:** A strong default encoder matters more operationally than the theoretically best codec.
- **Impact:** Streamers and recorders may gain better sound without proprietary Core Audio or FDK installations.
- **Watch next:** Run independent ABX tests across speech, music, sample rates, bitrates, and decoder implementations.
