# LLM Architecture Gallery

- Score: 192 | [HN](https://news.ycombinator.com/item?id=47388676) | Link: https://sebastianraschka.com/llm-architecture-gallery/

- TL;DR  
Sebastian Raschka’s LLM Architecture Gallery is a visual, regularly updated catalog of modern open-weight LLMs, each with a concise diagram and fact sheet. It contrasts dense transformers, sparse MoE, and hybrid/state-space designs, detailing scale, attention variants, long-context strategies, and efficiency tricks (e.g., sliding-window, MLA, GQA, QK-Norm). Links to configs, tech reports, and “from-scratch” repos make it a practical reference for builders. HN readers see it as a Neural Network Zoo–style map that clarifies real-world model engineering choices.

- Comment pulse  
  - Gallery praised as a modern Neural Network Zoo → modular, visual overview that bridges “NNs approximate functions” to concrete model components.  
  - Practitioners note architectures shape prompting behavior → context length and attention patterns change which input structures and layouts perform best.  
  - Some joke about expecting building architecture; others share zoomable versions for easier exploration of the dense, information-rich diagrams.

- LLM perspective  
  - View: Use this as a design-space atlas when selecting baselines, planning ablations, or reverse-engineering closed models’ likely layouts.  
  - Impact: Speeds up onboarding and communication for engineers, researchers, and educators by standardizing names and highlighting recurring architectural motifs.  
  - Watch next: Compare future gallery updates with benchmark trends to see which hybrid-attention and MoE patterns actually win in practice.
