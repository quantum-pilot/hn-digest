# AI Agent Guidelines for CS336 at Stanford

- Score: 300 | [HN](https://news.ycombinator.com/item?id=48359232) | Link: https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md

- TL;DR  
  Stanford’s CS336 ships explicit instructions for LLM coding assistants, framing them as TAs that explain, probe, and debug rather than generate code or solutions. Agents may clarify concepts, interpret errors, and suggest tests, but must not write Python/pseudocode, fill TODOs, or implement core components. HN discussion centers on prompt length and practicality, logging AI usage (.history folders), using tools’ “learning/coaching modes,” assignment design and assessment, and how to integrate such guidelines into real workflows and repos.

- Comment pulse  
  Terse, focused prompts beat long specs → shorter AGENTS.md files stay in context and work better; add tooling like .history folders or scripts to track AI usage.  
  AI as tutor, not crutch → learning/coaching modes that refuse to write code help build intuition—counterpoint: without hard exams, many will still take the shortcut.  
  Pragmatic policy over bans → aligns with industry use of AI; enforcement is fuzzy, but embedding AGENTS.md/CLAUDE.md in course repos makes compliance more automatic.

- LLM perspective  
  View: Clear “TA, not solver” specs plus examples meaningfully shift model behavior, but only if supported by assessment design and tooling.  
  Impact: Students who lean into guided debugging and questioning will learn systems-level ML skills faster than those copy-pasting solutions.  
  Watch next: Courses bundling custom AI harnesses, auto-logging, and graded oral/code reviews to align incentives with genuine understanding.
