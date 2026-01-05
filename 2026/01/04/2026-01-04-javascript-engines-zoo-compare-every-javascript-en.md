# JavaScript engines zoo – Compare every JavaScript engine

- Score: 165 | [HN](https://news.ycombinator.com/item?id=46486978) | Link: https://zoo.js.org/

### TL;DR
An open-source “JavaScript engines zoo” compares dozens of JS engines across architectures, listing speed, binary size, codebase size, language, JIT, and ECMAScript compatibility. Results show JavaScriptCore often outperforming V8, SpiderMonkey lagging, and Meta’s upcoming static Hermes doing very well without JIT on Apple Silicon. HN discussion pivots to security: running untrusted JS safely still needs multiple layers (engine, workerd-style sandboxes, containers/VMs), and in practice browser choice is now rarely constrained by pure JS speed.

### Comment pulse
- Secure sandboxing remains hard: no engine alone is “hardened”; people layer workerd, containers/VMs, memory-safe runtimes, or serverless to mitigate inevitable engine zero-days.  
- Performance surprises: JavaScriptCore often beats V8; static Hermes excels without JIT; SpiderMonkey trails, disappointing Firefox fans benchmarking JetStream2—counterpoint: many still find Firefox fast enough.  
- User impact: several note Chrome’s huge 2008 JS speed lead drove adoption, but today engine performance is “good enough”; bugs, features, and extensions matter more.  

### LLM perspective
- View: Public, comparable profiles of many JS engines help demystify trade-offs between speed, simplicity, size, and spec coverage.  
- Impact: Runtime authors can pick non-V8 engines, or JITless configurations like Hermes, when security, startup time, or footprint dominates.  
- Watch next: More systematic security testing, fuzzing results, and exploit writeups correlated with engines and configurations, not only microbenchmark charts.
