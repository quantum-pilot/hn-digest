# Agents need control flow, not more prompts

- Score: 292 | [HN](https://news.ycombinator.com/item?id=48051562) | Link: https://bsuh.bearblog.dev/agents-need-control-flow/

- TL;DR  
  The post argues that complex AI agents fail when control logic lives in prompts. Prompt chains are nondeterministic, impossible to reason about, and scale poorly. Instead, LLMs should be treated as components inside deterministic software: explicit state machines, validation checkpoints, and programmatic error detection. Without this, users end up babysitting, auditing, or blindly trusting outputs. HN commenters largely agree, sharing war stories and patterns where code orchestrates tools and LLMs just generate code or translate natural language into constrained actions.

- Comment pulse  
  - Letting models manage multi-step workflows proved flaky; wrapping them in simple deterministic loops fixed reliability, but clashes with vendor platforms pushing autonomous, prompt-driven agents, narratives.  
  - Common pattern: use LLMs to generate deterministic code and validators, then run tasks as pipelines—deterministic flow → LLM decision → deterministic tools, with human review.  
  - Several note this just recreates programming: define objects and methods, let LLM translate language into calls—counterpoint: some report long-running agents working with thoughtful todo-list designs.

- LLM perspective  
  - View: Treat agents as software systems with embedded models; design control flow and safety first, prompts last.  
  - Impact: This favors teams with strong engineering discipline; 'no-code' agent builders will struggle to match reliability-sensitive production use cases.  
  - Watch next: Track frameworks that compile workflows into state machines plus verification hooks, with LLMs as pluggable tools rather than central planners.
