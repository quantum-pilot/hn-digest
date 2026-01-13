# TimeCapsuleLLM: LLM trained only on data from 1800-1875

- Score: 446 | [HN](https://news.ycombinator.com/item?id=46590280) | Link: https://github.com/haykgrigo3/TimeCapsuleLLM

## TL;DR

TimeCapsuleLLM is a series of language models trained from scratch only on 1800–1875 London texts (books, legal documents, newspapers) to capture Victorian style and worldview while excluding modern concepts. Model sizes range from 16M to 700M parameters; outputs increasingly coherent, era‑accurate prose but still hallucinate and inherit OCR noise. The project also releases curated datasets, tokenizers, and simple bias analyses. Hacker News debates using time‑bounded models to probe LLM “innovation,” data limitations, historical accuracy, and the value of explicitly constrained bias.

## Comment pulse

- Pre‑1900 models as testbeds for rediscovering relativity/chemistry → intriguing AGI probe; needs GPT‑scale models, clean pre‑cutoff corpora — counterpoint: experiments and data leakage undermine conclusions.  
- Historians note prompts like “Who art Henry” misrepresent 19th‑century English, questioning the creator’s historical literacy and evaluation benchmarks.  
- Corpus reflects literate elites and newspapers, not everyday voices; some still prefer this consistent, legible bias over today’s noisy, crowd‑sourced training data.  

## LLM perspective

- View: Clever proof‑of‑concept for Selective Temporal Training, suggesting many niche LLMs could model specific eras, regions, or subcultures.  
- Impact: Useful for digital humanities, historical fiction, and studying how biases evolve when you hold time and place fixed.  
- Watch next: Scaling this to multi‑billion‑parameter models and rigorous bias/knowledge benchmarks would test whether temporal filters measurably change reasoning and recall.
