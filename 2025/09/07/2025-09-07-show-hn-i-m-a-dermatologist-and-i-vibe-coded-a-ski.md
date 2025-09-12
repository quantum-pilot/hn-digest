# Show HN: I'm a dermatologist and I vibe coded a skin cancer learning app

- Score: 426 | [HN](https://news.ycombinator.com/item?id=45157020) | Link: https://molecheck.info/

- TL;DR
  - A dermatologist used AI “vibe coding” to ship a mobile app that trains laypeople to spot concerning skin lesions via quick binary quizzes and feedback. HN praises lower barriers for domain experts, but debates case prevalence (balanced sets vs real-world low base rates) and warns about user miscalibration. The author clarifies it’s for education, not diagnosis, and plans better balancing and instruction. Commenters also note potential score inflation from class imbalance and the broader challenge of handling false positives/negatives outside an educational setting.

- Comment pulse
  - AI lowers build costs/time for clinicians → domain ideas ship without dev teams; term “vibe code” grates — counterpoint: image classification is largely commoditized.
  - Case mix matters → 50:50 aids recognition; real prevalence is ~1% malignant; staged curricula may improve learning and avoid base-rate gaming.
  - Add explainability and calibration → teach ABCDE, show why images are malignant/benign; fix broken guide link; avoid overconfidence from inflated scores.

- LLM perspective
  - View: Treat as a spaced-repetition trainer with prevalence-aware scoring, progressive difficulty, and immediate feedback; never position as a diagnostic tool.
  - Impact: Lets clinicians prototype education tools; could upskill self-screening but also spike unnecessary referrals if thresholds and messaging are off.
  - Watch next: Publish dataset sources, base-rate confusion matrices, and retention studies; add ABCDE tips, saliency overlays, and fix the how-to link.
