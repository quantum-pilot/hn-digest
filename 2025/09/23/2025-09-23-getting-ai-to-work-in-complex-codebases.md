# Getting AI to work in complex codebases

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45347532) | Link: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md

- TL;DR
    - The piece proposes a pipeline to make coding agents effective in large codebases: curate context, ask clarifying questions, draft specs/plans, generate changes, run a critic, and iterate. HN experiences echo this: plan-first workflows create markdown designs, then agents execute while developers verify via tests. Human oversight is crucial—critics hallucinate issues and agents struggle to judge “working.” Simplified, well-documented architectures help. Despite steering overhead and tool limits (e.g., weak sub-agent support), overall throughput and developer satisfaction improve.

- Comment pulse
    - Plan-first with multi-file context → reduces drift; “code critic” catches some issues but is wrong ~60%, so human triage is mandatory.
    - Shift to spec-and-test ownership → agents implement, developers verify behavior — counterpoint: that’s always been the job; also test clients per Postel’s Law.
    - Tooling/practices matter → sub-agents (Claude) > Copilot for orchestration; simpler vertical architectures enable easier AI-driven table/service creation.

- LLM perspective
    - View: Performance hinges on curated context, explicit specs, and iterative verification over raw generation.
    - Impact: Engineers move toward system design and test authoring; agents handle scaffolding and refactors across large repos.
    - Watch next: Benchmarks on multi-file refactors; IDE support for sub-agents; standardized spec/test formats and PR acceptance metrics.
