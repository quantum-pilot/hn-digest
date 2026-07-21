# Perfection is not over-engineering

- Score: 184 | [HN](https://news.ycombinator.com/item?id=48979120) | Link: https://var0.xyz/posts/perfection-is-not-over-engineering.html

- TL;DR  
Author argues “perfection” in software isn’t the same as over‑engineering: perfection means the only design that satisfies clear, honest requirements, while over‑engineering means solving the wrong or imaginary problems, often via fashionable complexity like unnecessary microservices. HN discussion agrees that vague requirements and cargo‑cult scalability create brittle systems, but splits on language: some see “product” and “perfection” mindsets as psychologically or ethically toxic, others defend scoped “good enough” solutions that explicitly ignore rare edge cases.

- Comment pulse  
  - Perfection ≠ over-engineering → real issue is weak requirements, seen in teams running many microservices for imaginary scale, losing data integrity and adding ops burden.  
  - Perfection talk is double-edged → often excuses shipping crap; sometimes just sets “cover 90% use cases, defer rare edges”. — counterpoint: on-call engineers resent this.  
  - Product mindset debate → author treats systems as products needing user requirements; critics prefer “tool” framing, arguing product goals (revenue) easily misalign with user interests.

- LLM perspective  
  - View: Treat “perfect” as contextually correct under explicit constraints, but name and document consciously accepted imperfections and deferred work.  
  - Impact: Clearer requirements shift effort from fashionable architectures toward simpler monoliths, tests, and observability matching real scale and failure modes.  
  - Watch next: Introduce reviews that default to monoliths, requiring concrete scale and ownership justifications before accepting extra services or infrastructure.
