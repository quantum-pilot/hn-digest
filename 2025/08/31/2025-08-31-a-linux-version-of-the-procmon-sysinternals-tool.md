# A Linux version of the Procmon Sysinternals tool

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45087748) | Link: https://github.com/microsoft/ProcMon-for-Linux

### TL;DR

Microsoft’s preview release of ProcMon for Linux brings a terminal interface to system-wide syscall tracing. It can capture every process and event, filter by comma-separated process IDs or syscall names, save headless traces to a database file, and reopen saved data in its interactive view. The repository lists Ubuntu 18.04, CMake 3.14 or newer, and SQLite development libraries as build requirements. Unlike tracing one process tree with `strace`, commenters say its eBPF-based approach provides host-wide visibility without pausing each traced process.

### Comment pulse

- Readers compared it with `strace`, Sysdig, DTrace, and htop’s tracing mode; remote operation and a reportedly broken install guide drew concern.

### LLM perspective

- View: System-wide capture plus a searchable terminal view gives Linux diagnostics a useful middle ground.
- Impact: Operators can inspect broad syscall activity without first knowing which process deserves tracing.
- Watch next: Preview maturity, installation reliability, overhead, and remote workflows will determine whether it becomes a routine tool.
