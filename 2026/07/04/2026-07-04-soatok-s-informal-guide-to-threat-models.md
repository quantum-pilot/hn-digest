# Soatok's Informal Guide to Threat Models

- Score: 121 | [HN](https://news.ycombinator.com/item?id=48781597) | Link: https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/

- TL;DR  
  An informal, opinionated guide explains threat modeling as clarifying “who attacks what and why,” not producing compliance paperwork. Security claims are meaningless without explicit assets, adversaries, and assumptions, and models must evolve as systems change. The author applies this to messaging protocols (e.g., critiquing Signal’s threat model) and to post‑quantum cryptography, arguing for preparing seriously for Q‑Day and questioning hybrid PQ+ECDH. HN readers liked the clarity and humor but debated the author’s tone, Signal take, and quantum pessimism.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Threat modeling as explicit assumptions, not checklist → helps define “secure for whom?”, complements shorter privacy‑oriented guides; open question: how to keep models current over time.  
  - Author’s pro‑Signal history and abrasive tone reduce trust for some → they see limited nuance — counterpoint: others note this piece also criticizes Signal’s threat model.  
  - Post‑quantum section sparks debate → some doubt Q‑Day or abandoning ECC, others (including author) cite accelerated timelines and argue hybrid PQ+ECDH is weaker than pure PQ.

- LLM perspective  
  - View: Treat threat models as living documents; revise with each architecture change and after incidents, not only at project start.  
  - Impact: Messaging, wallet, and infra vendors should publish explicit threat models so users can align product choices with their risks.  
  - Watch next: Track NIST PQC rollout, major providers’ Q‑Day timelines, and real‑world data comparing hybrid versus pure PQ deployments.
