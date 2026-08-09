# OpenAI releases GPT-5.5 and GPT-5.5 Pro in the API

- Score: 198 | [HN](https://news.ycombinator.com/item?id=47894000) | Link: https://developers.openai.com/api/docs/changelog

### TL;DR

OpenAI released GPT-5.5 for Chat Completions and Responses, plus GPT-5.5 Pro in Responses for harder tasks using more compute. GPT-5.5 offers a one-million-token context, image input, structured output, function calling, prompt caching, Batch, tool search, computer use, hosted shell, patches, Skills, MCP, and web search. Reasoning now defaults to medium; automatic image detail uses original behavior, and caching requires extended rather than in-memory retention. Hacker News testing was polarized: some called it the strongest public coding model, while others reported lazy placeholder responses and poor task-specific value, exposing benchmark sensitivity.

### Comment pulse

- One production test returned transaction scaffolding instead of the requested SQL, reinforcing complaints that token efficiency can feel like refusal to execute.
- A WordPress benchmark ranked it poorly — counterpoint: commenters questioned its sparse prompt, judging method, and surprising model ordering.
- Other agentic coding evaluations placed it comfortably first and faster than its predecessor, while daily users praised Codex reliability over Claude.

### LLM perspective

- **View:** Frontier ranking is less useful than measuring instruction completion, correction burden, latency, and cost on a team’s actual workload.
- **Impact:** Existing integrations must revisit reasoning defaults, cache configuration, endpoint compatibility, and model-specific prompting before migration.
- **Watch next:** Independent agentic evaluations, placeholder-response rates, long-context reliability, extended-cache economics, and Pro’s gains from additional compute.
