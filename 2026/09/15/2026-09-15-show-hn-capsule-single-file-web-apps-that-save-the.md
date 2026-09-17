# Show HN: Capsule – Single-file web apps that save their data into SQLite

- Score: 371 | [HN](https://news.ycombinator.com/item?id=49712278) | Link: https://withcapsule.app/

### TL;DR

Capsule packages an app's HTML/CSS interface, assets, schema, and local SQLite data into one shareable file, opened by a free desktop runtime on macOS, Windows, or Linux. It targets private, offline, individually editable tools and offers AI-assisted creation; mobile support is planned. HN discussion split over whether portability justifies another runtime: supporters saw value for personal and corporate tools without hosting, while critics cited browser file APIs, synchronization limits, corruption risks in cloud folders, and established alternatives using OPFS.

### Comment pulse

- Local files already work in browsers → File System Access and OPFS support persistent apps, but sharing a self-contained artifact remains Capsule's distinction.
- Independent copies can be useful → itineraries, recipes, and corporate tools need no server, account, or shared authoritative state.
- A custom runtime adds friction → recipients must install software, updates fragment, and collaborative state becomes awkward — counterpoint: hosting brings cost and security work.

### LLM perspective

- View: Capsule is strongest as an editable document format, not as a substitute for continuously synchronized web applications.
- Impact: Individuals and restricted enterprises could distribute small stateful tools without operating infrastructure or exposing their data to a service.
- Watch next: Runtime sandboxing, file-format documentation, cloud-folder corruption handling, and mobile support will determine whether portability outweighs dependency risk.
