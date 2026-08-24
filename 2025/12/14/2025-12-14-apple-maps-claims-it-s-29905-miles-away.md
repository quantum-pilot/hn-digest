# Apple Maps claims it's 29,905 miles away

- Score: 142 | [HN](https://news.ycombinator.com/item?id=46262950) | Link: https://mathstodon.xyz/@dpiponi/115651419771418748

### TL;DR

Apple Maps displayed a moving item near Guatemala City as 29,905 miles away, farther than Earth’s circumference, while its directions implied implausible travel speed. Commenters identified the item as a lost AirTag, but the supplied material does not establish the calculation’s cause. Suggestions included accumulated route estimates, a closed-road penalty accidentally treated as distance, or altitude-related data. The author framed the screenshot as an argument for estimation questions in interviews; commenters disputed whether such screening would prevent an implementation bug.

### Comment pulse

- Distance explanations remained speculation; several readers favored a routing sentinel or penalty leaking into the displayed total.
- Tesla ferry and Volvo mountain-road anecdotes showed another failure class: navigation software rejecting valid GPS after its internal model diverges.
- Readers agreed the number deserved a sanity check — counterpoint: Fermi questions test estimation, not necessarily defensive implementation.

### LLM perspective

- View: The striking defect is not an uncertain position but an impossible distance reaching the interface unchecked.
- Impact: Navigation products need plausibility bounds and transparent handling when sensor data conflicts with route models.
- Watch next: Whether Apple corrects the display and explains which calculation produced the value.
