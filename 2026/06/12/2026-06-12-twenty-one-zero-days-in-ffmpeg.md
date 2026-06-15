# Twenty One Zero-Days in FFmpeg

- Score: 287 | [HN](https://news.ycombinator.com/item?id=48510046) | Link: https://depthfirst.com/research/21-zero-days-in-ffmpeg

### TL;DR
Depthfirst used an autonomous LLM-based security agent to scan FFmpeg and found 21 previously unknown vulnerabilities, many lurking for 10–20 years, across demuxers, RTP/RTSP, and option parsing. The system doesn’t just reason about code; it generates harnesses and concrete proof-of-concept inputs, including a detailed AV1-over-RTP bug that yields reliable remote code execution from a single malicious RTSP packet. Discussion centers on FFmpeg’s long-standing fragility, the need to sandbox media stacks, and shifting from bug reports to auto-generated patches.

### Comment pulse
- FFmpeg is notoriously bug-prone; treat it as hostile and sandbox aggressively, especially since obscure codecs are still fully attacker-controllable attack surface.  
- Finding bugs is now cheap; scarce resource is maintainers’ time—tools that open correct PRs, not tickets, are what developers will actually welcome.  
- Some see this as overhyped advertising and “zero-day” misuse, yet agree remote RTSP RCE is serious and disclosure helps operators mitigate.

### LLM perspective
- View: Agentic LLM systems are starting to match deep manual audits on hardened C, especially in complex parser-heavy projects.  
- Impact: Maintainers, downstream integrators, and security teams must assume rapid, cheap discovery of latent bugs in any exposed parsing path.  
- Watch next: Standardized benchmarks for agentic security tools and practical workflows that pair auto-finders with auto-fixers maintainers can safely review.
