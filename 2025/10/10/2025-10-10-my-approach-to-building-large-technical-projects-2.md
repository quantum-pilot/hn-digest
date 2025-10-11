# My approach to building large technical projects (2023)

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45535202) | Link: https://mitchellh.com/writing/building-large-technical-projects

- TL;DR
  - Mitchell Hashimoto outlines a method for large technical projects: decompose into small, testable pieces that yield visible progress; sprint to frequent demos; choose “good enough” implementations; adopt your own product early to guide priorities; iterate later. He warns experience can tempt perfectionism; throwaway demos/CLIs keep motivation and reveal product flaws sooner. HN discussion echoes the value of tight feedback loops (REPLs, tests), links the approach to Extreme Programming, and debates what to “skip” first—structure vs algorithms/performance—plus constraints and LLMs as accelerators.

- Comment pulse
  - Quick feedback loops → faster motivation and fewer bugs; REPLs and e2e tests keep changes visible. — counterpoint: slow setup kills momentum and projects.
  - Avoid perfectionism/second‑system → constraints (hackathons, pico‑8) and “shitty code” unblock progress; LLM tools accelerate scaffolding.
  - XP alignment → solo Extreme Programming: iterate small, test, demo often; demos become living specs and regression checks.

- LLM perspective
  - View: Prioritize tasks by shortest path to a runnable demo or test; accept throwaways to maintain momentum.
  - Impact: Teams shift to demo milestones and feedback-loop SLAs; reduced overengineering; higher personal project completion.
  - Watch next: Measure “time-to-first-demo” and “demo cadence”; invest in REPLs, hot reload, e2e snapshots, and demo CI.
