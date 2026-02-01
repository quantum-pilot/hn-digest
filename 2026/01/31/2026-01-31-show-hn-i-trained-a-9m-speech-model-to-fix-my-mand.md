# Show HN: I trained a 9M speech model to fix my Mandarin tones

- Score: 429 | [HN](https://news.ycombinator.com/item?id=46832074) | Link: https://simedw.com/2026/01/31/ear-pronunication-via-ctc/

### TL;DR
An independent developer built a 9M-parameter Mandarin “ear trainer” that runs entirely in the browser. It uses a Conformer encoder with CTC, pinyin+tone tokens, forced alignment via Viterbi, and a silence-filtering trick to grade each syllable without auto-correcting. Trained on ~300 hours of read speech and heavily quantized, it remains accurate yet tiny. HN testers like the concept but report frequent misrecognitions for natives and conversational speed, dataset bias toward common phrases, and missing tone-sandhi handling, sparking debate about how critical tones really are.

### Comment pulse
- Model often mishears real speech → biases toward common collocations (e.g., zhōngguó), limited syllable set, and read-speech training cause errors for natives and fast speech.  
- Tool best for slow, isolated practice → over-enunciation is rewarded; lacks robust handling of tone sandhi and conversational reduction, so sentences get marked wrong.  
- Tone importance debated → some natives say you can communicate with wrong tones; others argue beginners become unintelligible without them—counterpoint: context helps at higher levels.

### LLM perspective
- View: Elegant use of a tiny Conformer-CTC model plus clever alignment tricks to give immediate, on-device pronunciation feedback.  
- Impact: If improved for conversational and child speech, this could outperform generic ASR APIs for focused Mandarin tutoring.  
- Watch next: add diverse corpora, per-dialect tuning, better sandhi modeling, and calibration for non-native accents and microphones.
