# Show HN: An interactive guide to how browsers work

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46488654) | Link: https://howbrowserswork.com/

- TL;DR  
    - Interactive, browser-based guide that walks users from typing a URL through DNS resolution, TCP setup, HTTP exchange, HTML parsing, DOM construction, and layout/paint/compositing, emphasizing intuition over protocol minutiae. It explains streaming, error‑tolerant parsing and how DOM changes drive rendering costs, helping developers reason about performance. HN commenters praise the clarity and interactivity, suggest covering modern HTTPS/DNS and resource loading, add historical context about pre‑DOM browsers, and recommend deeper references like HPBN and browser.engineering.

- Comment pulse  
    - DNS and transport are simplified → HTTPS resource records and HTTP/3 over QUIC mean browsers may bypass classic TCP paths entirely.  
    - DOM description is modern-centric → many early or niche browsers rendered HTML without a DOM abstraction, so wording should clarify historical and current scope.  
    - Readers want more depth → requests for visuals, subresource loading flows, and links to HPBN, Every Layout, and browser.engineering for advanced networking/layout knowledge.

- LLM perspective  
    - View: Interactive, minimal-jargon walkthroughs fill a documentation gap between specs and tutorials, especially for onboarding new web or backend engineers.  
    - Impact: Better models of parsing and rendering help teams debug layout jank, latency spikes, and caching issues faster than trial-and-error.  
    - Watch next: Next iterations could add toggles for HTTP/1.1 vs HTTP/2/3, TLS, and parallel resource loading waterfalls tied to real performance metrics.
