# Denial of service and source code exposure in React Server Components

- Score: 158 | [HN](https://news.ycombinator.com/item?id=46236924) | Link: https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components

### TL;DR
A newly disclosed CVE in React Server Components (RSC) allows denial‑of‑service and accidental source‑code exposure. Commenters trace this to RSC’s complexity: it hides a deep serialization/RPC layer and blurs the client/server boundary, making it hard to reason about what runs where or what data becomes visible. Many compare this unfavorably to earlier, clearer models (classic SPAs, Next.js pages router, traditional server‑rendered frameworks) and question React’s expansion into opaque full‑stack territory.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- RSC blurs client/server boundaries → hard to build a correct mental model; hidden deep serialization/RPC increases risk of bugs and security vulnerabilities.  
- Next.js app router worsens confusion → same file may run server‑ or client‑side, breaking assumptions about headers, env vars, and secret handling.  
- React’s full‑stack ambitions worry some → they miss simple SPAs/SSR and distrust CVE phrasing as perception management—counterpoint: others see standard disclosure and optional features.

---

### LLM perspective
- View: Hidden cross‑boundary magic is inherently fragile; security incidents are predictable when developers can’t easily see execution or data‑flow paths.  
- Impact: Teams will reconsider RSC usage, harden serialization layers, and favor architectures with clearer separations of responsibility and deployment.  
- Watch next: Better analyzers for “what runs where,” stricter framework defaults around secrets, and renewed interest in simpler server‑rendered stacks.
