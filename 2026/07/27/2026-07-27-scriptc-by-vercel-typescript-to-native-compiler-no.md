# Scriptc by Vercel: TypeScript-to-Native compiler, no JavaScript engine in binary

- Score: 268 | [HN](https://news.ycombinator.com/item?id=49063175) | Link: https://github.com/vercel-labs/scriptc

## TL;DR
scriptc is Vercel’s TypeScript-to-native compiler that turns regular Node-style TypeScript into small (~180KB), fast binaries with ~2ms startup and 1–4MB RSS, without bundling a JavaScript engine by default. It statically compiles most of the language, Node APIs, and web-style `fetch`, while optionally embedding QuickJS only for dynamic pieces like `any`-heavy code or JS-only npm dependencies. Correctness is enforced via differential tests against Node and AddressSanitizer runs, aiming for JS-exact behavior with systems-language-like deployment ergonomics.

## LLM perspective
- View: Bridges JS ergonomics with systems-style deployment, making TS viable for CLIs, daemons, and serverless without full runtime heft.
- Impact: Could shift some Node projects, especially small services and tools, toward native binaries while preserving existing TS toolchains.
- Watch next: Windows/Linux maturity, real-world npm-heavy projects, benchmarks under load, and how often `--dynamic` becomes necessary in practice.
