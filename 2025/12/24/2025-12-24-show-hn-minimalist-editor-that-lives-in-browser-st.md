# Show HN: Minimalist editor that lives in browser, stores everything in the URL

- Score: 206 | [HN](https://news.ycombinator.com/item?id=46378554) | Link: https://github.com/antonmedv/textarea

- TL;DR  
    - A tiny notes webapp runs entirely in the browser, storing content in the URL hash (deflate‑compressed) plus localStorage, so no backend is needed. Notes become shareable links; modern browsers’ large URL limits even allow book‑length text. HN commenters swap similar “data‑in‑URL” hacks (e.g., map annotation), share encoding tips, and discuss how URL size limits and tracking scripts interact with privacy, comparing this approach with both bloated commercial URLs and simple local text editors.

- Comment pulse  
    - Data-in-URL apps are great for one-off tools → trivial hosting, no database, easy sharing; people report building map and drawing variants quickly.  
    - URL capacity is surprisingly large → specs guarantee 8k+ bytes, browsers often 1–2MB; advertising trackers already exploit this for massive query strings.  
    - Privacy appeal: no server-stored notes → attractive for editors and side projects — counterpoint: tracking beacons and native offline editors can still be more private.

- LLM perspective  
    - View: Encoding full documents into URLs is a neat pattern for stateless web tools, especially for sharable prompts or snippets.  
    - Impact: Encourages ultra-light, host-anywhere utilities without auth, databases, or sync logic, ideal for indie devs and internal tools.  
    - Watch next: Libraries standardizing URL-safe compression/encoding, browser guidance on practical URL limits, and privacy-preserving analytics for such stateless apps.
