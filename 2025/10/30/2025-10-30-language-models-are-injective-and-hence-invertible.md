# Language models are injective and hence invertible

- Score: 212 | [HN](https://news.ycombinator.com/item?id=45758093) | Link: https://arxiv.org/abs/2510.15511

### TL;DR

An arXiv paper claims transformer language models map discrete input sequences injectively to continuous hidden representations, preserving distinct inputs through initialization and training despite locally non-injective components. The authors report billions of collision tests across six models and introduce SipIt, an algorithm said to reconstruct exact input tokens from hidden activations in linear time. Crucially, this does not invert generated output text or recover training data. Commenters questioned whether high-dimensional collision testing adds meaningful evidence and highlighted privacy risks when hidden states are stored or shared.

### Comment pulse

- Critics argued billions of tests are weak evidence in enormous continuous spaces under a very small collision threshold.
- Clarifications distinguished reversible hidden representations from final token outputs, which routinely map multiple prompts to similar or identical text.

### LLM perspective

- View: The practical result concerns exposure of internal activations, not magical reversal of ordinary chatbot responses.
- Impact: Systems exporting or retaining hidden states may preserve more sensitive prompt detail than operators assume.
- Watch next: Seek peer review, proof-condition scrutiny, quantization tests, architecture coverage, and defenses preserving downstream utility.
