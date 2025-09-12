# Stop writing CLI validation. Parse it right the first time

- Score: 203 | [HN](https://news.ycombinator.com/item?id=45151622) | Link: https://hackers.pub/@hongminhee/2025/stop-writing-cli-validation-parse-it-right-the-first-time

- TL;DR
  - The author argues “parse, don’t validate” for CLIs: define command schemas with parser combinators so illegal flag combos are unrepresentable. Their TypeScript library, Optique, encodes dependencies, mutual exclusivity, and mode-specific options; TS infers precise unions, removing ad‑hoc checks and easing refactors. It’s young. HN notes this mirrors Zod-style upfront parsing and established Haskell/Rust approaches (optparse-applicative, Clap), debates Node CLI runtimes, and flags error aggregation/diagnostics as the hard part; related tools like Rad offer declarative constraints.

- Comment pulse
  - Parse upfront into typed structures → invariants live in types, downstream code stops checking; fewer bugs and simpler refactors.
  - Use Rust/Clap; ship native binaries → smaller footprint. — counterpoint: everything has deps; internal CLIs accept runtimes; many builds are harder than bundling Node.
  - Concern: accumulating friendly errors when illegal states are unrepresentable → answer: applicative parsers accumulate; libraries provide aggregate errors and recovery hooks.

- LLM perspective
  - View: Typed parser combinators shift complexity to compile time; less glue code beats ad-hoc validators.
  - Impact: Teams shipping multi-command CLIs gain safer refactors, clearer invariants, and easier reuse across subcommands.
  - Watch next: Error aggregation UX, helpful diagnostics, Windows packaging, runtime size, and benchmarks against Clap/yargs/commander.
