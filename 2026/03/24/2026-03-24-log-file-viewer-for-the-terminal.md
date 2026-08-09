# Log File Viewer for the Terminal

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47498924) | Link: https://lnav.org/

### TL;DR

lnav is a serverless terminal viewer that merges, tails, searches, filters, and queries logs. It automatically detects formats, opens compressed files, exposes log data through SQLite, and claims better CPU and memory performance than standard tools on a 3.3GB access log. Long-time HN users praise its lightweight handling of web-server and lab-device logs, with a history reaching 2009. Critics found the interface, colors, initial indexing, and exit behavior confusing; the maintainer points to pager-style keys, built-in themes, extensive internal help, and improvements in newer releases.

### Comment pulse

- Local multi-file analysis avoids Grafana’s operational weight → users value automatic parsing, merging, querying, and low resource use.
- Discoverability frustrates newcomers — counterpoint: q exits, pager conventions apply, grayscale is configurable, and recent versions removed extra prompt processes.
- Some users want a TUI for structured JSON and charts → alternatives mentioned include Treewalker, vnlog, and feedgnuplot.

### LLM perspective

- **View:** lnav occupies a useful middle ground between shell primitives and centralized observability stacks.
- **Impact:** Operators can inspect small-scale or ad hoc logs without deploying centralized storage or running a service.
- **Watch next:** Indexing responsiveness, packaging consistency, structured-JSON workflows, theme defaults, current-version documentation, and large-file benchmarks.
