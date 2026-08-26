# Go.sum is not a lockfile

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46537095) | Link: https://words.filippo.io/gosum/

### TL;DR

The author argues that go.sum should never be parsed as a dependency graph or version lock: it maps module versions to cryptographic hashes and locally caches Go’s checksum-database guarantees. Version selection lives in go.mod, which since Go 1.17 records every build-relevant direct and transitive dependency for the main module; readonly mode prevents undeclared resolution changes. HN discussion largely exposed terminology clashes. Some readers define lockfiles by integrity hashes, while others mean selected versions. Both matter, but go.sum’s security effect is separate from go.mod’s resolution semantics.

### Comment pulse

- Resolution → Go 1.17 records selected transitive versions in the main go.mod; later requirements must update that file.
- Integrity → go.sum detects changed module contents — counterpoint: this security guarantee does not decide which version builds.
- Terminology → ecosystems conflate resolved versions, checksums, and manifests under “lockfile,” making distinct technical claims appear contradictory.

### LLM perspective

- View: Tooling should name the required property—version selection, dependency graph, or content integrity—before choosing an input file.
- Impact: Scanners parsing go.sum may overreport stale modules while misunderstanding the build’s actual constraints.
- Watch next: Better build-relevant graph tooling across platform constraints and clearer integrity-versus-resolution documentation.
