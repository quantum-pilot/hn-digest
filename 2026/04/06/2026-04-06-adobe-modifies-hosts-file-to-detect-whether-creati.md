# Adobe modifies hosts file to detect whether Creative Cloud is installed

- Score: 212 | [HN](https://news.ycombinator.com/item?id=47664205) | Link: https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/

### TL;DR
Adobe’s Creative Cloud installer secretly adds entries to the Windows/macOS hosts file so adobe.com can detect if Creative Cloud is installed, working around Chrome’s local-network access restrictions. The article frames this as malware‑like DRM behavior and another example of anti‑user design. HN commenters debate how much apps should be allowed to touch system configuration, whether OSes should lock down files like hosts, and call for transparent, reversible installers, and question why security tools don’t treat this as suspicious.

### Comment pulse
- Apps must not silently edit system config like hosts → users want sandboxing, read‑only /etc, explicit per‑change consent; note iOS/Android already enforce this model.  
- Editing hosts should trigger alerts → some note Defender warns and hosts were historically app-edited—counterpoint: legacy behavior doesn’t justify covert tracking or bypassing browser security.  
- Adobe seen as persistently anti‑consumer → behavior recalls old DRM/host-file hacks; some demand installers show diff-style system changes with easy rollback.

### LLM perspective
- View: Host-file tracking is a cheap workaround that erodes trust more than it meaningfully improves user experience or security.  
- Impact: Encourages power users to block Adobe domains, seek alternatives, and lobby OS vendors for configuration and installer transparency controls.  
- Watch next: Whether regulators classify undisclosed host-file edits as unfair tracking and whether mainstream OSes start gating or logging writes.
