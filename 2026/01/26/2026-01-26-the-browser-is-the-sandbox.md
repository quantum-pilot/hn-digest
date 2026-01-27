# The browser is the sandbox

- Score: 327 | [HN](https://news.ycombinator.com/item?id=46762150) | Link: https://simonwillison.net/2026/Jan/25/the-browser-is-the-sandbox/

- TL;DR  
  - Paul Kinlan argues the web browser is already a battle-tested sandbox for AI agents and LLM-generated code. His Co-do demo runs an agent entirely in-browser: limited filesystem access, constrained network calls via CSP and sandboxed iframes (including a double-iframe trick), and isolated execution via WebAssembly in Web Workers. Simon Willison highlights this as an alternative to heavy local containers like Claude Cowork, and HN expands the discussion to browser extensions, OS-level sandboxes, and the limits of current web APIs and browser support.

- Comment pulse  
  - Browser/extension sandboxes suit LLM-generated code; when agents must touch real CLIs/files, people add OS-level supervisors like Vallignus to enforce policies.  
  - New web APIs enabling directory-level AI workflows feel transformative—counterpoint: long-running chains, native UI advantages, and partial browser support still block “first-class” status.  
  - Traditional Unix permissions/systemd are seen as too coarse for untrusted AI tools; limited-user schemes help, but kernel vulns and unrestricted networking remain problems.

- LLM perspective  
  - View: Browser sandboxes are ideal for many “local agent” use cases that don’t truly require OS-level privileges.  
  - Impact: If standardized across browsers, these patterns could normalize secure, install-free dev tools and editors powered by remote LLMs.  
  - Watch next: Comparative security/usability studies of browser, container, and OS-user sandboxes for autonomous agents under realistic attack and failure scenarios.
