# Jeffgeerling.com has been migrated to Hugo

- Score: 205 | [HN](https://news.ycombinator.com/item?id=46487498) | Link: https://www.jeffgeerling.com/blog/2026/migrated-to-hugo/

- TL;DR  
Jeff Geerling migrated his long‑running blog from Drupal to Hugo to escape enterprise‑grade CMS complexity and a laborious publishing workflow. Hugo matches his Markdown‑first writing, removes PHP/DB maintenance, and turns deployment into a simple build‑and‑git‑push, though comments and search are still TODO. Hacker News replies echo the appeal of static generators and hand‑rolled tools, but highlight Hugo’s breaking changes, the risk of endless tinkering, and alternatives like Jekyll or Pelican.

- Comment pulse  
  - Custom static generators feel empowering → small Lisp/Go/Python codebases are fast, understood, and stay out of the way — counterpoint: they can tempt tinkering instead.  
  - Hugo isn’t maintenance‑free → theme authors report frequent breakage from template overhauls, so pinning versions or vendoring the binary/script into source control is strongly recommended.  
  - Choosing an SSG is nontrivial → commenters debate Hugo vs Jekyll, Eleventy, Pelican, etc., balancing simplicity, docs, incremental build correctness, extensibility, and long‑term stability.

- LLM perspective  
  - View: Static generators fit personal blogs better than DXPs → they optimize for author joy, not multi‑user workflows, at traffic scales.  
  - Impact: Fewer moving parts shift effort from patching modules to writing content, but complex features like comments/search now need design choices.  
  - Watch next: Watch for reusable, self‑hosted comment and search add‑ons for SSGs, plus better migration/redirect tooling for decade‑scale blogs.
