# Find SF parking cops

- Score: 496 | [HN](https://news.ycombinator.com/item?id=45350690) | Link: https://walzr.com/sf-parking/

### TL;DR

A project reverse-engineered San Francisco’s public parking-ticket system to display each officer’s most recent citation location and a leaderboard in near real time. The data source was cut off within hours, leaving only a snapshot. Commenters inferred that the seemingly irregular citation-number sequence was probably a modulo-7 check-digit scheme rather than arbitrary numbering. They praised the interface and investigative creativity, while the rapid shutdown demonstrated how enumerable public records can enable live personnel tracking beyond their intended administrative use.

### Comment pulse

- Citation IDs were predictable → a check digit appears to turn simple sequential records into the observed increment pattern.
- SFMTA reacted unusually quickly → the underlying data source stopped working only hours after launch.

### LLM perspective

- View: Public record lookup becomes operational surveillance when identifiers are enumerable and updates expose worker locations.
- Impact: Agencies must balance transparency with aggregation risks that individual record pages do not make obvious.
- Watch next: Examine whether SFMTA added rate limits, authentication, delayed publication, or non-sequential identifiers.
