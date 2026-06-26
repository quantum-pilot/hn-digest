# LuaJIT 3.0 proposed syntax extensions

- Score: 223 | [HN](https://news.ycombinator.com/item?id=48667336) | Link: https://github.com/LuaJIT/LuaJIT/issues/1475

### TL;DR
LuaJIT 3.0 is considering a batch of syntax extensions: C/JS-style logical operators, ternary expressions, compound assignment, and bitwise operators, many borrowed from Luau. Commenters like the modernization and potential easing of cross-dialect code (and AI-generated Lua), but worry LuaJIT is drifting from standard Lua 5.x into its own language and duplicating syntax for little gain. A parallel debate: add a dedicated ternary, or instead make if-then-else an expression with broader benefits and deeper semantic costs.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Ternary vs if-expression → Some prefer `if x then y else z` for nesting; critics say value-returning blocks alter Lua’s semantics more than adding `?:`.
- Direction and naming → LuaJIT is effectively a Lua 5.1 fork; added features and Luau imports make some argue 3.0 deserves a distinct language name.
- JS-style operators (`&&`, `||`, ternary) → Proponents cite familiarity and AI tooling; opponents say duplicating `and`/`or` adds complexity without solving problems — counterpoint: Ruby uses both.

---

### LLM perspective
- View: LuaJIT 3.0 is drifting into “Lua-like” territory; explicit governance and compatibility targets will matter more than individual operators.  
- Impact: Game engines, Roblox-adjacent ecosystems, and AI-generated Lua benefit from Luau overlap; multi-version runtimes and bindings face higher complexity.  
- Watch next: Clear spec of which Lua 5.2–5.4 features land, performance regressions from new syntax, and tooling support across dialects.
