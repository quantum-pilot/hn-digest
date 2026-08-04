# All of human cooking compressed into 2 megabytes

- Score: 350 | [HN](https://news.ycombinator.com/item?id=48291225) | Link: https://arxiv.org/abs/2605.22391

### TL;DR

Epicure trains three compact ingredient embeddings from 4.14 million multilingual recipes, normalizing raw names into 1,790 ingredients and combining recipe co-occurrence with FlavorDB chemical-compound links. Cooc, Chem, and Core variants represent different positions between culinary context and chemistry, supporting similarity and pairing exploration rather than storing recipes. HN’s consensus was that the headline overclaims: the work omits technique, proportions, and much global cuisine, with English and Chinese dominating. Commenters still saw value in flavor discovery, while demo testing exposed vocabulary, localization, and generation failures.

### Comment pulse

- This models ingredients, not cooking → embeddings capture pairings but omit preparation order, temperature, ratios, texture, and technique that determine whether recipes succeed.
- Coverage is uneven → English and Chinese supply roughly 90% while Africa and Arab cuisines are absent — counterpoint: included languages reach large populations.
- An older demo showed promise and brittleness → it inferred rice preparation and lamb cuts, yet missed common terms, localization distinctions, and salad combinations.

### LLM perspective

- **View:** The artifact is a coordinate system for ingredients; its compression ratio says little about culinary completeness or recipe quality.
- **Impact:** Chefs and recommenders gain a pairing prior, while recipe generation still needs structured steps, quantities, sensory goals, and validation.
- **Watch next:** Evaluate geographic balance, translation errors, synonym granularity, pairing prediction, chef judgments, and whether procedural data improves generated recipes.
