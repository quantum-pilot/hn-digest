# Self-updating screenshots

- Score: 457 | [HN](https://news.ycombinator.com/item?id=47908051) | Link: https://interblah.net/self-updating-screenshots

### TL;DR

Jelly’s help-center build now generates screenshots directly from the running Rails application. Special comments embedded in Markdown specify a demo-team route, capture mode, CSS selector, and optional clicks, waits, cropping, hiding, or torn-edge styling; a Rake task drives headless Chrome through Capybara and Cuprite, reuses logins, writes images, and renders the help pages. This keeps UI imagery synchronized with feature changes and lowers documentation friction. Hacker News shared similar Nix, Android-emulator, theme-aware, and Fastlane workflows, while warning that fresh screenshots can conceal stale prose when labels or navigation change.

### Comment pulse

- Automated light and dark variants can use picture elements with color preferences, including inside GitHub READMEs.
- Ephemeral emulators make mobile capture reproducible and eliminate setup residue; app-store automation also scales across screen sizes and localizations.
- Updated pixels do not validate instructions — counterpoint: lower capture friction makes simultaneous prose edits more likely.

### LLM perspective

- **View:** Treat screenshots as build artifacts derived from controlled application state, not hand-maintained assets.
- **Impact:** Product teams can update visual guides within feature pull requests instead of scheduling manual recapture.
- **Watch next:** Text-label assertions, deterministic demo data, animation stabilization, visual diffs, localization, and accessibility coverage.
