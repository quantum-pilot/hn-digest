# Jira Is Turing-Complete

- Score: 291 | [HN](https://news.ycombinator.com/item?id=48263253) | Link: https://seriot.ch/computation/jira.html

## TL;DR

By explicitly encoding a two‑counter Minsky machine in Jira’s automation system, the article gives a concrete proof that Jira is Turing‑complete. Issue counts implement registers, workflow status acts as the program counter, and automation rules implement increment/decrement and branching. A simple setup performs addition; a more compact three‑state construction computes Fibonacci numbers, only limited by Jira’s rule‑chaining quotas. Under the standard assumption of unbounded resources, Jira automations are not just script‑like—they are full‑blown programs.

## LLM perspective

- View: Scheduling and workflows in popular tools quietly reach general computability, blurring lines between “configuring software” and “programming.”
- Impact: Teams may unknowingly create arbitrarily complex control flows in Jira, complicating debugging, testing, observability, and change management.
- Watch next: Tool vendors might add analysis, linting, or sandboxing for automations, treating them like code with types, tests, and review.
