# How does Shazam work?

- Score: 163 | [HN](https://news.ycombinator.com/item?id=47835366) | Link: https://perthirtysix.com/how-the-heck-does-shazam-work

### TL;DR

Shazam converts a short recording into a spectrogram by applying FFTs to waveform slices, then discards most data and keeps prominent frequency-time peaks. It pairs nearby peaks into hashes containing two frequencies and their time gap. Those hashes address an inverted index of song fingerprints; a candidate wins when many matches share the same temporal offset. The sparse representation survives background noise and searches quickly, but identifies exact recordings rather than melodies, so humming, covers, or uncatalogued music can fail. Readers admired the transparent algorithm while emphasizing database coverage.

### Comment pulse

- Commenters distinguished elegant matching code from the harder commercial asset: assembling, refreshing, and geographically curating the reference catalog.
- Similar fingerprinting powers television content recognition, where user intent and consent may determine whether the feature feels useful or invasive.
- Recognizing different performances is materially harder because pitch, instrumentation, and timing change, requiring more sophisticated approaches.

### LLM perspective

- Publish confidence and catalog provenance so users can distinguish weak matches from absent reference audio.
- Privacy-friendly television recognition should be opt-in, local where possible, and expose immediate consumer value.
- Evaluate separately on noise, speed variation, covers, live performances, regional catalogs, and newly released tracks.
