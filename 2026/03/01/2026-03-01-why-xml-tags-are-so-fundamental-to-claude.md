# Why XML tags are so fundamental to Claude

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47207236) | Link: https://glthr.com/XML-fundamental-to-Claude

- TL;DR  
  - The article argues that Claude’s “secret sauce” is treating XML-style tags as first-class delimiters that separate different layers of language: instructions, quoted content, metadata, and tools. The author connects this to a universal principle that effective communication needs explicit markers distinguishing base discourse from embedded or higher‑order expressions, like quotation marks. HN commenters broadly accept that delimiters help, but doubt XML is uniquely powerful, pointing instead to training habits, tool-calling markup, and a lack of hard comparative evidence.

- Comment pulse  
  - Claude isn’t unique in using delimiters; every LLM has role markers. XML may work well because models learned its structure from web data.  
  - XML feels obsolete as a general format, so hype seems odd—counterpoint: people report XML-tag prompting helped, and Anthropic still documents it explicitly.  
  - Core benefit is clear sectioning, not XML per se; Anthropic’s tool API and internal safety tags use XML-like markup, inspiring jailbreak experiments and multi-model worries.

- LLM perspective  
  - View: Use whatever delimiters are easiest for you and understood by the model; XML is one successful, but not magical, choice.  
  - Impact: Teams standardizing on XML-style prompts risk overfitting to Claude; neutral formats like markdown fences or JSON aid portability across providers.  
  - Watch next: Run A/B tests: XML tags vs markdown headings vs JSON blocks for tasks, plus tool-calling accuracy and jailbreak robustness comparisons.
