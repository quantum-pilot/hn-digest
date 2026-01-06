# During Helene, I just wanted a plain text website

- Score: 337 | [HN](https://news.ycombinator.com/item?id=46494734) | Link: https://sparkbox.com/foundry/helene_and_mobile_web_performance

### TL;DR
During Hurricane Helene, unreliable mobile data made most emergency and government sites unusable: bloated JS, heavy images, PDFs, and complex navigation blocked basic needs like road and shelter info. The only consistently useful resource was a plain-text daily email from a state representative listing food, power, fuel, and closures. The piece argues that critical sites should prioritize fast, semantic, mobile-first HTML and clear information architecture. HN discussion highlights existing but under-advertised text-only news modes, pervasive web bloat, and ideas for standardized “lite” endpoints.

---

### Comment pulse
- Many outlets already expose lite/text subdomains, but they’re hidden, still ship heavy CSS and cookie banners; commenters want a standardized “reader/text” endpoint.  
- Sparkbox’s own article page sends ~1.18MB for 6.7KB of text; a 500KB hero PNG could be a 15KB AVIF—undermining its performance message.  
- Plain HTML and forms can handle most interactions; JS-only sites like modern GitHub regress resilience. Newspack’s Helene-era text sites helped thousands but lacked discoverability.

---

### LLM perspective
- View: Treat emergency, utility, and banking sites like infrastructure, with mandated lightweight fallbacks and strict mobile performance budgets.  
- Impact: CMS vendors, agencies, and newsrooms must ship design systems defaulting to semantic HTML, progressive enhancement, and outage-conscious content.  
- Watch next: Standardize a .well-known or header for text-only views, and add disaster-mode benchmarks to performance tools and procurement checklists.
