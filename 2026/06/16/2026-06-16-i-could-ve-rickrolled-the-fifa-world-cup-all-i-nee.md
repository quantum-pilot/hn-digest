# I Could've Rickrolled the FIFA World Cup. All I Needed Was My ID

- Score: 260 | [HN](https://news.ycombinator.com/item?id=48550936) | Link: https://bobdahacker.com/blog/fifa-hack

### TL;DR

A public FIFA agent registration added the researcher to FIFA’s shared Microsoft Entra tenant. Clients displayed NO_ROLES, but backend APIs failed to enforce authorization, exposing live match previews, RTMP ingest URLs and stream keys, broadcast controls, statistics, editorial systems, and files. The researcher did not attempt takeover, yet warned an attacker could disrupt or inject feeds and alter data. After unanswered outreach, the researcher escalated through MediaKind, CISA, and FBI contacts; server-side 403 checks appeared next day. HN praised the finding but questioned takeover certainty and apparent AI-assisted prose.

### Comment pulse

- Impact was serious but bounded by uncertainty → competing RTMP publishers might cause glitches, and live directors could cut suspicious feeds quickly.
- Disclosure channels failed the researcher → no security.txt, bounty, or responsive FIFA contact forced costly, stressful escalation during live matches.
- AI-shaped presentation divided readers → critics said formulaic prose undermined trust — counterpoint: others found the human-edited story clear, useful, and engaging.

### LLM perspective

- **View:** Authentication created the blast radius; missing backend authorization converted one legitimate external identity into organization-wide access.
- **Impact:** Broadcasters, sports platforms, and SaaS tenants need deny-by-default APIs, tenant segmentation, and tested role enforcement.
- **Watch next:** Audit every shared-tenant application, rotate exposed keys, review logs, remove distribution access, and publish a coordinated disclosure policy.
