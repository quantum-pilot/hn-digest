# FUTO Swipe – A new swipe typing model

- Score: 209 | [HN](https://news.ycombinator.com/item?id=48648619) | Link: https://swipe.futo.tech/

### TL;DR

FUTO Swipe combines three models: a universal layout- and language-agnostic encoder, a tiny per-language context model trained only on text, and a layout- plus language-specific decoder trained on swipe traces. With all three, QWERTY English, and beam width 300, its test-set top-four failure rate is about 4%, falling below 1% when excluding unknown words. HN users said the update approaches Gboard while preserving privacy, but reported capitalization, punctuation, and contextual-suggestion gaps. Discussion also highlighted ClearFlow, a swipe-optimized layout selected from roughly 800,000 synthetic evaluations.

### Comment pulse

- QWERTY creates ambiguous gesture paths → ClearFlow reduces colinear and obtuse trigrams; temporal cues detect intended letters without interrupting flow.
- Real-world quality is close, not equal, to Gboard → users praised swiping but found random capitalization, weak context, and apostrophe errors.
- Licensing is fragmented → the swipe library uses GPLv3, while the Android app and model use separate FUTO-written terms.

### LLM perspective

- **View:** Separating universal geometry, linguistic context, and layout specialization makes new languages cheaper while preserving a path to peak accuracy.
- **Impact:** Privacy-focused keyboards can compete without cloud inference, though each language-layout pair still needs swipe data for the best decoder.
- **Watch next:** Publish top-one accuracy, latency and memory by device, multilingual decoders, OOV handling, ClearFlow learning curves, and context-model ablations.
