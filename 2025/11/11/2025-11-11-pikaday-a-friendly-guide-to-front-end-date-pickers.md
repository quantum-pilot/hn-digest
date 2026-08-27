# Pikaday: A friendly guide to front-end date pickers

- Score: 113 | [HN](https://news.ycombinator.com/item?id=45887957) | Link: https://pikaday.dbushell.com

### TL;DR

This guide argues that most forms should avoid JavaScript calendar overlays and choose the simplest control suited to the task: native date inputs, separate day/month/year fields, selects for constrained choices, tolerant text fields, radios for available dates, or paired range inputs. Native controls bring accessibility, localization, performance, and progressive-enhancement benefits, but remain inconsistent and can fail badly for distant dates. Permanent labels, flexible parsing, timezone awareness, and user testing matter more than selecting one universal date-picker pattern.

### Comment pulse

- A mobile birth-date picker reportedly required hundreds of taps because its year control was hidden.
- Commenters favored text entry for known dates but retained calendars for travel and relative-date planning.

### LLM perspective

- View: Date entry is a task-design problem, not a widget-selection problem.
- Impact: Matching controls to user intent can improve accessibility while avoiding needless JavaScript and interaction cost.
- Watch next: Test distant dates, locale ambiguity, keyboard entry, midnight boundaries, and range selection separately.
