# Nicu's test website made with SVG (2007)

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45240391) | Link: https://svg.nicubunu.ro/

### TL;DR

A 2007 test site built entirely in Inkscape-authored SVG asked whether search engines would index embedded text and follow links, using a unique token as a probe. Modern HN commenters found that token in ordinary Google results, suggesting the experiment succeeded at least for text discovery. They also highlighted SVG’s sharp scaling, searchable text, small files, styling, and dark-mode potential. Downsides include font and sizing complexity, uncertain assistive-technology behavior, reader-mode fragility, and browser performance degradation with thousands of elements.

### Comment pulse

- SVG charts preserve resolution and text semantics → making them self-contained avoids broken styles in RSS readers and reader modes.
- Inline SVG can reduce requests and page weight → initial sprite construction and optimization still demand substantial manual work.
- Entire SVG interfaces remain viable within limits → canvas may outperform them once interactive element counts grow large.

### LLM perspective

- View: The experiment anticipated today’s tension between vector-native semantics and document-level interoperability.
- Impact: Publishers can gain crisp, indexable graphics if they test accessibility and non-browser consumption paths.
- Watch next: Screen-reader behavior, description indexing, JavaScript-generated SVG discovery, and large-document performance.
