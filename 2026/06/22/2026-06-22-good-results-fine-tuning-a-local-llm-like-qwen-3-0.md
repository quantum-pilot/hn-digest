# Good results fine tuning a local LLM like Qwen 3:0.6B to categorize questions

- Score: 203 | [HN](https://news.ycombinator.com/item?id=48623434) | Link: https://www.teachmecoolstuff.com/viewarticle/fine-tuning-a-local-llm-to-categorize-questions

### TL;DR

A household RAG chatbot uses a fine-tuned Qwen 3 0.6B model to route questions into metadata categories before vector search. Prompting the base model scored 13/131, while Unsloth QLoRA training on roughly 850 examples raised accuracy to 104/131. Replacing semantic category names with opaque two-letter labels reached 120/131, or 91.6%, though water-related categories still confused it. HN commenters argued that classic classifiers, small encoders, or constrained decoding may solve this narrow task more cheaply, while suggesting synthetic hard examples for further gains.

### Comment pulse

- Traditional classifiers fit subject routing → advocates proposed n-gram SGD, logistic regression, embeddings, or BERT-scale encoders with smaller artifacts and faster training.

- A 600M model remains defensible when categories require context → counterpoint: this dataset’s narrow labels may not justify generative-model overhead.

- Invalid labels are a decoding problem, not necessarily a training problem → llama.cpp-style grammars or logit masking can eliminate unsupported outputs.

### LLM perspective

- **View:** The largest gain came from redesigning the output space, showing interface constraints can matter as much as model tuning.

- **Impact:** Metadata-aware RAG can trade a lightweight routing step for smaller retrieval sets, but classifier complexity should match label ambiguity.

- **Watch next:** Compare held-out accuracy, latency, memory, and maintenance across logistic regression, encoders, constrained Qwen, and richer adversarial datasets.
