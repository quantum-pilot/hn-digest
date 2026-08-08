# Why are there both TMP and TEMP environment variables? (2015)

- Score: 186 | [HN](https://news.ycombinator.com/item?id=47984522) | Link: https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213

### TL;DR

`TMP` and `TEMP` coexist because DOS added environment variables to an ecosystem inherited from CP/M, whose programs used application-specific binary patches instead of shared configuration. As native DOS software adopted environment variables, both spellings emerged without a standard. DOS 2.0’s `COMMAND.COM` used `TEMP` for pipeline scratch files, while Windows’ `GetTempFileName` later preferred `TMP`; each program decides. Hacker News enjoyed the history of patchable WordStar and compared the inconsistency to HTTP proxy variable casing, while correcting the claim that CP/M was common in 1973 and noting how arbitrary decisions fossilize.

### Comment pulse

- Veterans confirmed configuring WordStar by patching machine code, a practical response to severe RAM and storage constraints.
- Readers challenged the timeline: CP/M development began around 1973–74, but it was not yet a common microcomputer operating system.
- Similar ambiguities persist in environment-variable casing, reinforcing that compatibility preserves even lightly considered early choices.

### LLM perspective

- **View:** Neither name is universally authoritative; program-specific lookup order determines behavior.
- **Impact:** Setting both variables consistently is safer when supporting heterogeneous legacy software.
- **Watch next:** Modern code should use platform temporary-directory APIs rather than interpreting historical variables independently.
