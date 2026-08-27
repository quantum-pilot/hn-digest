# Babel is why I keep blogging with Emacs

- Score: 212 | [HN](https://news.ycombinator.com/item?id=45453222) | Link: https://entropicthoughts.com/why-stick-to-emacs-blog

### TL;DR

The author keeps an opaque, occasionally brittle Org-mode publishing stack because Babel can execute embedded code during export, reuse sessions, exchange variables with prose, and render outputs such as tables or plots. Replacing roughly 20,000 lines of Emacs machinery with a comprehensible custom generator sounds attractive, but reproducing the Babel features actually used would take months. Commenters split between embracing Org’s extensibility and building tiny, understandable generators, while suggesting hybrids that delegate only executable blocks to headless Emacs.

### Comment pulse

- Babel earns its complexity → executable, reproducible prose supports plots and even embedded interactive HTML within one writing workflow.
- Custom generators restore ownership → small dependency-light tools can remain fast, stable, and understandable for years.
- Hybrid architecture → a bespoke publisher could call Babel through Emacs rather than reimplementing its language execution machinery.

### LLM perspective

- View: Workflow value comes from the irreplaceable capability, not the total system’s conceptual cleanliness.
- Impact: Technical writers must choose between operational transparency and integrated executable documents.
- Watch next: A minimal Babel bridge could test whether the author can retain reproducibility while shrinking publishing complexity.
