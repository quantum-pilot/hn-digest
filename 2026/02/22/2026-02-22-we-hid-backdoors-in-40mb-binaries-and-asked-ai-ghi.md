# We hid backdoors in ~40MB binaries and asked AI + Ghidra to find them

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47111440) | Link: https://quesma.com/blog/introducing-binaryaudit/

## TL;DR
Quesma built BinaryAudit, a benchmark where they inject simple, realistic backdoors into large C/Rust binaries (web/DNS/SSH servers), strip symbols, and ask LLM agents to find the malicious function using tools like Ghidra and Radare2. Frontier models can now drive decompilers, trace imports, and sometimes locate real backdoor logic, but the best (Claude Opus 4.6) only solves ~49% of tasks and produces many false positives. Today, AI is a useful assistant for reverse engineering, not a trustworthy malware detector.

---

## Comment pulse
- “This only works without obfuscation” → critics say any real attacker hides imports/strings, so detection will collapse — counterpoint: authors frame this as an entry-level, non-adversarial benchmark.
- Agents as amplifiers → practitioners use LLMs to map attack surface, generate diagrams, and scan for similar patterns while humans do deep verification.
- Metrics matter → some models have 0% false positives but low detection; others trade recall for noise, so classic ROC/threshold thinking is needed.

---

## LLM perspective
- View: Treat LLMs as junior reversers plus scripting glue, not as final malware-oracle services.
- Impact: Security engineers, firmware teams, and “regular” developers gain accessible first-pass binary analysis.
- Watch next: Benchmarks with mild real-world obfuscation, better Ghidra/IDA integrations, and small fine-tuned local models deployed inside secure environments.
