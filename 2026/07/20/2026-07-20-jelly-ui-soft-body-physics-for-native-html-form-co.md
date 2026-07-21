# Jelly UI: Soft-body physics for native HTML form controls

- Score: 296 | [HN](https://news.ycombinator.com/item?id=48981620) | Link: https://jelly-ui.com/

### TL;DR
Jelly UI is a dependency-free Web Components library that wraps native-style form controls in soft-body, “jelly” physics, with built-in dark mode, RTL support, and WCAG AA color tokens. It integrates via a single module script and custom elements like `<jelly-button>`. HN discussion focuses on performance of its requestAnimationFrame loop, subtle UX correctness issues when reimplementing standard controls, and thoughtful handling of reduced-motion accessibility, alongside broader debate over playful versus minimal, utilitarian UI—and some Flash-era nostalgia.

---

### Comment pulse
- Performance skepticism → One user claims constant RAF-driven repaints per component are “crazy”; others say profiling shows an active set, microsecond costs, like standard game loops.
- UX correctness → Custom controls initially mishandled click-drag-release outside bounds; commenters stress parity with native behavior, author quickly patches logic.
- Accessibility and taste → Respects prefers-reduced-motion and now offers an override; some love playful feedback, others increasingly strip animations for focus and comfort.

---

### LLM perspective
- View: Technically clever niche library showing how far Web Components and CSS/JS can push “feel” without heavy frameworks.  
- Impact: Most useful for marketing sites, playful dashboards, or prototypes, less so for conservative enterprise UI.  
- Watch next: Benchmarks on low-end devices, thorough keyboard/screen-reader audits, and patterns for safely re-skinning native controls without UX regressions.
