# Building an HTML-first site doubled our users overnight

- Score: 1273 | [HN](https://news.ycombinator.com/item?id=48475483) | Link: https://mohkohn.co.uk/writing/html-first/

### TL;DR

A utility replaced a failed, inaccessible React application with an Astro site built from server-rendered HTML and progressively enhanced web components. Each wizard step submitted and saved data, including uploads, on the backend; the form worked without JavaScript, on poor connections and old browsers, and met WCAG AA. Completions doubled, revealing users invisible to JavaScript analytics, and one person resumed after a month. HN endorsed the reliability gains but debated development cost: simpler foundations reduce failure modes, while rich interfaces, duplicated validation, and frontend-backend coordination can require more work.

### Comment pulse

- Simplicity versus velocity → Familiar SPA ecosystems provide reusable rich widgets — counterpoint: lightweight HTML removes client failure modes and reduces long-term complexity.
- Team boundaries → Progressive enhancement can demand backend persistence and synchronized validation at every step, challenging organizations split into frontend and backend silos.
- Established pattern → GOV.UK veterans and HTMX users described server-rendered forms, POST-redirect-GET flows, and accessibility-first wizard libraries as proven production techniques.

### LLM perspective

- **View:** Progressive enhancement is resilience engineering when users cannot choose their device, browser, connection, or service provider.
- **Impact:** Public-service teams should treat no-JavaScript completion, saved progress, and assistive compatibility as acceptance criteria.
- **Watch next:** Measure completion by browser, connection, assistive technology, JavaScript failure, resumed sessions, validation errors, and support-channel diversion.
