# How SQLite is tested

- Score: 219 | [HN](https://news.ycombinator.com/item?id=46303277) | Link: https://sqlite.org/testing.html

- TL;DR  
SQLite backs ~156k lines of C with ~92M lines of tests and four independent harnesses (TCL suite, embedded TH3, SQLLogicTest, dbsqlfuzz). It systematically simulates OOM, I/O errors, crashes, malformed files, and boundary conditions; uses MC/DC branch coverage, mutation testing, sanitizers, Valgrind, leak checks, and assert-heavy builds; and reruns historical fuzz cases. Human-run release checklists tie it together. HN admires this craftsmanship, debates checklist quality, notes proprietary test harnesses, and recalls bugs in newer JSON features.

- Comment pulse  
  - Checklists as in aviation/medicine/SQLite → lightweight shared rituals improve coordination and catch omissions—counterpoint: many organizations create bloated, useless checklist bureaucracy.  
  - Proprietary tests in public-domain project → SQLite uses closed TH3/dbsqlfuzz; commenters wonder if “closed test suite” could be a viable open‑core-style business model.  
  - Uneven feature maturity → core is rock-solid but JSON functions had escaping/Unicode bugs; reminder that even exemplary test cultures still ship edge‑case defects.

- LLM perspective  
  - View: SQLite’s process shows industrial-strength assurance doesn’t require formal methods; disciplined fuzzing, anomaly tests, and coverage already get extraordinary reliability.  
  - Impact: Most teams can’t afford 590× test-to-code ratio, but can cheaply adopt OOM/I/O simulation, fuzzing, and regression-first bug fixes.  
  - Watch next: Expect more reusable fuzz corpora, open-source structure-aware fuzzers, and checklist tooling that balances human judgment with automation.
