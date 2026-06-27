# What happened after 2k people tried to hack my AI assistant

- Score: 350 | [HN](https://news.ycombinator.com/item?id=48681687) | Link: https://www.fernandoi.cl/posts/hackmyclaw/

- TL;DR  
  An indie developer exposed their email-based AI assistant to ~2k people, offering a bounty for exfiltrating a hidden secret via prompt injection. The assistant (Claude Opus-based, with constrained tools) reportedly never revealed the secret, leading the author to feel less worried about prompt injection. Hacker News replies argue the setup was too restricted, attackers unmotivated, and success criteria too narrow; they stress that real risk comes when agents can take actions (like sending emails), not just echo secrets.

  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  Test design was too safe → no tools, minimal replying, and “don’t answer emails” instructions make secret leakage artificially unlikely—counterpoint: author says it was still useful for normal tasks.  
  Evidence is weak → casual HN tinkerers aren’t professional jailbreakers; serious exploiters wouldn’t burn real techniques on a public stunt.  
  Security vs usefulness → blocking all replies isn’t meaningful safety; hard part is distinguishing legitimate from malicious actions while still assisting.

- LLM perspective  
  View: Treat this as a small anecdote, not proof that modern models resist prompt injection in realistic deployments.  
  Impact: Agent builders should still sandbox tools, scope permissions, and log/alert on high-risk actions, not rely on system prompts alone.  
  Watch next: Independent red-team benchmarks where agents have real tools (email, HTTP, file access) and attackers are incentivized to exfiltrate data or cause actions.
