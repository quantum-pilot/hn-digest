# I asked Meta’s Muse for its filesystem and it sent me 6.8GB

- Score: 329 | [HN](https://news.ycombinator.com/item?id=49802871) | Link: https://mouse.dev/blog/muse-runtime-export/

### TL;DR

Peter James asked Meta’s Muse to archive accessible files to Google Drive and received roughly 2.7GB compressed, 6.8GB unpacked, apparently covering his session’s Linux root filesystem. It included internal documentation, skills, runtime setup, agent logs, memory, app templates, and SSH-key files of unknown validity. He demonstrated no container escape, withheld sensitive files, and Meta marked the bounty report Not Applicable. HN readers split over whether exporting a dedicated user sandbox is a vulnerability, intended openness, or excessive exposure.

### Comment pulse

- The export reveals substantial product internals → documentation and code exposed memory, scheduling, connectors, sandboxing, app-building, and experimental device integration.
- Security impact remains unproven → the keys’ validity and reach were unknown, while boundary probing found no escape.
- Full computer access may be intentional → dedicated sandboxes empower agents — counterpoint: ordinary conversation still enabled sensitive runtime material to leave.

### LLM perspective

- View: Sandbox ownership and export boundaries need an explicit product contract, not assumptions derived from filesystem visibility.
- Impact: Users gain portability, while Meta risks disclosing implementation details or reusable credentials packaged into session images.
- Watch next: Clarify key scope, tenant isolation, export policy, file allowlists, and Meta’s Not Applicable rationale.
