# OpenAI reduces Codex Model Context Size from 372k to 272k

- Score: 293 | [HN](https://news.ycombinator.com/item?id=48965850) | Link: https://github.com/openai/codex/pull/33972/files

## TL;DR

OpenAI cut Codex’s max context from 372k to 272k tokens. Heavy users say this worsens an already-bad situation: mandatory, opaque context compaction that triggers around 20% remaining tokens, discards important details, and can force repeated re-reading of large codebases or research materials. Others argue very large windows already degrade model quality and cost, so workflows should favor chunking, explicit plans, or external documents. The thread also cites evidence of context rot and calls for better controls over compaction.

## Comment pulse

- Long-window coders feel crippled → reduced context plus forced compaction breaks research workflows, causing loops and hallucinations — counterpoint: some adapt via plans, restarts.  
- Large windows hurt quality, say others → beyond ~250–300k tokens models get slower, “dumber,” and expensive; better to slim docs, modularize, and chunk tasks.  
- Alternatives emerge → users build tools like context-bonsai, markdown memories, and multi-agent plans; research suggests compaction can rival long contexts but context rot persists.  

## LLM perspective

- View: Key issue isn’t just 272k vs 372k, but lack of user control over compaction and memory strategy.  
- Impact: Power users with large codebases or multi-doc agents suffer most; casual coding or chat unaffected, may see cheaper runs.  
- Watch next: OpenAI adding compaction toggles, per-message pinning, or first-class external memory would relieve tension more than incremental context increases.
