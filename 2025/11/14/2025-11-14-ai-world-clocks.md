# AI World Clocks

- Score: 560 | [HN](https://news.ycombinator.com/item?id=45930151) | Link: https://clocks.brianmoore.com/

### TL;DR

AI World Clocks asks nine models, once per minute and within 2,000 output tokens, to generate responsive HTML and CSS for an analog clock showing a specified time. The sparse source provides no benchmark or correctness data; the value lies in watching varied successes and failures. The creator says Kimi tends to be accurate but repetitive while Qwen is stranger and funnier. Commenters debated honesty, prompt bias, nondeterminism, and whether broken clocks expose limitations or produce unexpectedly useful design ideas.

### Comment pulse

- Accuracy and creativity diverged → consistent Kimi outputs looked competent, while erratic Qwen results supplied novelty and humor.
- A fixed prompt is not necessarily neutral → wording may favor models trained on similar clock-generation patterns.
- Failures can inspire → malformed layouts sometimes suggested designs that a correctness-only benchmark would discard.

### LLM perspective

- View: The project is a compact visualization of variance, trade-offs, and prompt sensitivity rather than a model ranking.
- Impact: Designers can inspect generated artifacts where aesthetic surprise and functional correctness visibly compete.
- Watch next: Publish source outputs, parsed time accuracy, failure rates, seeds, and user preference comparisons.
