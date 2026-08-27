# Disable AI in Firefox

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45696752) | Link: https://flamedfury.com/posts/disable-ai-in-firefox/

### TL;DR

A personal guide says Firefox users can set `browser.ml.enable` to false in `about:config` as a broad switch for machine-learning features, or disable individual controls for chatbots, link previews, extension APIs, page assistance, and smart tab grouping. The author dislikes distracting prompts but is still testing tab grouping. Commenters noted that the master switch may also remove useful on-device translation or PDF accessibility features, and that internal preferences can change between versions. This is version-specific community guidance, not an official compatibility promise.

### Comment pulse

- Control preference → users want one clear opt-out from unsolicited browser features.
- Collateral-cost concern → a blanket switch may disable private, local features that some users value.
- Maintenance caveat → internal configuration names may move or disappear across Firefox releases.

### LLM perspective

- View: Granular controls better separate objections to remote assistants from useful local inference.
- Impact: A master toggle favors simplicity but shifts feature discovery and accessibility tradeoffs onto users.
- Watch next: Mozilla’s official controls, preference stability, and clearer labeling of local versus networked processing.
