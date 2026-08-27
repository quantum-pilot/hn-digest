# Flow: Actor-based language for C++, used by FoundationDB

- Score: 160 | [HN](https://news.ycombinator.com/item?id=46191763) | Link: https://github.com/apple/foundationdb/tree/main/flow

### TL;DR

The supplied source is chiefly a directory listing for FoundationDB’s Flow implementation, showing an actor compiler, numerous actor-based C++ files, runtime support, build configuration, and Swift bridge code; it does not itself fully explain Flow’s semantics. Discussion describes Flow as a restricted C++ extension for type-safe actor messaging and deterministic simulation, where interfaces and the run loop can be replaced so failures replay reproducibly. Commenters cite several adopters and impressive simulation history, but those claims come from the discussion, while the C# compiler dependency and language subset draw portability concerns.

### Comment pulse

- Commenters praise deterministic simulation and typed messaging as central to FoundationDB’s reliability workflow.
- Reported adopters extend beyond FoundationDB, though the frozen repository listing does not verify those deployments.
- The C# actor compiler and incompatible C++ subset prompt calls for a Clang-based implementation.

### LLM perspective

- View: Flow’s differentiator is reproducible whole-system simulation, not actor syntax alone.
- Impact: That model can make distributed failure testing systematic, but specialized tooling raises adoption costs.
- Watch next: Authoritative semantics, compiler modernization, and evidence from deployments outside FoundationDB.
