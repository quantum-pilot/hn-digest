# I used Claude Code to get a second opinion on my MRI

- Score: 308 | [HN](https://news.ycombinator.com/item?id=48708941) | Link: https://antoine.fi/mri-analysis-using-claude-code-opus

### TL;DR

After a clinic diagnosed a greater-than-50% partial subscapularis tear and began an intervention-heavy plan, the author gave 266 MB of shoulder MRI DICOM files to Claude Code running Opus 4.8. Its report found the tendon intact; a multi-agent comparison favored mild tendinosis with no discrete tear, contradicting the radiologist. The experiment increased doubt rather than resolving it. HN clinicians warned that modality limits, missing clinical context, prompt sensitivity, and confident inconsistency make AI interpretation unsafe. Commenters saw value in explanations and advocacy, but favored an independent radiologist over model arbitration.

### Comment pulse

- Imaging conclusions are modality-bound → ultrasound may miss small calcifications that radiographs or MRI reveal; apparently conflicting reports can both be technically accurate.
- More opinions can increase uncertainty → repeated sessions produce confident contradictions and drift toward suggestions — counterpoint: AI can help patients formulate questions.
- Human expertise is fallible too → commenters recounted serious misdiagnoses, strengthening the case for independent specialist review rather than unquestioned authority.

### LLM perspective

- **View:** An unvalidated model can generate hypotheses and translations, but cannot establish diagnostic truth when specialists and images disagree.
- **Impact:** Patients gain accessible interpretation but also bear new anxiety, anchoring, privacy, and treatment-delay risks.
- **Watch next:** Require blinded radiologist rereads, validated imaging benchmarks, prompt-robustness tests, calibrated uncertainty, DICOM privacy safeguards, and clinician-supervised workflows.
