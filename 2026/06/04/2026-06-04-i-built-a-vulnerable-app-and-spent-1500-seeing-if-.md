# I built a vulnerable app and spent $1,500 seeing if LLMs could hack it

- Score: 378 | [HN](https://news.ycombinator.com/item?id=48392343) | Link: https://kasra.blog/blog/i-spent-1500-seeing-if-llms-could-hack-my-app/

### TL;DR
- A security researcher built a deliberately vulnerable book-review app (React Native + FastAPI + Firebase) where the real bug was open Firebase/Firestore access, not the hardened API.  
- Using an agentic harness with tools and a $10/2h/run cap, they spent ~$1,500 testing many frontier models on whether they could autonomously find and exploit it.  
- GPT‑5.5 solved it 7/10 runs; DeepSeek V4 Pro was a cheap runner‑up; most others failed due to distraction, wrong attack paths, or safety refusals—especially Anthropic and Gemini.

---

### Comment pulse
- Anthropic models are increasingly over‑guardrailed → frequent refusals on benign security, RE, and even UX tasks, pushing users and orgs toward laxer, “more useful” models.  
- Methodology is naive → expecting fully autonomous exploitation is unrealistic; Chinese models shine when guided by a human analyst — counterpoint: autonomy is exactly what many vendors currently promise.  
- Guardrails scoring is muddled → GPT had relaxed safety; Claude/Gemini were blocked yet still occasionally exploited targets, suggesting both unfair comparison and leaky safety systems.

---

### LLM perspective
- View: Today’s models are strong security assistants but poor fully autonomous pentesters; they tunnel on APIs and miss alternative attack surfaces like misconfigured backends.  
- Impact: Security teams should pair humans with LLMs for triage, RE, and exploit scripting, treating agents as juniors, not independent red‑teams.  
- Watch next: Reproducible, open CTF-style benchmarks; tunable safety tiers per use case; better agent frameworks for systematic tool use instead of aimless API poking.
