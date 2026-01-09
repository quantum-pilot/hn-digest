# Go.sum is not a lockfile

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46537095) | Link: https://words.filippo.io/gosum/

### TL;DR
Go’s `go.sum` file is not a lockfile and should not be used to infer dependency graphs or “what version was built.” It’s only a local cache of cryptographic hashes used to verify module contents against the Go Checksum Database; it has no influence on version resolution. Since Go 1.17, `go.mod` plays both roles—manifest and lockfile—by listing all direct and transitive dependencies and the exact versions used when that module is the main module. HN debates whether this really matches lockfile semantics and how it interacts with real‑world, semver‑breaking libraries.

---

### Comment pulse
- `go.mod` as precise build spec → With Go ≥1.17 and `-mod=readonly`, MVS happens when updating `go.mod`, so it encodes the actual chosen versions, not just minima.
- Unused packages and bad semver → “Gigantic” cloud SDKs drag fragile transitive deps that still influence version selection; some devs resort to vendoring or splitting binaries to contain damage.
- What is a lockfile? → Some insist hashes are essential; Go offloads that to the checksum DB + `go.sum`, worrying CI users who want hash-pinning — counterpoint: proxy + sums already block tag tampering.

---

### LLM perspective
- View: Treat `go.mod` as the authoritative dependency graph; reserve `go.sum` purely for integrity checks and tooling that talks to the checksum DB.
- Impact: Security and SRE teams should pivot scanners and SBOM tooling to `go.mod` parsing instead of mining `go.sum`.
- Watch next: Better docs and examples around MVS, `-mod` modes, and CI workflows that guarantee reproducible builds without overloading `go.sum`.
