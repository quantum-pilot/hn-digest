# Gemini 3.5 Flash

- Score: 588 | [HN](https://news.ycombinator.com/item?id=48196570) | Link: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/

### TL;DR

Google launched Gemini 3.5 Flash for coding and long-horizon agents, claiming it beats Gemini 3.1 Pro on Terminal-Bench, MCP Atlas, GDPval-AA, and multimodal reasoning while outputting tokens four times faster than peer frontier models. It is generally available across Gemini, Search, Antigravity, developer APIs, and enterprise products; Gemini Spark uses it for persistent personal-agent tasks. HN admired the speed/capability claims but questioned whether the Flash label still signals affordability and whether benchmark gains survive messy visual and agentic tasks.

### Comment pulse

- Price-performance worsened despite stronger scores → one evaluation estimated 3.5 Flash cost $1,552, 5.6× 3.0 Flash Preview, with greater token use.
- Visual polish still masks structural errors → an elaborate pelican SVG omitted bicycle frame connections — counterpoint: untrained humans often misdraw bicycles similarly.
- Vendor lock-in now carries quota risk → commenters urged provider abstraction as Google raised API rates and reportedly cut AI Pro allowances.

### LLM perspective

- **View:** Benchmark leadership matters only alongside task completion, token efficiency, controllability, and workflow cost; speed alone can hide expensive verbosity.
- **Impact:** Developers gain a faster agent model but must revisit budgets, quotas, routing, and fallback providers before moving production workloads.
- **Watch next:** Independent agent benchmarks, malformed-output rates, price-normalized quality, token usage, quota stability, Spark safety, and 3.5 Pro’s promised release.
