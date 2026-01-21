# The Overcomplexity of the Shadcn Radio Button

- Score: 474 | [HN](https://news.ycombinator.com/item?id=46688971) | Link: https://paulmakeswebsites.com/writing/shadcn-radio-button/

TL;DR
- An engineer inspects a Shadcn + Radix “radio button” and finds hundreds of lines of React, Tailwind classes, ARIA roles, and JS weight replacing a simple `<input type="radio">`. They show modern CSS can style native radios cleanly, keeping built‑in semantics and accessibility, while libraries recreate controls as buttons plus hidden inputs. HN commenters debate React-era overengineering, organizational incentives that favor big stacks, where native inputs truly fall short, and when to push back on design instead of adding dependencies.

Comment pulse
- React and Tailwind encourage div-soup; many devs skip DOM/CSS, so simple widgets become frameworks on frameworks — counterpoint: some find plain React fine when minimalist.
- At scale, companies standardize on React-based stacks to ease hiring and coordination, even if a vanilla DOM/CSS approach could deliver leaner, faster interfaces.
- Some insist native inputs are hard to customize and bad on mobile; others note modern CSS and labels solve radios well, with selects still painful.

LLM perspective
- View: Prefer native elements plus light CSS for default controls; reserve heavy UI primitives for genuinely novel interactions or cross-platform widgets.
- Impact: Teams that audit component libraries often find quick bundle-size wins and simpler accessibility by swapping radios/checkboxes back to plain inputs.
- Watch next: Track emerging CSS features and native form improvements; each reduces justification for JS-heavy inputs and can inform design-system refactors.
