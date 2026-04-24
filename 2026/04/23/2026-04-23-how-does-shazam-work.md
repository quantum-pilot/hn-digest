# How does Shazam work?

- Score: 163 | [HN](https://news.ycombinator.com/item?id=47835366) | Link: https://perthirtysix.com/how-the-heck-does-shazam-work

- TL;DR  
  - Shazam converts microphone audio into a spectrogram using the Fast Fourier Transform, then throws away almost everything, keeping only the loudest frequency peaks. It links nearby peaks in time and frequency into compact hashes, which act as fingerprints of that specific recording. An inverted index maps each hash to songs and time offsets; matching is just fast table lookups plus checking that time gaps align. This works well for exact recordings, less so for singing, covers, remixes, or rare/older tracks.

- Comment pulse  
  - Shazam’s core fingerprinting is public and reproducible; value is dataset scale and ops, not the math.  
  - Same fingerprinting powers TV ACR; today it’s adtech, but user-consent versions could aid discovery and metadata.  
  - Basic recording recognition is "easy"; covers, parodies, niche/old tracks need heavier ML (e.g., Audible Magic) and still miss out—counterpoint: engineers couldn’t design it from scratch.

- LLM perspective  
  - Shazam shows how sparse, interpretable features can beat black-box ML when problem is well-posed and data is abundant.  
  - On-device recognition will likely blend classic fingerprints with compact learned embeddings, trading coverage for privacy and always-on, low-power listening.  
  - Expect legal and UX battles around ACR: opt-in discovery tools versus opaque surveillance baked into TVs, speakers, and apps.
