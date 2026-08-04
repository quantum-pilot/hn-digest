# Late.sh – a command-line Clubhouse for computer people

- Score: 306 | [HN](https://news.ycombinator.com/item?id=49001127) | Link: https://late.sh/

### TL;DR

Late.sh is a terminal-based social clubhouse reached with a normal SSH client. It combines live chat, radio, games, shared ASCII art, news, challenges, and work profiles; an optional companion adds local audio, voice rooms, YouTube, and image pasting. Identity comes from an SSH-key fingerprint rather than passwords or OAuth, with a documented throwaway-key option. Hacker News liked the nostalgic, low-friction format but flagged default usernames, unpublished host-key verification, and a curl-to-shell installer as security and consent pitfalls.

### Comment pulse

- Username privacy needs explicit warning → SSH may expose a work machine’s full-name account — counterpoint: choose a pseudonymous user and disposable key.
- Operational trust needs work → users requested a published host fingerprint and objected to curl-to-shell installation despite source-inspection alternatives.
- The concept rekindles old-web community appeal → SSH-only access, selectable themes, and shared spaces recalled tilde communities without browser-platform overhead.

### LLM perspective

- **View:** SSH is the product’s differentiator and its sharp edge: familiar protocol defaults become visible social-account decisions.
- **Impact:** Terminal-native communities gain an unusually portable interface, while maintainers inherit identity, moderation, persistence, and client-security responsibilities.
- **Watch next:** Publish host-key fingerprints, clarify username derivation before login, harden installer guidance, and test planned screen sharing across platforms.
