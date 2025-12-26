# All I Want for Christmas Is Your Secrets: LangGrinch hits LangChain Core

- Score: 59 | [HN](https://news.ycombinator.com/item?id=46386009) | Link: https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/

### TL;DR

LangChain-core had a critical deserialization bug (CVE-2025-68664) where its custom “lc” marker let attacker-shaped dicts be revived as framework objects. That enables secret exfiltration via secrets_from_env and potentially code execution, especially when LLM outputs flow into serialized metadata, logs, or caches. Patches disable risky defaults and escape lc keys, but impact is wide given LangChain’s adoption. HN mostly jokes about LangChain’s user base, holiday incident response, and whether the blog post itself was LLM-written.

---

### Comment pulse

- LangChain seen as toyish → commenters expect many production users to be slow or unable to patch—counterpoint: some are just unfamiliar, not negligent.  
- Several readers nitpick the prose, guessing parts were LLM-generated and even joking the vulnerable code itself might be, too.  
- Others quip about Christmas-timed sev1 calls and trademark issues with “LangGrinch,” sympathizing with responders but approving timely disclosure.  

---

### LLM perspective

- View: LLM-centric stacks must treat model output exactly like external user input when it can later influence deserialization or execution.  
- Impact: Security, platform, and ML teams need shared inventories of agent frameworks, versions, and secret-access paths across environments.  
- Watch next: Expect audits of other marker-based serializers and more CVEs where AI orchestration metadata crosses trust boundaries.
