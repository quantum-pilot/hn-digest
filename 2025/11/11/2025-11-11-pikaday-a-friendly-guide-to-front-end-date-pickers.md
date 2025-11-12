# Pikaday: A friendly guide to front-end date pickers

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45887957) | Link: https://pikaday.dbushell.com

- TL;DR
  - Bushell’s guide argues most apps shouldn’t ship JS date pickers: prefer native date/time inputs or simple split/select/masked fields, lean on browser a11y/i18n, progressive enhancement, and user testing. Range pickers and relative dates are often fragile; simplify flows instead. He refuses to recommend a library. HN counters with field stories: native mobile pickers hid year controls and confused users; some advocate plain text plus ISO storage, others note calendars are essential for planning and time zones make “today/tomorrow” hazardous.

- Comment pulse
  - Native pickers can fail → hidden year controls led to hundreds of taps; switching to text+dropdowns ended complaints — counterpoint: avoid calendar UIs for date-of-birth.
  - Plain text beats widgets → fewer browser/a11y pitfalls; store ISO strings — counterpoint: trip planning needs a calendar; ISO/offsets get tricky for future cross-border times.
  - Relative dates are risky → 'Today/Tomorrow' ambiguity around midnight, DST, time zones; prefer explicit dates with clear timezone context.

- LLM perspective
  - View: Default to native inputs or simple fields; offer typing and calendar only when visualization is necessary.
  - Impact: Reduces errors and dev burden; improves a11y/compliance; still meets planning use cases via optional, well-tested calendar overlays.
  - Watch next: Browser datepicker accessibility fixes, EAA enforcement, design-system components that combine free-text parsing with constrained selects and timezone clarity.
