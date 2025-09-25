# Python on the Edge: Fast, sandboxed, and powered by WebAssembly

- Score: 195 | [HN](https://news.ycombinator.com/item?id=45362023) | Link: https://wasmer.io/posts/python-on-the-edge-powered-by-webassembly

- TL;DR
  - Wasmer Edge (beta) now runs unmodified CPython on WASIX with dynamic linking, libffi, threads, sockets, and a curated index of precompiled native packages. It demos FastAPI/Django/Streamlit/ffmpeg and benchmarks near-native on pystone, with a first-run compile delay and faster paths promised. Compared to Cloudflare’s Pyodide and AWS Lambda, it claims broader compatibility, websockets, and faster cold starts. HN testers confirmed a WASM Python 3.12 shell (needs Wasmer v6.1.0-rc.5), asked about numpy/scipy, outbound networking/scheduling, JS interop, and sandboxed user scripts; FFI seen as critical.

- Comment pulse
  - Works as advertised → brew install wasmer; got a WASM CPython 3.12 REPL; requires Wasmer v6.1.0‑rc.5.— counterpoint: why not just use containers?
  - C-extensions matter → libffi + dynamic linking target numpy/scipy; Pyodide exists but lacks threads/sockets; performance vs Pyodide still unclear from benchmarks.
  - Sandboxed scripting at edge → feasible for user-supplied transforms with network access; ASGI implies FastHTML works; scheduling semantics raised as an open question.

- LLM perspective
  - View: Real CPython with C-extensions on WASM reduces shims and broadens edge workloads beyond browser-oriented Pyodide constraints.
  - Impact: Safer plugin execution, low-latency APIs, and easier portability for frameworks needing sockets, threads, or native deps.
  - Watch next: Publish real-world benchmarks, numpy/scipy/polars/PyTorch status, cold-start numbers, Wasmer‑JS release, outbound networking limits, pricing, and persistence/DB story.
