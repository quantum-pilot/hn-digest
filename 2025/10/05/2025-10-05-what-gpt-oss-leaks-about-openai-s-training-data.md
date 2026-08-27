# What GPT-OSS leaks about OpenAI's training data

- Score: 133 | [HN](https://news.ycombinator.com/item?id=45483924) | Link: https://fi-le.net/oss/

### TL;DR

The author analyzes GPT-oss embedding norms to identify unusual “glitch tokens,” then tests whether several OpenAI models can translate or recognize high-norm Chinese strings. Recognition is presented as evidence that some phrases appeared during training; a correlation between model recognition and GitHub search frequency is offered as weaker evidence about possible sourcing. The method cannot identify the originating document, and commenters challenge the stronger claim that adult websites themselves were training sources rather than phrases that also occur elsewhere, including moderation lists or spam repositories.

### Comment pulse

- Commenters questioned the assumed explanation for low embedding norms, including whether weight decay applied to embeddings.
- The main criticism was that phrase membership does not establish the website or dataset from which it came.

### LLM perspective

- View: Open weights create a useful audit surface, but token behavior supports narrower conclusions than dataset attribution.
- Impact: Glitch-token probes may reveal membership signals or operational weaknesses without reconstructing a training corpus.
- Watch next: Controls for tokenizer construction, initialization, duplication, and alternative phrase sources are essential.
