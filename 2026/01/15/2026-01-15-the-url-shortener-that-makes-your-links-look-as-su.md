# The URL shortener that makes your links look as suspicious as possible

- Score: 750 | [HN](https://news.ycombinator.com/item?id=46627652) | Link: https://creepylink.com/

- TL;DR  
    - CreepyLink is a joke URL shortener that deliberately produces maximally sketchy-looking links, reviving the old ShadyURL concept. Beyond humor, HN readers noticed emergent utility: some LLM agents and browsers treat these links as suspicious, refusing to follow them or triggering red “dangerous site” warnings. That makes CreepyLink an accidental probe of model and browser safety heuristics, and a lightweight way to experiment with link-based bot-filtering, while also serving as a classic “learn-by-building” side project.

- Comment pulse  
    - LLM-deterrent angle → Several models (Gemini, GPT-5.2, Mistral) refuse to follow CreepyLink URLs, suggesting a crude anti-agent or anti-scraping filter—counterpoint: bulk crawlers for training may ignore this.  
    - Browser reactions → Chrome and Firefox flag many generated URLs as deceptive or dangerous, showing how aggressively modern safe-browsing systems score odd-looking domains/paths.  
    - Toy-project value → Repeating the “shady URL” idea is fine; URL shorteners make good practice for web, DB, and system design, plus this replaces now-defunct ShadyURL.

- LLM perspective  
    - View: This is accidental adversarial UX testing for both browser security and LLM link-follow policies, wrapped in a joke.  
    - Impact: Site owners, bot-wranglers, and ML engineers can cheaply probe or gate automated traffic without complex infrastructure.  
    - Watch next: More formal “do-not-follow” link standards for agents, benchmarks of model crawling behavior, and explicit policies in model docs.
