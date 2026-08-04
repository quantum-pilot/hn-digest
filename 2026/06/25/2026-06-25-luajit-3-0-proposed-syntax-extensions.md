# LuaJIT 3.0 proposed syntax extensions

- Score: 223 | [HN](https://news.ycombinator.com/item?id=48667336) | Link: https://github.com/LuaJIT/LuaJIT/issues/1475

### TL;DR

LuaJIT 3.0 proposes a conservative bundle of backward-compatible syntax additions: bitwise and floor-division operators, C-style logical aliases, ternary expressions, optional chaining, nil coalescing, and compound assignments. Each should improve quality of life, have precedent elsewhere, avoid ambiguity, and remain manageable for formatters and language servers; broader ideas such as continue, switch, default parameters, and interpolation remain unresolved. HN welcomed renewed development and conveniences but debated whether C-like aliases merely create duplicate spellings, whether ternaries should instead be if expressions, and whether LuaJIT is becoming a distinct Lua 5.1-derived language.

### Comment pulse

- Ternary design divides users → `?:` is compact and familiar — counterpoint: Luau-style `if … then … else` scales better to nesting and `elseif`.
- Logical aliases add familiarity but little capability → `&&` and `||` may help C/JavaScript users while fragmenting style and complicating tooling.
- Compatibility remains intentionally asymmetric → LuaJIT stays rooted in 5.1, adopting later or dialect features selectively where existing semantics permit.

### LLM perspective

- **View:** The strongest additions distinguish nil from false and avoid reevaluation; cosmetic aliases offer weaker benefits against lasting ecosystem cost.
- **Impact:** Developers gain concise expressions; parsers, formatters, LSPs, transpilers, and multi-version runtimes must absorb another expanding dialect boundary.
- **Watch next:** Track final syntax, metamethod semantics, precedence tests, tooling support, migration guidance, and parity with long forms.
