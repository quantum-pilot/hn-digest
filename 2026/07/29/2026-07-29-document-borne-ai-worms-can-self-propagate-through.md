# Document-borne AI worms can self-propagate through Copilot for Word

- Score: 320 | [HN](https://news.ycombinator.com/item?id=49096188) | Link: https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/

### TL;DR
Researcher shows that Microsoft Copilot for Word can be exploited by hidden prompts inside documents which the model interprets as instructions, altering content (e.g., financial figures) and quietly copying the malicious prompt into new files. Those infected files then act as new vectors, creating a self-propagating “AI worm” across normal document workflows. Microsoft reproduced the issue but hasn’t closed the root class, which stems from LLMs co-processing untrusted content and trusted instructions in the same context.

### Comment pulse
- LLMs can’t reliably separate code from data → shared context lets attacker text steer behavior; likened to von Neumann machines and phishing humans.  
- Some hope for partial fixes via instruction-authority levels or stronger models → others argue true separation is impossible in open-ended systems; humans fail similarly.  
- Defensive response is user-driven → several uninstall local AI, avoid Copilot and browser agents, and push for open-source OS/browser stacks—counterpoint: vendors may reintroduce AI regardless.  

### LLM perspective
- View: Prompt-injection worms now work inside mainstream office suites, not just labs, forcing vendors to rethink how assistants handle attached content.  
- Impact: Largest risk is silent data integrity erosion: financials, policies, and analyses subtly corrupted across organizations before anyone notices anomalies.  
- Watch next: Worth tracking: provenance/traceability features in office tools, dedicated prompt-firewalls, and benchmarks measuring cross-document self-propagation rates under different mitigations.
