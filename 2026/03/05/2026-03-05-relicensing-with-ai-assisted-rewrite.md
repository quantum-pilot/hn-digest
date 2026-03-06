# Relicensing with AI-Assisted Rewrite

- Score: 372 | [HN](https://news.ycombinator.com/item?id=47257803) | Link: https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/

## TL;DR

A popular Python library, chardet, was “rewritten” using Claude and relicensed from LGPL to MIT, prompting its original author to allege a GPL violation. The post explains that true clean‑room rewrites require strict separation between people who saw the original code and those who write the replacement—something AI breaks if it’s directly prompted with LGPL code. A recent US Supreme Court move affirming “human authorship” deepens the paradox: AI-written code may be uncopyrightable, derivative of LGPL, or even effectively public domain, threatening copyleft’s enforceability.

---

## Comment pulse

- LLM-as-clean-room is dubious → models likely trained on GPL/LGPL; they can’t reliably “ignore” that influence, making the maintainer’s process hard to defend legally.  
- Clean room vs. copying → real test is substantial similarity and information flow; independent creation is allowed but nearly impossible to prove with LLM involvement.  
- Generative AI vs. copyright → AI makes expression cheap, blurring “derivative work” and weakening GPL as leverage—counterpoint: feeding original code to AI still clearly creates a derivative.  

---

## LLM perspective

- View: Treat AI as an amplifier of whatever licensing posture you already have; it doesn’t magically cleanse or void upstream obligations.  
- Impact: Library users inherit hidden license risk; compliance teams must now audit both code and generation process, including model usage logs.  
- Watch next: First test cases over AI-assisted relicensing, “clean” training datasets, and new OSS norms (e.g., AI-use policies, contributor attestations).
