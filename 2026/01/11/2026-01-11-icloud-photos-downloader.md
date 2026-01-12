# iCloud Photos Downloader

- Score: 261 | [HN](https://news.ycombinator.com/item?id=46578921) | Link: https://github.com/icloud-photos-downloader/icloud_photos_downloader

### TL;DR
iCloud Photos Downloader is a cross‑platform, MIT‑licensed command‑line tool that lets you bulk download and continuously sync your iCloud Photos library to local storage (Linux/Windows/macOS, including NAS). It supports Live Photos, RAW, de‑duplication, metadata fixing, and multiple operating modes (copy/sync/move with optional watching). It relies on Apple’s web APIs, so you must allow web access and turn off Advanced Data Protection. HN discussion centers on how hard “true” Photos backups are and Apple’s weak official export options.

---

### Comment pulse
- Full‑fidelity backups are hard → Photos stores albums, edits, Live/burst relationships, and adjusted dates outside files; most tools flatten this. Photos Backup Anywhere tries full round‑trip fidelity.  
- Many dislike iCloud for Windows and flaky third‑party apps → some bypass iCloud entirely using usbmuxd/ifuse to pull originals directly over USB and free phone space.  
- “No official way to download everything” → critics see this as lock‑in; others note macOS export‑originals and EU‑wide Apple data exports as partial remedies — counterpoint: both are clunky.  

---

### LLM perspective
- View: This tool is infrastructure for escaping or hedging against Apple’s Photos lock‑in while still using the service day‑to‑day.  
- Impact: Most useful for large libraries, NAS users, Windows desktops, and cautious families wanting independent archives beyond Apple’s control.  
- Watch next: ADP‑compatible methods, verification of restored libraries against Photos’ metadata, and sustainable maintenance/governance for such critical backup tools.
