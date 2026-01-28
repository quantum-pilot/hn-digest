# I made my own Git

- Score: 318 | [HN](https://news.ycombinator.com/item?id=46778341) | Link: https://tonystr.net/blog/git_immitation

### TL;DR
- An engineer implemented a minimalist Git-like system (in Rust) to understand Git’s internals: blobs, trees, commits, object IDs, and plumbing commands.  
- The writeup demystifies how content-addressed storage and simple data structures compose into branches, history, and common Git operations.  
- HN readers treat it mainly as an educational piece: they discuss Git’s underrated recursive merge/rerere features, recommend other “understand Git from the inside” resources, and debate AI models quietly training on such hobby repos.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Git’s recursive merge and rerere → remembers past conflict resolutions, making merges safer and more repeatable—counterpoint: many teams still prefer linear, rebased histories despite this.
- DIY Git projects → great way to grok internals; readers share complementary resources and tools, from Git From the Bottom Up to CodeCrafters-style “build your own Git” challenges.
- LLM training on public repos → small personal projects get mass-cloned by bots, raising concerns about circular training, authors’ intent, and potential “poisoning” of future models.

---

### LLM perspective
- View: Hands-on reimplementations of core tools will increasingly double as training fodder and as meta-examples of “agent-style” planning.
- Impact: Tool authors, educators, and open-source hobbyists unintentionally shape coding model behaviors and norms through these small, didactic repos.
- Watch next: Explicit opt-outs/labels for training data, benchmarks on model self-contamination, and more principled VCS experiments (e.g., first-class conflicts, non-code diffing).
