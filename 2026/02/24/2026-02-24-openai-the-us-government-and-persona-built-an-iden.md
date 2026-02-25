# OpenAI, the US government and Persona built an identity surveillance machine

- Score: 407 | [HN](https://news.ycombinator.com/item?id=47140632) | Link: https://vmfunc.re/blog/persona/

- TL;DR  
  Security researchers used Shodan and certificate-transparency logs to find openai-watchlistdb.withpersona.com and a FedRAMP Persona government deployment leaking 53MB of source via Vite sourcemaps. The code reveals a unified KYC/AML platform: biometric “face lists,” 269 automated checks, PEP facial recognition comparing selfies to politician photos, and direct SAR/STR filing to FinCEN/FINTRAC with intelligence tags. OpenAI apparently used this watchlist infrastructure before disclosing ID checks, raising concerns about consent, retention, blocked countries, and opaque denials. HN splits between seeing routine KYC and a nascent surveillance machine, while noting Persona’s quick post-incident response.

- Comment pulse  
  - Some point to Persona’s incident-review blog and CEO’s Twitter replies, describing the sourcemap leak as embarrassing but well-handled operationally—counterpoint: others see pure spin.  
  - One camp argues this is essentially standard high-end KYC/AML for regulated customers like OpenAI; nothing surprising beyond branding and tone.  
  - Others focus on broader surveillance creep: social-media vetting, visa requirements, and Persona deflecting DSARs as “just a processor,” calling for stronger privacy laws and enforcement.

- LLM perspective  
  - View: Large-scale KYC plus AI assistants and automated SAR/STR filing effectively create a semi-privatized identity-surveillance rail, even without explicit “spy” vendors.  
  - Impact: Organizations integrating Persona/OpenAI must reassess biometric consent flows, retention periods, and blocked-jurisdiction policies against BIPA, GDPR, and domestic financial-surveillance rules.  
  - Watch next: Watch for independent audits of Persona’s government stack, regulator inquiries, biometric-privacy lawsuits, and product changes adding transparency and appeal mechanisms.
