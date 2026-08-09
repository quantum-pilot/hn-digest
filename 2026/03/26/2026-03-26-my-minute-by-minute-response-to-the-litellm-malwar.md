# My minute-by-minute response to the LiteLLM malware attack

- Score: 269 | [HN](https://news.ycombinator.com/item?id=47531967) | Link: https://futuresearch.ai/blog/litellm-attack-transcript/

### TL;DR

A frozen Mac and 11,000 Python processes led an ML engineer to discover poisoned LiteLLM 1.82.8 minutes after its PyPI upload. A transitive `uvx` install brought in an auto-executing `.pth` file designed to steal credentials, persist on Linux, move laterally through Kubernetes, and exfiltrate data; recursive Python launches also created the conspicuous fork bomb. Claude Code initially blamed ordinary tooling, then helped trace the package, inspect it in isolation, assess exposure, find reporting contacts, and publish a disclosure within 72 minutes.

### Comment pulse

- Security practitioners welcomed the high-quality, AI-assisted report — counterpoint: reopening Cursor after suspected compromise violated basic quarantine practice.
- Readers cautioned that agents lack responsibility and might accidentally execute hostile samples despite explicit safety instructions.
- Package feeds already support partner scanning; dependency cooldowns could give scanners time to flag suspicious fresh releases before broad installation.

### LLM perspective

- **View:** AI can compress forensic expertise, but confident early misdiagnoses demand persistent human skepticism.
- **Impact:** Non-specialists can escalate credible incidents faster, while unsafe agent actions can enlarge exposure.
- **Watch next:** Registry response speed, dependency-delay adoption, credential-rotation evidence, and safer malware-analysis guardrails.
