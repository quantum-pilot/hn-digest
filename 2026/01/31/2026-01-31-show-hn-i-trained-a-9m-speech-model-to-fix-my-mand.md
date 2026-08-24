# Show HN: I trained a 9M speech model to fix my Mandarin tones

- Score: 429 | [HN](https://news.ycombinator.com/item?id=46832074) | Link: https://simedw.com/2026/01/31/ear-pronunication-via-ctc/

### TL;DR

Simon Edwardsson trained a 9-million-parameter Mandarin pronunciation grader on roughly 300 hours of AISHELL-1 and Primewords speech. A Conformer with CTC predicts 1,254 Pinyin-plus-tone tokens, then Viterbi alignment scores each expected syllable; filtering high-blank silence fixed a severe confidence bug. INT8 quantization reduced the browser model to about 11MB, while reported validation tone accuracy remained 98.29%. Testers liked the interface but found strong read-speech bias: native and intermediate speakers needed exaggerated, slow delivery, while conversational speech, sandhi and children’s voices exposed gaps, and likely-token substitutions obscured actual pronunciation.

### Comment pulse

- Users reported frequent errors at normal speed, including shifted syllable alignment and wrong tones that disappeared only with deliberate over-enunciation.
- A constrained syllable vocabulary can choose the likeliest legal token rather than describe malformed sounds or separate acoustic errors from sequence bias.
- Tones’ importance split speakers — counterpoint: context and regional accents help comprehension, but learners also make grammar and pronunciation errors.

### LLM perspective

- View: Small acoustic models can grade rehearsed speech well, but benchmark accuracy does not guarantee pedagogical validity.
- Impact: Learners gain private on-device feedback, while false corrections may reinforce unnatural pacing or undermine confidence.
- Watch next: Conversational and child speech data, native-speaker acceptance rates, sandhi tests and open-set phoneme error detection.
