# FFmpeg 9.1's new AAC encoder

- Score: 260 | [HN](https://news.ycombinator.com/item?id=48747116) | Link: https://hydrogenaudio.org/index.php/topic,129691.0.html

### TL;DR
FFmpeg 9.1 ships a new built‑in AAC encoder that massively improves on FFmpeg’s old, artifact‑prone one and approaches or surpasses Apple’s CoreAudio at comparable constant bitrates. This matters because AAC remains the default in RTMP live streaming (YouTube, Twitch, OBS), where Opus isn’t widely supported despite clearly superior quality, especially at low bitrates. Discussion also highlights a long‑hidden AAC decoder bug around perceptual noise substitution, heavy reliance on 48 kHz tuning, and the mix of human listening and objective metrics in codec design.  
*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Opus clearly outperforms AAC in these tests, especially at 64 kbps → but AAC dominates streaming/device support, and Opus’s spec/licensing quirks hinder use in games and appliances. — counterpoint: “works pretty much anywhere” for many users.  

- New FFmpeg AAC fixes old chirping/low‑quality output → may now rival CoreAudio CBR, reducing need for Apple/FDK/qaac workarounds; lack of robust VBR still keeps CoreAudio attractive to some.  

- Codec tuning exposed a long‑standing PNS bug and AAC’s sample‑rate‑dependent windows → encoder is optimized for 48 kHz, aligning with pro standards, video sync, OS/DAC defaults, and Opus’s 48 kHz‑centric design.

### LLM perspective
- View: This release makes “default FFmpeg AAC” finally a safe, high‑quality choice for most practical streaming and recording setups.  

- Impact: Broad FFmpeg/OBS ecosystems benefit; fewer users need proprietary encoders or codec research just to get decent AAC audio.  

- Watch next: Add strong VBR modes, expand listening tests versus Opus/CoreAudio, and propagate PNS‑related decoder fixes across players and libraries.
