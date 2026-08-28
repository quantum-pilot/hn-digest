# An LLM is a lossy encyclopedia

- Score: 512 | [HN](https://news.ycombinator.com/item?id=45062046) | Link: https://simonwillison.net/2025/Aug/29/lossy-encyclopedia/

### TL;DR

Simon Willison compares an LLM’s weights to a lossy encyclopedia: they preserve broad patterns while dropping exact details, so users should supply authoritative examples when precision matters. A model may help adapt correct device boilerplate once given, but should not be trusted to reconstruct it from weights alone. Commenters liked the intuition yet warned that users need domain knowledge to detect losses, while confident fabrication, nondeterminism, and absent sourcing make the analogy too gentle—especially for high-stakes questions.

### Comment pulse

- Treat models as processors over supplied evidence → exact source material reduces dependence on imperfect memorization.
- The analogy understates risk → plausible inventions and missing provenance differ from ordinary compression errors.

### LLM perspective

- View: The useful boundary is evidence transformation, not treating model weights as an authoritative knowledge store.
- Impact: Novices face the highest verification burden because they least recognize which details cannot survive compression.
- Watch next: Interfaces should surface provenance, uncertainty, and retrieved evidence before users act on precise claims.
