# Apple reveals 'shocking evidence' from ex-employee's MacBook in OpenAI suit

- Score: 207 | [HN](https://news.ycombinator.com/item?id=49527573) | Link: https://9to5mac.com/2026/08/31/apple-openai-forensic-macbook-evidence/

### TL;DR

In a supplemental brief seeking expedited discovery, Apple alleges former employee Chang Liu used a confidential power-converter circuit while working at OpenAI, employed AI agents to run simulations, and discussed restoring Apple-owned devices after learning of an investigation. Apple argues logs and metadata may disappear and that exposing trade secrets to an agent or model could create hard-to-reverse propagation. These remain Apple’s litigation claims, not adjudicated findings. Commenters debate whether “learning” meant model training or ordinary agent memory, and what clean-room separation would require.

### Comment pulse

- AI complicates containment → copied secrets may persist in files, memory, or weights, though commenters dispute which mechanism occurred here.
- Clean-room boundaries may need executions → separating specification extraction from later design could reduce contamination — counterpoint: agents might retain unauthorized access.
- Device mixing expands discovery risk → syncing work material onto personal or employer-owned hardware can expose additional accounts and forensic artifacts.

### LLM perspective

- View: The central technical question is provenance: where the schematic entered, persisted, influenced output, and remained accessible.
- Impact: Trade-secret cases may require agent logs, memory stores, prompts, model lineage, and device synchronization records.
- Watch next: The court’s discovery ruling and forensic evidence should clarify use, preservation, and whether any model weights changed.
