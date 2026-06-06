# Computer Use is 45x more expensive than structured APIs

- Score: 286 | [HN](https://news.ycombinator.com/item?id=48024859) | Link: https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/

### TL;DR
The authors benchmark a Claude Sonnet “computer-use” vision agent (browser-use 0.12) against the same model using structured HTTP tools for an internal admin panel task. The API-driven agent reliably finished in 8 tool calls, ~12k tokens, ~20 seconds; the vision agent needed a 14-step handcrafted UI walkthrough, took ~53 steps, ~550k tokens, ~17 minutes, and showed huge variance. They argue this gap is structural: pixels require repeated screenshots and pagination inference, whereas APIs expose full state cheaply, especially when endpoints can be auto-generated.

---

### Comment pulse
- Use hostile UIs to defeat agents → frequent UI changes, odd mouse behavior, hidden tasks; joke that many enterprise SaaS apps already do this accidentally.  
- Hybrid idea: use accessibility/DOM APIs to map UI into reusable workflows, then share scripts—counterpoint: must prevent workflows that exfiltrate sensitive data.  
- Practitioners favor APIs/CLI over “computer use” → cheaper, more reliable, and avoids giving a monkey full access to your digital house.

---

### LLM perspective
- View: Treat tokens, latency, and reliability as hard budget constraints; vision-only agents will usually lose against structured interfaces.  
- Impact: Stronger incentive to add auto-generated APIs or accessibility surfaces to internal tools instead of over-investing in general browser agents.  
- Watch next: Benchmarks on larger, messier apps; standardized “UI-to-API” mappers; security models for shared agent workflows.
