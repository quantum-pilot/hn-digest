# Bring Back Idiomatic Design

- Score: 432 | [HN](https://news.ycombinator.com/item?id=47738827) | Link: https://essays.johnloeber.com/p/4-bring-back-idiomatic-design

### TL;DR
Author laments the loss of “idiomatic design”: shared UI conventions that made desktop apps predictable (menus, shortcuts, native widgets, clear labels). On the web, frameworks, custom components, touch constraints, and WebAssembly apps have produced idiosyncratic interfaces, broken browser behaviors, and cognitive overhead for routine tasks like entering dates or credit cards. He urges using native HTML/browser idioms, clear text over icons, and internal consistency. HN commenters supply concrete UX horror stories and debate whether true standardization is still feasible.

### Comment pulse
- Inconsistent key behaviors (Enter vs Ctrl/Shift+Enter across Slack, Teams, GitHub) force users to juggle mental models; commenters want globally stable, context-aware shortcuts.  
- Root causes debated: missing system frameworks, rushed PM-led decisions, dark-pattern incentives—counterpoint: modern UX juggles accessibility, security, legacy browsers, and endless devices, making consensus hard.  
- OS UI kits once enforced idioms; the web’s document roots and roll-your-own controls mean every app reinvents widgets like date pickers and credit-card forms.  

### LLM perspective
- View: Idioms are shared mental models; reusing them beats bespoke “clever” UIs, especially for forms, navigation, and keyboard handling.  
- Impact: Consistent web idioms reduce onboarding time, errors, accessibility bugs, and support costs across SaaS, banking, and enterprise software.  
- Watch next: Browser-native components for dates, payments, and rich text; opinionated design systems; telemetry-guided standards for shortcuts and input behavior.
