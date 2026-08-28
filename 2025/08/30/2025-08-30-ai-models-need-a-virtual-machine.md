# AI models need a virtual machine

- Score: 234 | [HN](https://news.ycombinator.com/item?id=45074467) | Link: https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/

### TL;DR

A SIGPLAN viewpoint proposes standardizing the orchestration layer around AI models as a “model virtual machine.” This layer would load models and tools, construct context, parse structured outputs, mediate tool calls, manage memory and user input, enforce typed permissions, and expose auditing and resource data. The authors argue a shared specification could separate models from integration logic while improving portability, safety, and governance, drawing on MCP, structured tool calling, secure orchestrators, and agent runtimes. The post seeks consensus rather than presenting a concrete instruction set or implementation.

### Comment pulse

- Critics said “VM” obscures a proposal closer to an orchestrator, sandbox, capability system, or access-control runtime.
- Discussion emphasized that safety depends jointly on permitted actions, data provenance, user scope, and task partitioning.

### LLM perspective

- View: Standardizing enforcement boundaries is valuable, but the VM metaphor is less precise than the security problem.
- Impact: Interoperable policy and audit hooks could reduce duplicated agent infrastructure without making model behavior trustworthy.
- Watch next: A minimal specification must define capabilities, information flow, identity, confirmation, and failure semantics concretely.
