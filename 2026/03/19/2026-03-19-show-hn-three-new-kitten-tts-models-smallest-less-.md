# Show HN: Three new Kitten TTS models – smallest less than 25MB

- Score: 295 | [HN](https://news.ycombinator.com/item?id=47441546) | Link: https://github.com/KittenML/KittenTTS

### TL;DR

Kitten TTS v0.8 adds 15M-, 40M-, and 80M-parameter open-source speech models, spanning 25 to 80 MB and running through ONNX on CPUs without a GPU. The developer-preview library produces 24 kHz audio, offers eight voices, adjustable speed, preprocessing, and Linux, macOS, and Windows support. Its roadmap includes mobile, multilingual, custom-voice, ASR, and higher-quality releases. HN testers found output impressive for the size and measured the 80M model at roughly 1.5× real time on an Intel 9700, while flagging pronunciation and packaging problems.

### Comment pulse

- Installing the Python package can pull Torch and multi-gigabyte CUDA dependencies despite CPU-only inference, undermining the tiny-model pitch.
- A tester found numbers nearly unintelligible; maintainers recommended text expansion and promised a model-level fix.
- Readers requested training-data provenance and Japanese support; the latter matters because another multilingual model sometimes mixes Mandarin.

### LLM perspective

- **View:** Compact weights matter less if dependency graphs erase deployment savings.
- **Impact:** Edge applications gain viable offline speech, provided preprocessing and packaging mature.
- **Watch next:** Data disclosure, reproducible quality benchmarks, mobile SDKs, and corrected GPU acceleration.
