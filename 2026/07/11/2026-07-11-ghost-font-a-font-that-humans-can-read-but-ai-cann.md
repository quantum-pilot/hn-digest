# Ghost Font: A font that humans can read but AI cannot

- Score: 190 | [HN](https://news.ycombinator.com/item?id=48870381) | Link: https://www.mixfont.com/ghost-font

### TL;DR

Ghost Font is a browser prototype that encodes readable text in moving dot patterns: individual frames resemble noise, while motion reveals letters to human viewers. It also embeds a static decoy intended to divert models that extract and inspect video frames. Its creator reports frontier systems struggled without technique-specific prompting, but explicitly presents it as an experiment, not encryption, and anticipates video-native models defeating it. HN readers quickly demonstrated that frame differencing, optical flow, and even unprompted agentic analysis can recover messages; several humans found the effect difficult or headache-inducing.

### Comment pulse

- The concealment is brittle → aligning and subtracting adjacent frames exposes motion contours that conventional OCR or an agent can then read.
- Human legibility varies sharply → some viewers read the moving message instantly, while others saw only the decoy, likened it to stereograms, or reported headaches.
- CAPTCHA value is temporary → motion raises attacker effort — counterpoint: reusable video filters turn it into another solvable automation contest.

### LLM perspective

- **View:** This is perceptual obfuscation, not access control; secrecy disappears once the temporal transformation is inferred.
- **Impact:** Useful as a benchmark or art experiment, but unsuitable for confidential communication and potentially inaccessible to many people.
- **Watch next:** Open-source release should enable standardized tests across models, codecs, frame rates, decoys, mobile displays, and human accessibility.
