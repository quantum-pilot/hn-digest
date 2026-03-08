# Sarvam 105B, the first competitive Indian open source LLM

- Score: 169 | [HN](https://news.ycombinator.com/item?id=47285422) | Link: https://www.sarvam.ai/blogs/sarvam-30b-105b

### TL;DR

Sarvam AI has open-sourced two Mixture-of-Experts LLMs, Sarvam 30B and 105B, trained entirely in India using government-backed compute and Apache-2.0 weights. Architecturally, they combine sparse MoE layers, long-context attention (GQA/MLA), and a highly optimized Indic tokenizer plus custom inference stack aimed at running from H100s down to laptops. Benchmarks show 105B competitive with 80–120B open models in math, coding, reasoning, and “agentic” tasks, while both models strongly dominate on Indian-language benchmarks, positioning them as sovereign, India-centric foundation models.

---

### Comment pulse

- Sovereign models matter → Local weights capture cultural/linguistic diversity and reduce dependence on US/China labs—counterpoint: turning this into nationalism risks *less* diversity, not more.  
- Quality and infra skepticism → Early user tests see hallucinations and “2023-level” behavior; others doubt India has chips/infra to reach true frontier scale.  
- Originality and transparency worries → People want proof it’s not just a Qwen clone, plus clearer details on data, optimization code, and the vague “Nvidia help” story.

---

### LLM perspective

- View: Technically, this is serious work: full-stack MoE, RL, Indic tokenizer, and strong benchmarks, not a thin fine-tune.  
- Impact: Most immediate value is for Indian devs, enterprises, and government wanting local, license-friendly, high-Indic-coverage models.  
- Watch next: Independent evals, open-source of key tooling/datasets, and a clearly articulated business/governance model will determine if this becomes India’s DeepSeek-equivalent.
