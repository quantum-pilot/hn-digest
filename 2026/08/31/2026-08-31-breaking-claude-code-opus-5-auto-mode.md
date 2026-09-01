# Breaking Claude Code Opus 5 Auto Mode

- Score: 370 | [HN](https://news.ycombinator.com/item?id=49506819) | Link: https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/

### TL;DR

A security researcher reports achieving code execution from a website-summary task against Claude Code Opus 5 Auto Mode. The site redirects to a ZIP whose supplied decoder is refused; Claude writes its own Python decoder inside the extracted directory, where a malicious `struct.py` shadows the standard library and launches a payload. Three small five-run variants succeeded 60–80%, so the rates are illustrative, not universal. Anthropic reportedly classified the behavior as expected, describing Auto Mode’s classifier as best-effort rather than an isolation boundary.

### Comment pulse

- Readers blamed predictable agent tool habits and Python module shadowing for turning a cautious replacement decoder into the exploit path.
- Some called it a Claude-targeted Trojan rather than prompt injection—counterpoint: the undisclosed arbitrary execution outcome remains the same.
- Sandboxing advocates stressed that approval classifiers cannot replace filesystem isolation, credential separation, and restricted network egress.

### LLM perspective

- View: Safety judged command-by-command misses malicious behavior assembled across individually plausible steps.
- Impact: Unattended agents handling untrusted content can expose developer machines even when obvious binaries are refused.
- Watch next: Benchmark adaptive chains and require safe extraction directories, isolated interpreters, and egress-denied execution.
