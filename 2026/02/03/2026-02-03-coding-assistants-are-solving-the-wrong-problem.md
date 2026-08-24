# Coding assistants are solving the wrong problem

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46866481) | Link: https://www.bicameral-ai.com/blog/introducing-bicameral

### TL;DR

Bicameral argues coding assistants optimize the 16% of developer time spent coding while worsening the problem: clarifying requirements and aligning business intent with architecture. Citing studies and a survey, it says agents can bury state, data-flow, and downstream-service gaps in implementations, shifting discovery into review and production. It proposes tools that surface codebase constraints during product discussions or compare implementations with requirements. Commenters agreed expertise and problem framing matter, but disputed the premise: well-prompted models can critique designs, while inexperienced users may neither ask the right questions nor detect failures.

### Comment pulse

- Requirements determine leverage → migrations with explicit tasks work well; novel business processes expose assumptions only during implementation.
- Expertise remains the safety net → assistants accelerate unfamiliar tooling — counterpoint: users cannot reliably catch errors outside their own domain knowledge.
- Interface design shapes behavior → code-first agents encourage premature output, though critics say asking for alternatives and edge cases already changes the result.

### LLM perspective

- View: The strongest opportunity is moving AI earlier into requirements discovery while retaining human authority over tradeoffs and organizational context.
- Impact: Product and engineering teams may spend longer upstream, reducing costly rework; management must stop measuring generated-code volume as velocity.
- Watch next: Survey methods, controlled team-delivery studies, requirement-to-code traceability, defect escape rates, junior outcomes, and tools that interrupt underspecified work.
