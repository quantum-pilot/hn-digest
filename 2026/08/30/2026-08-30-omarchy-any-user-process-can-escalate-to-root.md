# Omarchy: Any User Process Can Escalate to Root

- Score: 505 | [HN](https://news.ycombinator.com/item?id=49499854) | Link: https://0xcc.io/posts/omarchy-root-creds/

### TL;DR

A security researcher reports that Omarchy versions before 4.0.1 placed the default user in Docker’s privileged group, allowing any process in that desktop session to command the root-owned daemon. A demonstrated container mount could read the host’s protected password file, so compromise of a browser, editor, package script, or coding agent could become full root access. Omarchy removed the default membership after private disclosure. Commenters agree on Docker’s privilege model but dispute novelty, noting that many Linux guides recommend the same risky convenience.

### Comment pulse

- Defaults change the risk → knowingly enabling Docker access differs from a distribution silently granting it to every session process.
- Scope is debated → some call root escalation decisive, while others argue user-level compromise already controls most valuable desktop assets.
- Trust extends beyond one fix → prior reported shell-input handling and AI-assisted development make commenters wary of the distro’s review process.

### LLM perspective

- View: The defect is less Docker’s known behavior than converting an optional administrative capability into an unexplained system default.
- Impact: Omarchy users before 4.0.1 had a broader blast radius for ordinary application compromise.
- Watch next: Verify upgrades remove membership, audit other convenience defaults, and evaluate rootless Docker or Podman workflows.
