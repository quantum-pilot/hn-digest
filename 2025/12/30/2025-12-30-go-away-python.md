# Go away Python

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46431028) | Link: https://lorentz.app/blog-item.html?id=go-shebang

- TL;DR  
  - An opinion piece argues Python is too painful for simple scripts because of virtualenvs, pip/poetry/uv confusion, and brittle deployments, and instead recommends Go, using go run and shell stubs to approximate a scripting feel with single static binaries. Hacker News replies that uv plus PEP 723 now give Python a one-command, shebang-friendly story, but complain this arrived late and isn’t official. Others debate scripting ergonomics, reliability, and “write once, run anywhere” tradeoffs between Go and Python.

- Comment pulse  
  - uv + PEP 723 fix Python script dependency pain via shebang metadata and `uv run` managing envs → simple usage — counterpoint: discovery/docs still poor.  
  - Go lacks native shebang execution; users rely on gorun or POSIX stubs, while other languages offer -run flags or direct script execution.  
  - Many find Python’s env tooling brittle for quick tasks and move to Go for reliability; others argue every mature ecosystem accretes confusing, competing tools.

- LLM perspective  
  - View: Language ergonomics now hinge on frictionless first-run experience; install-and-run must be as simple as bash for casual users.  
  - Impact: If Go better owns 'compiled scripts' and Python fails to standardize around uv-like tooling, greenfield scripting may drift toward Go.  
  - Watch next: Watch for official Python guidance on PEP 723, uv shipping with installers, and Go exploring any lighter-weight scripting options.
