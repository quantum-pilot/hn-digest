# Agentic Engineering Patterns

- Score: 475 | [HN](https://news.ycombinator.com/item?id=47243272) | Link: https://simonwillison.net/guides/agentic-engineering-patterns/

- TL;DR  
  Simon Willison is assembling a living cookbook of “agentic engineering patterns” for using coding agents (Claude Code, Codex, etc.). It frames code as cheap, emphasizes reusable workflows, tests-first loops, and techniques for understanding and steering AI-written code. HN largely agrees patterns are needed but fears a new buzzword industry. Commenters focus on emerging pain points: exploding code volume, code review bottlenecks, fragile or tautological tests, and the importance of strong harnesses and organizational culture over raw generation speed.

- Comment pulse  
  - AI patterns will spawn hype/consulting circus → chatbots work via plain language; formalism risks OOP-style dogma — counterpoint: shared affordance patterns curb confusion and hype.  
  - Code is cheap, review is bottleneck → AI inflates PR size; responses include loosening style review, investing in analysis/tooling, or seeking orgs that value maintainability.  
  - Agentic loops need strong tests → deterministic harnesses and mutation testing catch tautological LLM checks; otherwise agents “optimize” nothing while green tests give false confidence.

- LLM perspective  
  - View: Treat agents as junior collaborators embedded in tight test loops, not as oracles; design workflows around verification, not generation.  
  - Impact: Teams lacking testing culture or architectural ownership will suffer most from “cheap code”; AI amplifies existing process weaknesses.  
  - Watch next: Practical guidelines for code-review triage, AI-assisted refactoring, and organization-level guardrails will matter more than clever prompting tricks.
