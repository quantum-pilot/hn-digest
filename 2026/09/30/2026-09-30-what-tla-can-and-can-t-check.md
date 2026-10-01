# What TLA+ can and can't check

- Score: 228 | [HN](https://news.ycombinator.com/item?id=49909056) | Link: https://buttondown.com/hillelwayne/archive/what-tla-can-and-cant-check/

### TL;DR

TLA+ excels at modeling concurrent systems through state behaviors and checking invariants, actions, liveness, and refinement, but it cannot eliminate the need to choose and formalize the right properties. Important limits include real time, floating point, multi-step relations, reachability, statistical and security hyperproperties, and properties of the entire state graph. Auxiliary variables, self-composition, TLC features, or other tools can cover subsets at significant complexity. HN adds implementation drift and weak-memory semantics as practical gaps, rejecting claims that formal specifications make unreviewed AI code automatically safe.

### Comment pulse

- Verified specifications do not guarantee implementations → practitioners combine TLA+ with SPARK or property tests, but translation still requires substantial human checking.
- Weak-memory behavior is especially awkward → modeling compiler and CPU reorderings may require custom memory-system logic with enormous state spaces.
- Formal methods cannot replace understanding → commenters see generated specifications as useful guardrails — counterpoint: misunderstood invariants can preserve false confidence.

### LLM perspective

- View: Formal verification moves uncertainty into models and properties; it does not erase specification, implementation, or environmental gaps.
- Impact: AI-assisted teams need layered assurance linking intent, executable code, tests, runtime behavior, and deployment assumptions.
- Watch next: Evaluate specification synthesis, traceability tools, weak-memory libraries, property-derived tests, and defect rates on real agent-generated systems.
