# Edit store price tags using Flipper Zero

- Score: 268 | [HN](https://news.ycombinator.com/item?id=47822978) | Link: https://github.com/i12bp8/TagTinker

### TL;DR
TagTinker is a Flipper Zero app for studying and modifying infrared electronic shelf labels (ESLs), enabling custom text/image experiments on authorized tags. The project is heavily framed as a lab-only, educational research tool, but it exposes how many retail ESL systems lack authentication and can be trivially rewritten. Hacker News discussion notes that similar fraud was already possible with paper labels and at self-checkout, debates when altered prices must be honored, and highlights repurposing ESL hardware as cheap e-paper displays at home.

---

### Comment pulse
- ESL design favors simplicity and low cost over security → IR tags are easy to rewrite; similar scams existed with printed tags; RF replacements emerging.  
- Self-checkout fraud (e.g., scanning steak as bananas) → retailers deploy overhead cameras and ML (Everseen) to flag mismatches and force human review.  
- Altered ESLs rarely change what you pay → pricing comes from barcodes/POS; laws usually don’t protect fraudulently modified shelf labels, unlike genuine advertised-price errors.

---

### LLM perspective
- View: Infrared ESLs show how legacy, cost-optimized designs become widespread attack surfaces once cheap multipurpose tools like Flipper Zero exist.  
- Impact: Expect faster migration to authenticated RF ESLs and more video analytics at self-checkout, increasing surveillance and vendor lock-in for retailers.  
- Watch next: Open-source ESL stacks and Home Assistant integrations could normalize repurposing discarded tags as low-cost e-paper displays in consumer IoT.
