# How many of the 170k English words do you know?

- Score: 211 | [HN](https://news.ycombinator.com/item?id=48598586) | Link: https://vocabowl-870366514258.us-west1.run.app/

### TL;DR
A site called VocabOwl offers a 100-question, multiple-choice quiz that claims to “scientifically” estimate how many of ~171k English words you know using stratified sampling across difficulty bands. Hacker News users enjoyed the idea but found the execution weak: difficulty bands feel arbitrary, definitions are often sloppy, the UI is tedious, the test is easy to game, and the math behind the final estimate is plainly wrong (their bands only sum to 85k words). Many suspect heavy, unrefined AI involvement.

---

### Comment pulse
- UX is slow and boring → 100 questions, many easy ones up front, too many clicks, no adaptivity, so people quit before reaching harder words.  
- “Science” and math don’t hold up → difficulty tiers feel misclassified, band sizes total 85k not 171k, estimates overconfident yet structurally capped.  
- Multiple-choice design is exploitable → obvious distractors, “longest answer wins,” no “I don’t know,” so guessing and testwiseness inflate vocabulary scores.

---

### LLM perspective
- View: Vocabulary tests must separate recognition, educated guessing, and true command; this quiz mostly measures pattern-spotting in weak item design.  
- Impact: Casual users may overestimate vocabulary size; serious learners or educators should avoid treating these scores as diagnostic.  
- Watch next: Better tools would publish item banks, validation data, and adaptivity logic, and invite psychometric review rather than vague “AI + science” claims.
