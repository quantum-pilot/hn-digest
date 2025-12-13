# Denial of service and source code exposure in React Server Components

- Score: 340 | [HN](https://news.ycombinator.com/item?id=46236924) | Link: https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components

### TL;DR
React disclosed two new React Server Components vulnerabilities: a high‑severity denial‑of‑service bug and a medium‑severity server‑function source‑code leak. Crafted HTTP requests can hang servers or return function source, potentially exposing hardcoded secrets. Earlier patches for last week’s critical RSC CVE were incomplete, so projects using react‑server‑dom-* (including Next.js and other frameworks) must upgrade again. HN commenters question RSC’s complexity, documentation, and overuse, arguing its opaque serialization model and blurred server/client boundary make such security issues more likely.

### Comment pulse
- RSC blurs server/client boundary, needs deep serialization; developers find behavior unpredictable, hurting team comprehension—counterpoint: contributor says bugs are in JS serializer, not RSC’s architecture.  
- Many think SSR/RSC overused: static pages or e‑commerce gain, but SaaS apps don’t; complexity and infra cost often overshadow marginal performance wins.  
- React/Next criticized for immature RSC docs and shipping “experimental” tech broadly; some read blog’s CVE framing as perception management rather than candid incident reporting.  

### LLM perspective
- View: RSC’s idea is sound but its serializer is a high-risk component; treat it like a network parser with dedicated fuzzing.  
- Impact: Framework authors should isolate and minimize dynamic language features in wire protocols; security reviews must precede new default settings.  
- Watch next: Watch for additional RSC CVEs, formal security model documentation, and independent audits from Next.js, Vercel, and major hosting providers.
