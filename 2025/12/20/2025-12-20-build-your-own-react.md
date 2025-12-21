# Build Your Own React

- Score: 163 | [HN](https://news.ycombinator.com/item?id=46332526) | Link: https://pomb.us/build-your-own-react/

## TL;DR
The article walks you through building a tiny React clone (“Didact”) from scratch, mirroring React 16.8’s core architecture but skipping most optimizations. Step by step, it implements JSX’s `createElement`, a basic `render`, then adds concurrent rendering with `requestIdleCallback`, fiber trees for incremental work, a separate commit phase, diff-based reconciliation with effect tags, function components, and a minimal `useState` hook system. Hacker News readers particularly praise the interactive, code-driven presentation and report using the ideas in other runtimes and languages.

---

## Comment pulse
- Interactive docs are outstanding → CodeHike-powered animations make React internals tangible and easier to follow than videos or static code — counterpoint: heavy animation lags when scrolling quickly.  
- Tutorial is practically useful → Readers reuse the simplified renderer model for backend JSX renderers or Python/Tk “React-like” UIs, skipping events and hooks where unnecessary.  
- Documentation bar-raising → Many wish commercial vendors adopted similarly guided, narrative, and executable documentation; author is building DocsKit to make this style easier to adopt.

---

## LLM perspective
- View: This is an ideal “concept-minimal” reference for explaining fibers, reconciliation, and hooks without React’s production complexity.  
- Impact: Helps intermediate JS devs bridge from “using React” to understanding its scheduling and rendering model, enabling custom renderers and informed optimization.  
- Watch next: Compare Didact to real React profiler traces; implement keys, `useEffect`, and partial tree skipping to explore real-world trade-offs.
