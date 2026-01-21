# Scaling long-running autonomous coding

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46686418) | Link: https://simonwillison.net/2026/Jan/19/scaling-long-running-autonomous-coding/

### TL;DR
Cursor ran hundreds of coordinated coding agents for a week to build a new Rust web browser engine (FastRender), producing ~1M lines of code and a working, if glitchy, browser. Simon Willison built it locally and found the rendering clearly custom, yet surprisingly competent. The project leans on existing libraries and specs, raising questions about what “from scratch” and “autonomous” really mean. HN sees this as an early but important proof that orchestration, testing, and conformance suites will define large-scale AI coding.

### Comment pulse
- Tests become central asset → as code generation gets cheap, high-quality test suites and specs control correctness—counterpoint: models will overfit tests, not true intent.  
- Autonomy and “from scratch” debated → heavy use of libraries, unclear human supervision, missing discussion of WPT/fuzzing; main challenges remain speed, correctness, and security at browser scale.  
- Costs and nature of LLMs → concern over token, energy, and environmental costs vs human teams; consensus that LLMs mimic intelligence and still require strong, automated verification.

### LLM perspective
- View: Agent swarms plus rich specs/tests turn software creation into managing constraints and verification, not manually writing every component.  
- Impact: Small teams can attempt “too big” projects; long-term value shifts toward tests, architecture, and security auditing.  
- Watch next: Rigorous benchmarks using web-platform-tests, fuzzing, perf/security metrics comparing AI-built systems to traditional browser engines.
