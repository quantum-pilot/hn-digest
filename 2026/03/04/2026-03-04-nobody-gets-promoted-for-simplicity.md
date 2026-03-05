# Nobody gets promoted for simplicity

- Score: 823 | [HN](https://news.ycombinator.com/item?id=47246110) | Link: https://terriblesoftware.org/2026/03/03/nobody-gets-promoted-for-simplicity/

### TL;DR
- The essay argues that many orgs implicitly reward engineers for visible complexity instead of quiet, correct simplicity. Overbuilt “platform” work generates promotion-worthy narratives; the small, boring solution that ships in two days doesn’t. This bias starts in system-design interviews (“add more boxes”) and continues through design reviews and promotion rubrics. The author urges engineers to make their simple choices legible (document rejected options and triggers to add complexity later) and leaders to explicitly value avoided complexity, not just impressive architectures.

---

### Comment pulse
- Interview incentives favor complexity → candidates punished for saying “use Google Sheets/Postgres,” even when correct. Better: acknowledge off‑the‑shelf, then design under stated constraints.  
- AI lowers build cost of complex architectures → maintenance, ops, and understanding costs remain; orgs without strong “simplicity/ownership” culture will drown in AI-generated systems.  
- Promotions allegedly follow “impact, not complexity” → but ladders emphasize large, cross-team initiatives, so simple, high-ROI work often needs extra storytelling to count as impact.

---

### LLM perspective
- View: The central problem is that avoided work is invisible; simplicity must be framed as explicit, documented tradeoffs.  
- Impact: Teams that tie ownership/on-call to complexity will naturally favor simpler designs and resist AI-generated overengineering.  
- Watch next: Better system-design interviews and promotion rubrics that ask, “Did you make the system easier to change?” instead of “How big was your project?”
