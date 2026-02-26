# Large-Scale Online Deanonymization with LLMs

- Score: 170 | [HN](https://news.ycombinator.com/item?id=47139716) | Link: https://simonlermen.substack.com/p/large-scale-online-deanonymization

- TL;DR  
  Researchers show LLM agents can deanonymize “anonymous” users by inferring biographical clues from a few posts, then searching and reasoning across platforms to match identities. Benchmarks using anonymized Hacker News–LinkedIn pairs, split Reddit accounts, and Anthropic’s Interviewer dataset demonstrate high-precision re-identification that scales to tens of thousands of candidates. The paper argues rate-limiting, scraping controls, and personal opsec are now essential. Commenters debate footprint strategies, chilling effects on public discourse, and whether activists or ordinary users will suffer most.

- Comment pulse  
  - Deanonymization takes little data → a 2008 Netflix study plus LLM-powered text matching show tiny trails uniquely identify users; pseudonymity online may effectively vanish.  
  - Footprint strategies diverge → some advocate clean, minimal posting or not playing; others consider ‘flood the zone’ obfuscation—counterpoint: more posts may give models richer signals.  
  - Who’s harmed most? → some fear mainly activists and whistleblowers; others predict targets will be ordinary workers and forum users, amplifying harassment and chilling expertise-sharing.

- LLM perspective  
  - View: Pseudonymity should treated as weak → assume any cohesive persona can be linked across sites by current or near-future models.  
  - Impact: Online communities may shrink or splinter → more private groups, ephemeral chat, and local meetups instead of persistent, searchable posts.  
  - Watch next: Regulators will likely revisit data-access norms, scraping, and retention; technologists should prototype practical obfuscation tools and privacy-first social platforms.
