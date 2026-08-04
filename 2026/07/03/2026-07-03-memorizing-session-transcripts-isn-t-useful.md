# Memorizing session transcripts isn't useful

- Score: 175 | [HN](https://news.ycombinator.com/item?id=48776232) | Link: https://12gramsofcarbon.com/p/agentics-memorizing-session-transcripts

### TL;DR

After months of SWE testing, the author found no benefit from giving coding agents searchable prior transcripts when durable context—code, documentation, commits, and PRs—was available; performance sometimes worsened. Transcripts preserve discarded branches and stale assumptions, while agents treat every retrieved token as intent and rarely delete obsolete memory. Their alternative is artifact-centered context plus human-reviewed skill updates, fewer than 20% of which are accepted. HN largely confirmed harmful context bleed, though some argued transcripts remain valuable for auditing decisions and reconstructing manual validation rather than guiding new implementation.

### Comment pulse

- Temporal confusion makes memory hazardous → obsolete facts and hypothetical questions reappear as current assumptions across unrelated tasks.
- Fresh context can restore direction → users clear failed sessions because earlier reasoning creates sticky momentum toward the same mistake.
- Transcripts still support verification → reviewers can recover unrecorded testing and surface decisions agents made without approval.

### LLM perspective

- **View:** Memory quality depends more on curation and expiration than retrieval breadth.
- **Impact:** Teams should invest in durable decision artifacts before organization-wide transcript indexes.
- **Watch next:** Benchmark artifact-only, transcript-assisted, and human-curated memory under deliberately stale or contradictory context.
