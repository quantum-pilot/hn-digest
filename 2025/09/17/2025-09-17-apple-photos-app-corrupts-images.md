# Apple Photos app corrupts images

- Score: 1069 | [HN](https://news.ycombinator.com/item?id=45274277) | Link: https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/

TL;DR
- An engineer found Apple Photos sporadically corrupts images during camera import: RAW, JPEG, or both, with unchanged sizes but different checksums. After swapping cables, SD cards, laptop, and even camera, the issue persisted; disabling “delete after import” confirmed files on the SD were intact. He now imports and culls in Darktable, then exports to Photos. HN suspects a Photos import/concurrency bug and missing end‑to‑end integrity checks, and recommends safer workflows and verification before formatting to avoid data loss.

Comment pulse
- Likely Photos import race/concurrency bug → nondeterministic corruption, same size/different checksum; heavy import steps increase risk — counterpoint: OM‑1 USB quirks; try card reader/import-from-disk.
- Never delete on import → keep originals until verified backups exist; copy to local storage first; maintain multiple backups.
- Start with software changes → cheaper, faster to test alternate importers (Darktable, Olympus), then isolate hardware; randomness can appear clumpy, misleading.

LLM perspective
- View: E2E integrity on import is missing; Photos should hash source and destination and retry on mismatch.
- Impact: Photographers risk silent data loss; Apple, camera vendors, and pro apps should standardize verifiable copy protocols (checksums, FSYNC).
- Watch next: Reproductions with card readers, macOS versions, and RAW/USB matrices; open radars; community test suite comparing hashes pre/post import.
