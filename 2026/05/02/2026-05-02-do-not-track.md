# Do_not_track

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47988592) | Link: https://donottrack.sh/

### TL;DR

DO_NOT_TRACK proposes one cross-tool environment variable for disabling telemetry and nonessential network activity: set `DO_NOT_TRACK=1` in a shell profile. It would cover advertising identifiers, usage reporting, crash uploads, and requests unrelated to core functionality. Authors are asked to honor it alongside existing product-specific controls and preferably make data collection opt-in. The proposal addresses a fragmented landscape in which .NET, Go, Homebrew, cloud CLIs, and other tools each expose different commands or variables, borrowing the simplicity of `NO_COLOR` and `FORCE_COLOR`.

### Comment pulse

- Critics said an opt-out standard normalizes tracking by default — counterpoint: supporters view one signal as pragmatic protection across already-instrumented software.
- Browser DNT’s failure prompted doubts that financially motivated collectors would voluntarily comply.
- Users described confusing offline settings and suggested DNS blocking or aggregating existing variables as more enforceable alternatives.

### LLM perspective

- A universal preference helps only when projects adopt, document, and test compliance.
- Network-level blocking verifies behavior but may break legitimate endpoints sharing domains.
- Clear precedence is needed when global and tool-specific settings conflict.
