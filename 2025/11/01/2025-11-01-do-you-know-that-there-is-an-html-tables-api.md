# Do you know that there is an HTML tables API?

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45781293) | Link: https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/

- TL;DR
  - HTML exposes a table-specific DOM API (HTMLTableElement/HTMLTableRowElement) with insertRow/insertCell, rows/cells indexing, and createTHead/TBody/TFoot—letting you build/mutate tables without innerHTML and its XSS risk. The author notes quirks (insertRow(-1) appends; no TH creator) and suggests modernizing it. HN says frameworks rarely use it, but it’s handy for small scripts and keyboard navigation. Some report bulk updates are slower than assembling one string, and the semantic-vs-divs debate resurfaces for data grids.

- Comment pulse
  - Table DOM API aids hand-written DOM; frameworks ignore it → virtual DOM manages elements; section inference mirrors HTML — counterpoint: still useful for demos/keyboard navigation.
  - Bulk insert performance can lag → insertRow/insertCell trigger many synchronous mutations; innerHTML builds once then parses/paints.
  - Semantic vs div debate → some replace tables/buttons with divs to avoid default styles; others report semantic usage remains common.

- LLM perspective
  - View: Use the table API for small, dynamic UIs; prefer frameworks or templating for complex, reactive tables.
  - Impact: Better accessibility and keyboard navigation when sticking to real tables instead of div-based grids.
  - Watch next: Benchmarks comparing insertRow/insertCell vs innerHTML; proposals for TH insertion and events; framework bindings if demand emerges.
