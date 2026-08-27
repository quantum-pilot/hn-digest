# Show HN: I made a down detector for down detector

- Score: 524 | [HN](https://news.ycombinator.com/item?id=45974012) | Link: https://downdetectorsdowndetector.com

### TL;DR

This tiny independent service checks whether DownDetector itself responds from London, Auckland and New York, reporting HTTP status and latency for each region. The supplied snapshot shows successful 200 responses everywhere, then extends the joke with recursively monitored status checkers. Readers appreciated the tool after DownDetector appeared unavailable during a Cloudflare incident. They also identified a key limitation: an HTTP response can look healthy while a broken human-verification challenge makes the site unusable to actual visitors.

### Comment pulse

- Independent monitors are useful when providers differ by code, infrastructure and deployment cadence.
- Reachability is not usability → status checks should distinguish successful origin responses from blocked interactive workflows.

### LLM perspective

- View: Recursive monitoring is funny, but it exposes the real need for independent failure domains.
- Impact: Simple regional probes can clarify outages without relying on the service being diagnosed.
- Watch next: Challenge-page detection, content assertions and hosting separation between every monitoring layer.
