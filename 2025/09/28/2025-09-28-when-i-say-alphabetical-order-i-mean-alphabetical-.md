# When I say “alphabetical order”, I mean “alphabetical order”

- Score: 313 | [HN](https://news.ycombinator.com/item?id=45404022) | Link: https://sebastiano.tronto.net/blog/2025-09-28-alphabetic-order/

- TL;DR
    - A hiker merged photos from two Android phones named IMG_YYYYMMDD_HHmmss[…]. GUI file managers (Windows, Google Drive, KDE, GNOME) sorted them “by name” using natural sorting (numbers by value), not strict lexicographic order—misordering shots because one phone appended milliseconds directly while the other separated them with an underscore. The shell’s ls showed the expected lexicographic order. HN argues natural sort matches most users’ intent (e.g., versions/chapters), but surprises developers and has edge cases. Consensus: keep natural sort as default, but label it clearly and offer a toggle.

- Comment pulse
    - Natural sort as default → mirrors human expectation; avoids ugly leading zeros; great for versions/chapters — counterpoint: harms hash/ID scanning and dev workflows.
    - Edge cases critique → numbers have decimals, separators, locales; “smart” parsing becomes brittle and inconsistent across systems.
    - UX fix → expose “Natural” vs “Strict lexicographic” sorts; make labels explicit; easy per-app/OS toggle.

- LLM perspective
    - View: Default to natural sort, but make behavior explicit and configurable; avoid surprise.
    - Impact: File managers/cloud drives unify terminology; developers, photographers, archivists adjust naming or settings.
    - Watch next: OS-level sort setting propagated to apps; test suites for mixed tokens; camera apps standardize filename patterns.
