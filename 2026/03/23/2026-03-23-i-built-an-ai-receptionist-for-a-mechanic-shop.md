# I built an AI receptionist for a mechanic shop

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47487536) | Link: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/

- TL;DR  
An indie dev built “Axle,” a phone-based AI receptionist for her brother’s luxury mechanic shop to recapture work from 100+ missed calls weekly. She scraped the shop’s site, built a RAG knowledge base in MongoDB with Voyage embeddings, and wired it to Claude via a FastAPI webhook behind Vapi, Deepgram, and ElevenLabs. Axle answers common questions, logs calls, and escalates unknowns for callbacks. HN discussion questions pricing accuracy, customer experience, and whether AI outperforms humans or simpler voicemail-style systems.

- Comment pulse  
  - AI quoting is unsafe → real repair costs and parts availability are variable; bad estimates risk legal issues and reputation—counterpoint: clear “estimate only” disclaimers help.  
  - Human receptionists exist → shared or part‑time staff could answer phones with nuance, suiting “luxury” branding; AI saves modest labor if conversion gain is small.  
  - Scope matters → commenters favor bots for FAQs, callbacks, or ticketing, but prefer apps or smarter voicemail for complex issues and written estimates.

- LLM perspective  
  - View: Strong engineering for a niche use-case; success hinges on tightly limiting tasks and aggressively escalating anything ambiguous to humans.  
  - Impact: If reliable, similar templates could help small services (plumbers, clinics) capture missed leads without hiring full-time front-desk staff.  
  - Watch next: Instrument live trials—conversion rate, complaint rate, quote accuracy, latency—and compare against human receptionists and enhanced voicemail workflows.
