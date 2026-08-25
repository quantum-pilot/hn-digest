# Show HN: Whosthere: A LAN discovery tool with a modern TUI, written in Go

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46731432) | Link: https://github.com/ramonvermeulen/whosthere

### TL;DR

Whosthere is a Go terminal application for discovering local-network devices without elevated privileges. It concurrently queries mDNS and SSDP, triggers ARP resolution through TCP and UDP connection attempts, reads the cache, and adds manufacturer data. The interface supports search, device details, optional port scans, themes, and YAML configuration; daemon mode exposes device and health data through a small HTTP API. It supports Linux and macOS, installs through Homebrew or Go, limits networks to /16, and warns users to scan only networks they are authorized to inspect.

### Comment pulse

- Existing scanners set a baseline → Nmap handles quick rootless discovery, while Whosthere adds a persistent interface and API.
- Hostname resolution trails alternatives → one network found 54 names versus 75–80, motivating reverse-DNS improvements.
- Monitoring would expand utility → commenters want arrival logs for basic intrusion detection plus configurable interfaces and scan cadence.

### LLM perspective

- View: Its value is approachable aggregation and workflow, not novel discovery protocols.
- Impact: Home administrators gain unprivileged inventory and integration without memorizing several scanner commands.
- Watch next: Reverse DNS, arrival history, cadence controls, interface selection, Windows support, and Wayland clipboard.
