# JSON-LD Explained for Personal Websites

- Score: 141 | [HN](https://news.ycombinator.com/item?id=48621517) | Link: https://hawksley.dev/blog/json-ld-explained-for-personal-websites/

## TL;DR
The post is a practical, copy‑pasteable guide to adding JSON‑LD structured data to a personal site so search engines and LLM crawlers better understand who you are and what each page represents. It walks through core Schema.org types—WebSite, WebPage/ProfilePage/CollectionPage, Person, SoftwareApplication, BreadcrumbList, Blog, BlogPosting—and how to connect them via `@id`, `isPartOf`, `mainEntity`, and `breadcrumb`. HN commenters debate whether this mainly benefits site owners (visibility, rich snippets) or entrenched platforms and their AI summaries.

---

## Comment pulse
- Structured data feels like “fighting the last war” → Google now surfaces long LLM answers above original pages, so SEO tweaks seem futile.  
- Still worth doing → standardized metadata helps non‑Google search, maps, and future competitors; refusing to structure data only cements incumbents’ advantage.  
- Practical concerns → JSON-LD is easy, but duplicating metadata across HTML and JSON-LD demands consistency hygiene; some see duplication as acceptable cost.

---

## LLM perspective
- View: JSON-LD on personal sites is low-effort infrastructure that helps humans, crawlers, and future tools, even if Google’s benefits shrink.  
- Impact: Solo developers and small businesses can punch above their weight in entity disambiguation, authorship, and project discovery.  
- Watch next: Whether alternative search/AI products explicitly leverage JSON-LD graphs for attribution, ranking, and outbound clicks.
