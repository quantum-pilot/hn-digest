# Linux Zoom client proactively reading everything written to X11 clipboard

- Score: 340 | [HN](https://news.ycombinator.com/item?id=49675902) | Link: https://hachyderm.io/@simontatham/117201594980991062

### TL;DR

A Linux user reports that an updated Zoom client proactively reads everything copied to the X11 clipboard, potentially exposing secrets passed through password managers. The supplied post provides no version, trace, reproduction procedure, Zoom response, or explanation of intent, so it establishes an observation rather than confirmed exfiltration. Discussion recommends using Zoom in a browser or stronger sandbox, while noting X11’s architecture lets connected clients observe input and window activity more broadly than modern per-application permission models.

### Comment pulse

- Linux needs clearer permissions → Readers wanted Android-like controls exposing each application’s granted capabilities.
- X11 weakens sandboxing → Sharing the main X server can expose clipboard, keyboard, pointer, and window data across applications.
- Browser use reduces exposure → Participants preferred the web client when its feature set is sufficient.

### LLM perspective

- View: Clipboard reads are security-relevant, but the packet does not demonstrate transmission, storage, or malicious purpose.
- Impact: Password-manager users on X11 may need isolation practices their desktop environment does not provide automatically.
- Watch next: Reproducible traces, affected versions, Wayland behavior, Zoom’s explanation, and a client update or permission change.
