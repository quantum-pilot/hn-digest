# Show HN: I used Claude Code to discover connections between 100 books

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46567400) | Link: https://trails.pieterma.es/

- TL;DR  
    - A personal project uses Claude Code plus a web-fetch tool to automatically mine ~100 mostly HN-favorite books for recurring conceptual patterns, presented as “trails” (e.g., self-deception, bottlenecks, tacit knowledge). Each trail links diverse books illustrating the same underlying idea, aiming to support syntopic reading rather than summarization. HN discussion questions whether the AI-found links are genuinely insightful or just clever labeling, contrasts this with embedding-based clustering, and shares alternative ways people use LLMs to explore complex material.

- Comment pulse  
    - Skepticism → Trails feel like loose associations; author didn’t show concrete “aha”s; 100 HN-ish nonfiction titles form too narrow a corpus.  
    - Conditional praise → Some systems-theory themed trails mix domains in surprising, illustrative ways that prompt reflection, if you already like that style of conceptual cross-connection.  
    - Adjacent experiments → Others cluster book PDFs via embeddings + UMAP/HDBSCAN or use Claude to “read” hard GitHub repos; mislabels like “Thanos fraud” highlight hallucination risks.

- LLM perspective  
    - View: Using LLMs to propose cross-book conceptual lenses is promising, but requires strong human curation and clear prompts to avoid shallow or wrong themes.  
    - Impact: Most useful for heavy readers, researchers, and engineers who want idea maps across many texts they can’t fully reread.  
    - Watch next: Open-source pipelines combining embeddings + LLM labeling, user feedback loops on trail quality, and evaluations of whether such maps change what people actually read.
