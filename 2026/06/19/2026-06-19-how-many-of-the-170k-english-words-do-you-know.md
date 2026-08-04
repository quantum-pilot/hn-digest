# How many of the 170k English words do you know?

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48598586) | Link: https://vocabowl-870366514258.us-west1.run.app/

### TL;DR

VocabOwl promises a scientifically stratified 100-question multiple-choice estimate of how many of 171,476 English words a user knows, using five difficulty bands and Gemini 3 Flash. HN testers found the result more playful than scientific: the published bands total only about 85,000 words, so even perfect answers yield roughly half the advertised vocabulary. Critiques centered on whether the sampling, question construction, scoring, and interaction design can support any defensible estimate.

### Comment pulse

- Multiple choice inflates apparent knowledge → absurd distractors and answer-length cues reward guessing — counterpoint: chance-corrected forced choices can reveal partial morphological knowledge.
- Sampling appears semantically biased → later questions overrepresent verbosity, speech, and long-word concepts, possibly reflecting task-primed AI generation rather than English usage.
- A faster adaptive test would retain users → early answers should move difficulty aggressively, then converge as confidence rises; single-click answers need undo.

### LLM perspective

- **View:** A vocabulary test needs calibrated item-response modeling, not difficulty labels plus linear extrapolation from a small hand-shaped sample.
- **Impact:** Misleading scores may entertain, but they cannot support comparisons across native speakers, learners, domains, or educational backgrounds.
- **Watch next:** Publish the word source, frequency strata, item-generation method, validation cohort, confidence intervals, chance correction, and retest reliability.
