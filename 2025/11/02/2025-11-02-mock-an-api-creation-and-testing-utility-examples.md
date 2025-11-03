# Mock – An API creation and testing utility: Examples

- Score: 111 | [HN](https://news.ycombinator.com/item?id=45789556) | Link: https://dhuan.github.io/mock/latest/examples.html

- TL;DR
  - Mock is a CLI tool to create/test HTTP APIs by wiring routes to shell scripts or other interpreters. Examples show per-endpoint delays via middleware, polyglot endpoints (Node/Python/PHP), a stateful counter using temp files, and a minimal CRUD using jq. Dynamic behavior comes from helpers like get-payload, get-query, and route params. HN discussion highlights its language-agnostic, single-binary appeal for CI, acknowledges overlap with tools like WireMock, notes a naming collision with RPM’s “mock,” and includes general praise.

- Comment pulse
  - Why this vs WireMock? → Single static binary, no JVM; shell handlers allow quick dynamic responses — counterpoint: existing language-specific tools may already suffice.
  - Dynamic responses are easy → Built-ins extract body/params (get-payload, get-query), pass to scripts, then mock write outputs.
  - Name concern → “mock” collides with RPM’s tool; author concedes the name isn’t unique.

- LLM perspective
  - View: Unixy, polyglot mock server emphasizing shell composition; great for fast prototyping and CI sandboxes.
  - Impact: Reduces setup for teams avoiding Java/Node stacks; benefits DevOps/SREs fluent with POSIX tools.
  - Watch next: Windows/PowerShell parity, sandboxing for exec, record–replay and assertions, a concise config format.
