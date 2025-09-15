# AI models need a virtual machine

- Score: 234 | [HN](https://news.ycombinator.com/item?id=45074467) | Link: https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/

- TL;DR
    - The authors propose a “Model Virtual Machine”: a standardized orchestrator layer between AI models and the outside world (tools, data, users), akin to the JVM for agents. It would define typed operations (model/tool lifecycle, tool calls, memory, prompts, control flow) and enforce security, isolation, auditing, and portability. They cite MCP, OpenAI tool-calling, and secure orchestrators like FIDES/AC4A, arguing models and interfaces must co-evolve. HN debates terminology and scope, emphasizing sandboxing/capabilities, information-flow partitioning, and practical container/WASM paths.

- Comment pulse
    - VM is misnamed → this is sandboxing/authorization around tool calls; specifics are vague — counterpoint: a common spec could still improve portability and safety.
    - Need capability security → grant explicit, minimal capabilities; orchestrator tracks data provenance and spawns least-privileged subtasks with taint-tracking to prevent sensitive-data exfiltration.
    - Treat LLM as a user → per-context allow/deny/ask permissions and finer-grained command whitelists; WASM or containers provide isolation many already rely on.

- LLM perspective
     - View: Standardizing the orchestrator interface is useful; calling it a VM is branding, but a spec reduces bespoke agent glue.
     - Impact: Vendors can swap models safely, tools become portable, audits and metering unify; OS, cloud, and IDEs converge on capability APIs.
     - Watch next: MCP extensions for capabilities, FIDES/AC4A real-world trials, WASM sandbox patterns, and a draft spec with test suites and threat models.
