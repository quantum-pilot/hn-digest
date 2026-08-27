# All I Want for Christmas Is Your Secrets: LangGrinch hits LangChain Core

- Score: 59 | [HN](https://news.ycombinator.com/item?id=46386009) | Link: https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/

### TL;DR

LangChain Core’s CVE-2025-68664 arose because `dumps()` and `dumpd()` failed to escape user-controlled dictionaries containing the reserved `lc` marker. When attacker-shaped model fields pass through common serialization flows—streaming, logs, histories, or caches—the loader can mistake them for internal objects, potentially resolving environment secrets, invoking allowed constructors, or enabling execution-adjacent behavior. Versions 1.2.5 and 0.3.81 patch it. HN focused on likely patching delays, holiday incident response, and the article’s conspicuously promotional prose.

### Comment pulse

- Operational risk may outlast disclosure → commenters expect LangChain users to patch slowly despite the critical 9.3 score.
- The technical finding is compelling → discussion faulted the article’s language, branding, and presentation more than its vulnerability analysis.

### LLM perspective

- View: Marker-based serialization makes model output a trust boundary; upgrading is safer than tracing every reachable flow.
- Impact: Agent operators must inventory LangChain versions and minimize secret-bearing privileges around deserialization paths.
- Watch next: Track ecosystem patches, exploit publication, and whether additional allowlisted constructors yield direct code execution.
