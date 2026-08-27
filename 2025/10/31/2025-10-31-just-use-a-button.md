# Just use a button

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45774182) | Link: https://gomakethings.com/just-use-a-button/

### TL;DR

The author argues that interactive controls should use native HTML buttons rather than clickable divs. A button already exposes the correct assistive-technology role, enters keyboard focus order, and activates with Enter or Space; recreating those behaviors through role, tabindex, and key handlers adds fragile code. HN commenters broaden the lesson to anchors, images, and other semantic elements, while noting practical wrinkles: buttons inside forms default to submission, and inconsistent styling or limited native widgets have historically pushed developers toward custom controls.

### Comment pulse

- Native semantics preserve expected behavior → anchors support new tabs and buttons support keyboards without JavaScript reimplementation.
- Defaults still require literacy → authors should specify `type="button"` inside forms to avoid accidental submission.
- Platform limits encourage reinvention → styling constraints and weak native widgets sometimes motivate custom controls, increasing accessibility work.

### LLM perspective

- View: Semantic HTML is executable product behavior, not merely descriptive markup for accessibility audits.
- Impact: Correct primitives reduce code, interaction regressions, and maintenance across browsers and assistive technologies.
- Watch next: Test keyboard activation, focus order, form behavior, and screen-reader announcements in component libraries.
