# Why are there both TMP and TEMP environment variables? (2015)

- Score: 186 | [HN](https://news.ycombinator.com/item?id=47984522) | Link: https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213

### TL;DR
Chen explains why Windows has both `TMP` and `TEMP` for temporary-file locations. CP/M had no environment variables, so configuration was done by patching binaries directly. Early MS‑DOS apps were mostly CP/M ports and ignored environment variables; later DOS programs independently standardized on either `TMP` or `TEMP`. DOS 2.0’s piping logic chose `TEMP`, while Windows’s `GetTempFileName` checks `TMP` first, so both stuck around. Today, each program decides which to honor, often checking both in some arbitrary order.

---

### Comment pulse
- CP/M anecdote → Programs were configured by patching machine code because RAM, disk, and space for config parsers were extremely limited.  
- Historical nit → Readers contest “1973” as the era of CP/M on microcomputers, noting development started then but shipping systems came later.  
- Naming echoes elsewhere → Similar dualism as `http_proxy` vs `HTTP_PROXY`; tiny, early naming choices persist surprisingly long—counterpoint: some cases slowly converge via conventions.

---

### LLM perspective
- View → This is a classic example of path dependence: early arbitrary choices fossilize into long-lived conventions and tech debt.  
- Impact → OS, library, and tool authors should treat naming and precedence rules as permanent user-facing contracts, not casual details.  
- Watch next → Documentation and APIs could standardize precedence (e.g., always prefer one variable) while still honoring legacy names for compatibility.
