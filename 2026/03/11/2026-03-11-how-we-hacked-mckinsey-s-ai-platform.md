# How we hacked McKinsey's AI platform

- Score: 377 | [HN](https://news.ycombinator.com/item?id=47333627) | Link: https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform

### TL;DR
An AI-assisted pentesting startup, Codewall, targeted McKinsey’s Lilli AI platform and found publicly exposed endpoints with almost no authorization plus a classic SQL injection. The injection stemmed from LLM-written code that safely parameterized values but concatenated JSON field names directly into SQL, letting attackers access tens of thousands of user records. HN discussion focuses less on the exploit itself and more on McKinsey’s dysfunctional incentives around internal software, LLM-driven insecurity, and questions about disclosure and Codewall’s legitimacy.

*Content unavailable; summarizing from title and comments only.*

---

### Comment pulse
- McKinsey’s incentives undermine internal software → partners chase review points; devs lack guidance, ownership; internal tools like Lilli ship half-baked, then decay, exposing security gaps.  
- Bug was simple SQL injection via LLM-written dynamic SQL and exposed unauthenticated endpoint; commenters expect similar AI-coded flaws — counterpoint: some wished it showcased prompt-injection.  
- Readers question Codewall’s legitimacy and McKinsey’s response → sparse info, but Register coverage and disclosure timeline suggest fixes and user-notification obligations are real.  

---

### LLM perspective
- View: AI agents amplify existing security negligence; they accelerate discovery, not root causes like incentives and ownership.  
- Impact: Enterprises relying on LLM-coded tooling without strong review will see more classic bugs, now exploitable at machine speed.  
- Watch next: Standardize LLM coding guardrails, require security review for AI-generated diffs, and benchmark pentest agents against human professionals.
