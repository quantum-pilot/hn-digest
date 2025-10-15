# Wireshark 4.6.0 Supports macOS Pktap Metadata (PID, Process Name, etc.)

- Score: 122 | [HN](https://news.ycombinator.com/item?id=45580315) | Link: https://nuxx.net/blog/2025/10/14/wireshark-4-6-0-supports-macos-pktap-metadata-pid-process-name-etc/

- TL;DR
    - Wireshark 4.6.0 now parses macOS pktap metadata, exposing per-packet process name, PID, etc., when you capture to pcapng via tcpdump -i pktap,... You can filter in Wireshark using frame.darwin.process_info.* to pinpoint which app generated traffic. HN reactions: appreciation tempered by reminders that pktap has existed for years and power users often rely on alternatives or custom pipelines. Tips included remote live captures (Android/iOS or piping tcpdump over SSH). Windows analogs point to ETW/pktmon, but end-to-end Wireshark workflows remain fuzzy.

- Comment pulse
    - Wireshark is irreplaceable → pushback: OmniPeek and custom pipelines exist; power users outgrow GUI — counterpoint: ubiquity and ease still matter.
    - Remote capture tips → pipe tcpdump over SSH to a FIFO for live viewing; Android/iOS can act as capture devices.
    - Windows/Linux per-process attribution → Windows: ETW input exists; current workflow uses pktmon + Network Monitor; Wireshark how-to unclear for PIDs.

- LLM perspective
    - View: First-class process-level context in captures sharpens triage and attribution on macOS without custom scripts.
    - Impact: DFIR, SREs, and developers can rapidly map suspicious flows to apps; fewer repro steps and guesswork.
    - Watch next: Windows parity via ETW in Wireshark, Linux eBPF exporting proc metadata to pcapng, and streamlined remote-capture UX.
