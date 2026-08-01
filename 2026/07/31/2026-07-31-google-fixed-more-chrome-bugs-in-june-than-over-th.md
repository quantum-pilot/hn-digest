# Google fixed more Chrome bugs in June than over the past two years, thanks to AI

- Score: 478 | [HN](https://news.ycombinator.com/item?id=49120097) | Link: https://blog.google/security/chrome-stronger-with-every-update/

## TL;DR
Google reports that AI-based tools helped Chrome fix more bugs in one recent month than in the previous two years combined. Discussion centers on what this really proves: some see it as evidence that C/C++’s manual memory management is fundamentally unsafe at scale and argue for Rust-like languages; others stress legacy, performance, and existing mitigations. Many commenters note AI is especially well-suited for adversarial testing and security review, while warning that headline “wins” hide false positives, regressions, and KPI gaming.

*Content unavailable; summarizing from title and comments.*

## Comment pulse
- C/C++ are unfit for massive codebases → many discovered bugs are memory issues; Rust-style safety would prevent entire classes — counterpoint: legacy systems and embedded constraints make wholesale rewrites unrealistic.  
- AI-driven security analysis is becoming table stakes → integrating LLMs with fuzzers and verification loops rapidly surfaces bugs; Firefox’s recent clean Pwn2Own round hints the approach works.  
- Skeptics question the numbers → marketing may emphasize easy or backlog bugs; missing data on reverted fixes, new bugs from AI, and false-positive rates.  

## LLM perspective
- View: AI is most valuable as an automated reviewer, fuzzer companion, and triage assistant, not as a primary code generator.  
- Impact: Security-sensitive, legacy C/C++ projects gain most—AI can stretch their safe lifetime while long-term rewrites progress slowly.  
- Watch next: Independent audits comparing AI-found vs human/fuzzer bugs, their severities, regressions, and net risk reduction across major projects.
