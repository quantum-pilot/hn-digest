# Ollama Web Search

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45377641) | Link: https://ollama.com/blog/web-search

### TL;DR

Ollama launched authenticated web-search and page-fetch APIs, exposed through REST, Python, JavaScript, and an MCP server. A free individual tier supports grounding local or hosted models with current information; higher limits require Ollama Cloud. Its sample agent pairs search and fetch with Qwen 3 4B and recommends roughly 32,000 tokens of context. Commenters focused less on mechanics than on undisclosed search providers, privacy and reuse terms, uneven result quality, and tension between Ollama’s local-model identity and growing cloud business.

### Comment pulse

- Provider opacity → an Ollama representative claimed zero retention and user ownership, but commenters wanted formal privacy and licensing documentation.
- Cloud expansion → some call it mission drift; others value inexpensive access to models too large for consumer hardware.

### LLM perspective

- View: Search makes Ollama a broader agent platform, while outsourced retrieval introduces trust dependencies local inference cannot remove.
- Impact: Developers gain simpler grounding, but must evaluate provider coverage, retention, and result rights before production use.
- Watch next: Published privacy terms, named upstream providers, reproducible quality tests, and free-tier rate limits.
