# JMAP for Calendars, Contacts and Files Now in Stalwart

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45672336) | Link: https://stalw.art/blog/jmap-collaboration/

- TL;DR
  - Stalwart ships the first full JMAP collaboration server: calendars, contacts, files, and sharing, plus JSON‑native JSCalendar/JSContact—aimed to replace XML‑heavy CalDAV/CardDAV/WebDAV with one HTTPS/JSON API. The goal: simpler interop versus fragmented DAV/iCalendar/vCard stacks. Client support is early but growing (Mailtemi, Parula, OpenCloud); Stalwart targets 1.0 after performance and schema work. HN debates bootstrapping clients (IMAP→JMAP bridges), standard maturity and vendor buy‑in (Mozilla, Fastmail), and protocol choices: HTTP/JSON practicality and compression versus potential efficiency of binary alternatives.

- Comment pulse
  - Bridge IMAP to JMAP to jumpstart clients → reuse existing mailboxes, expose a clean API, avoid chicken‑and‑egg adoption.
  - Adoption hinges on clients and vendors → Mozilla plans JMAP; Fastmail hasn’t shipped calendars/contacts; Calendars/FileNode drafts still maturing — counterpoint: server-first unlocks serious client work.
  - HTTP/JSON is “good enough” → web compatibility, HTTP/3 binary framing, strong compression; skeptics prefer DER/CBOR or non-HTTP stacks for efficiency.

- LLM perspective
  - View: Unifying groupware on JMAP reduces protocol sprawl; bridges can smooth migration from DAV and IMAP.
  - Impact: Ecosystem shift if Thunderbird/Mozilla and Fastmail ship full JMAP; client SDKs and mobile apps follow.
  - Watch next: RFCs for Calendars/FileNode, performance benchmarks, interop plugfests, and practical IMAP/DAV→JMAP gateways.
