# Beets: The music geek’s media organizer

- Score: 237 | [HN](https://news.ycombinator.com/item?id=45873037) | Link: https://beets.io/

- TL;DR
  - Beets is an open-source, plugin-driven music library manager that tags, reorganizes, and serves collections using MusicBrainz/Discogs data, with tools for art, lyrics, replaygain, transcoding, duplicates, and a web UI. HN users praise it for automating Bandcamp and CD imports and syncing to streamers, often pairing with Picard. Friction appears with nonstandard material—live sets, fan edits, personal recordings, festivals—because beets assumes a canonical release model. Some submit missing releases to MusicBrainz; others prefer bespoke metadata. Genre tagging sparked debate; classical remains hard.

- Comment pulse
  - Release-centric model suits commercial releases; unique edits/live recordings/festivals clash. Workarounds: submit to MusicBrainz or tag manually — counterpoint: personal metadata needn’t live in a database.
  - Plugins/workflows smooth imports: Bandcamp autotagger, beets-flask pipelines, beets-alternatives for synced views; Picard helps when automatic matching fails.
  - Genres polarize: some strip them; others use multi-genre taxonomies for discovery. Classical tagging remains tricky despite improvements and specialized apps.

- LLM perspective
  - View: Treat beets as ETL for audio: ingest, normalize via external IDs, then materialize your canonical folder structure.
  - Impact: Strong for libraries aligned to release identifiers; for custom edits, maintain a parallel 'personal cut' namespace or excluded paths.
  - Watch next: Richer importers for festivals/mixes, batch tools to scaffold new MusicBrainz entries, and genre/classical schemas that survive across players and streamers.
