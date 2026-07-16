# TS-2026-009: Insecure argument handling in Tailscale SSH permitted root access

- Score: 210 | [HN](https://news.ycombinator.com/item?id=48915004) | Link: https://tailscale.com/security-bulletins

### TL;DR
In Tailscale SSH on Linux, a username beginning with `-` (e.g., `-i`) was passed to the `getent` CLI, which treated it as a flag and printed `/etc/passwd` starting with `root`. Tailscale then opened an interactive root session, bypassing ACLs such as `autogroup:nonroot`. Version 1.98.9 now rejects dash‑prefixed and numeric-only usernames and fixes related ACL/root bypasses. HN discussion centers on only using Tailscale as a VPN, preferring OpenSSH, and criticizing shell-based argument handling.

### Comment pulse
- Operate Tailscale only on hardened bastions as a VPN, avoid advanced features like SSH; distrust unaudited code and backlog—counterpoint: all software hides vulnerabilities, hence defense-in-depth.  
- Many prefer OpenSSH’s long security record and public-key or cert-based auth; some note Tailscale’s bug required existing tailnet access, unlike exposed Internet SSH.  
- Engineers decry passing usernames to getent as a subprocess; urge using getpwnam-style APIs, seeing the dash-username ban as a band‑aid on poor design.  

### LLM perspective
- View: Feature-rich security products should default to minimal, battle-tested components; every added convenience endpoint widens the potential attack surface.  
- Impact: Expect security-conscious teams to keep Tailscale as transport only, centralizing SSH and auth on traditional bastions and OpenSSH.  
- Watch next: Look for formal audits, more fuzzing around argument parsing, and migration from shelling out to direct OS APIs.
