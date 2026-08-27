# Wireshark 4.6.0 Supports macOS Pktap Metadata (PID, Process Name, etc.)

- Score: 122 | [HN](https://news.ycombinator.com/item?id=45580315) | Link: https://nuxx.net/blog/2025/10/14/wireshark-4-6-0-supports-macos-pktap-metadata-pid-process-name-etc/

### TL;DR

Wireshark 4.6.0 can parse macOS `pktap` metadata, exposing the process name, PID, and related information alongside captured packets. The author demonstrates capturing one or all interfaces with `tcpdump` using a `pktap` interface and writing Pcap-ng output, then inspecting Process Information in Wireshark. Display filters can target fields such as process name or PID. This connects unexpected traffic to its originating process—and a process to its network behavior—without the earlier manual handling the author described four years ago.

### Comment pulse

- Readers noted live remote captures can be piped into Wireshark from mobile devices, containers, and SSH sessions.
- Discussion disputed claims that Wireshark is irreplaceable and pointed to commercial or custom packet-processing alternatives.

### LLM perspective

- View: Process-aware captures turn packet inspection into a faster attribution workflow on macOS.
- Impact: Developers can narrow debugging and incident triage without correlating packets to processes separately.
- Watch next: Comparable documented PID attribution workflows for Linux and Windows captures.
