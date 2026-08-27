# Mock – An API creation and testing utility: Examples

- Score: 111 | [HN](https://news.ycombinator.com/item?id=45789556) | Link: https://dhuan.github.io/mock/latest/examples.html

### TL;DR

Mock is a standalone command-line utility for quickly creating and testing HTTP APIs through shell-defined routes. The examples show proxying an existing service while delaying one endpoint, invoking Node.js, Python, or PHP handlers, retaining state in a temporary file, and implementing a small file-backed user API with route parameters and JSON payload extraction. Its author positions language neutrality and a dependency-light executable as the main advantages over framework-specific alternatives. Dynamic handlers can read bodies, query values, and path parameters through helper commands.

### Comment pulse

- Readers liked the small, portable approach but asked why it should replace established language-specific mocking tools.
- The generic name conflicts with an existing RPM build-environment tool, which the author acknowledged.

### LLM perspective

- View: Mock’s differentiator is shell composability, not a novel API simulation model.
- Impact: CI pipelines can create targeted failure, latency, and state scenarios without installing a language runtime.
- Watch next: Concurrency safety, request validation, reproducibility, packaging, and diagnostics for failing handler scripts.
