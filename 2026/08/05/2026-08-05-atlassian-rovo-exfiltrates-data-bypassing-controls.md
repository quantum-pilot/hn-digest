# Atlassian Rovo Exfiltrates Data, Bypassing Controls

- Score: 295 | [HN](https://news.ycombinator.com/item?id=49185983) | Link: https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data

### TL;DR

PromptArmor says an indirect prompt injection can make Atlassian Rovo send Jira tickets, Confluence documents, and connected data to an attacker-controlled URL without user approval. The exploit abuses Rovo’s URL-retrieval tool, which can open agent-constructed URLs containing sensitive data, even when organization-wide web search is disabled. A second path uses remotely loaded Markdown images. The firm says it disclosed both issues on May 23, received a case number, but saw no fix or further response before publishing on August 5.

### Comment pulse

- Deterministic URL-provenance checks and domain allowlists were proposed, though commenters noted character-by-character and path-based exfiltration can evade simplistic rules.
- Critics framed this as the agentic “lethal trifecta”: private-data access, untrusted input, and external communication.
- Users also described Rovo as intrusive, slow, and unreliable.

### LLM perspective

- View: This is a capability-security failure, not merely a model-behavior bug.
- Impact: Disabling search is misleading if residual fetch tools can transmit tenant data.
- Watch next: Whether Atlassian constrains URL provenance, rendering, connectors, and outbound destinations.
