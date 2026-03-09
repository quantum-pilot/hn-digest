# Warn about PyPy being unmaintained

- Score: 295 | [HN](https://news.ycombinator.com/item?id=47293415) | Link: https://github.com/astral-sh/uv/pull/17643

- TL;DR  
  A uv pull request adds documentation warning that PyPy is “not actively developed anymore” and only supports Python up to 3.11, based on a PyPy maintainer’s comment in a NumPy issue. PyPy core devs say the project is still maintained (bug fixes, some JIT work) but lacks capacity to track CPython’s rapid evolution and needs contributors and funding, especially for 3.12. HN discusses wording (“unmaintained” vs “not active”), PyPy’s impressive speed, painful compatibility gaps, and Python ecosystem politics.

- Comment pulse  
  PyPy needs help → core devs invite code and financial support; commenters note weak donation UX and suggest public benchmarks to showcase real-world performance.  
  Project status nuance → maintainers fix bugs but lag CPython; many see “not actively developed” as accurate yet softer than “unmaintained”.  
  Great but tricky in practice → users praise 5× speed and long-term production use, but others hit subtle incompatibilities (C-API, GC behavior), making PyPy risky for large CPython-based stacks.

- LLM perspective  
  View: This is about honestly signaling project health without prematurely declaring a volunteer runtime “dead.”  
  Impact: Tooling like uv will influence which runtimes ecosystems treat as first-class and which quietly atrophy.  
  Watch next: Whether PyPy lands stable 3.12, improves fundraising/messaging, and if uv/docs update their stance accordingly.
