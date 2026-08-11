# Warn about PyPy being unmaintained

- Score: 295 | [HN](https://news.ycombinator.com/item?id=47293415) | Link: https://github.com/astral-sh/uv/pull/17643

### TL;DR

uv merged documentation warning that PyPy is no longer actively developed and supports only through Python 3.11, based on a NumPy discussion rather than an official project announcement. After it reached HN, maintainers clarified that PyPy is not unmaintained: bugs are fixed, the JIT still improves occasionally, and a new contributor is pursuing Python 3.12, but the small team cannot track CPython's pace. uv softened the pull-request title; another PyPy core developer nevertheless called the documentation fair until releases resume. The thread became a call for contributors and funding.

### Comment pulse

- PyPy still delivers exceptional CPU-bound speed; users report fivefold gains and decade-long production deployments where compatibility permits.
- Ecosystem fit limits adoption: C-extension-heavy libraries, CPython assumptions, and different garbage-collection behavior make migrations fail beyond benchmarks.
- Naming amplifies confusion: PyPy is an alternative interpreter; PyPI is the maintained package index, and uv interacts with both.

### LLM perspective

- **View:** “Unmaintained” is inaccurate; “capacity-constrained and lagging compatibility” describes the evidence more precisely.
- **Impact:** Users need explicit version and ecosystem caveats; maintainers need contributors more than premature deprecation.
- **Watch next:** Python 3.12 progress, maintenance releases, NumPy support, funding, commit cadence, and uv's note.
