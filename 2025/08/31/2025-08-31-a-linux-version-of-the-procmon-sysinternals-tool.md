# A Linux version of the Procmon Sysinternals tool

- Score: 166 | [HN](https://news.ycombinator.com/item?id=45087748) | Link: https://github.com/microsoft/ProcMon-for-Linux

TL;DR
- Microsoft’s Procmon-for-Linux reimagines Sysinternals Process Monitor using eBPF to trace syscalls across the whole host. It filters by PIDs and events, runs headless to write an SQLite trace (procmon.db), and includes a TUI viewer. Compared with strace/htop+strace, it doesn’t stop processes per syscall and can capture many processes with lower overhead. HN debates overlap with sysdig/dtrace and asks about Windows log compatibility and remote use; output is SQLite, compatibility unclear. Some report INSTALL issues; project is still a preview.

Comment pulse
- System-wide eBPF tracing > strace-per-PID → avoids stopping processes; scales to many processes with less slowdown.
- Existing tools (sysdig, dtrace, htop+strace) suffice → similar telemetry and mature workflows — counterpoint: Procmon’s TUI/filters ease adoption for Sysinternals users.
- Wants: remote capture and Windows-log compatibility → better integration with procdot; unclear today, output is SQLite; also reports of INSTALL.md not working.

LLM perspective
- View: Useful bridge for Windows admins; eBPF architecture gives Linux-native performance; value depends on stability and ecosystem integration.
- Impact: Could simplify incident triage and malware forensics on Linux; less friction switching between Windows and Linux workflows.
- Watch next: Confirm Windows PML/CSV export, remote capture, and container/namespace filtering; measure overhead versus strace/sysdig on busy hosts.
