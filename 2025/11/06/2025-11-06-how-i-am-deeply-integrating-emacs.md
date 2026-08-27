# How I am deeply integrating Emacs

- Score: 201 | [HN](https://news.ycombinator.com/item?id=45832341) | Link: https://joshblais.com/blog/how-i-am-deeply-integrating-emacs/

### TL;DR

An Emacs user describes making the editor a daily computing environment under Hyprland and Wayland without adopting EXWM, whose X11 dependence and exposure to single-threaded hangs were deal-breakers. A custom Go launcher targets the running Emacs instance and, the author claims, makes common actions ten times faster. Global shortcuts expose terminals, search, passwords, SSH, notes, calendars, email, feeds, music, files, and external text editing. The design centers on one programmable interface while preserving a separate window manager.

### Comment pulse

- Supporters emphasized plain text, programmable workflows, and durable personal tooling; skeptics questioned whether tool depth substitutes for motivation.
- Accessibility and mobile capture remain important boundaries, despite examples involving Emacspeak and alternate capture workflows.

### LLM perspective

- View: The launcher is the real integration layer; Emacs becomes a service behind consistent global actions.
- Impact: Frequent workflows gain coherence, but maintenance and accessibility costs move onto the user.
- Watch next: Whether the setup remains resilient when Emacs blocks or Wayland integrations change.
