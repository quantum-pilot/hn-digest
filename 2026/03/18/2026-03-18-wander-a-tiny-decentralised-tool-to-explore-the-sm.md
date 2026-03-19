# Wander – A tiny, decentralised tool to explore the small web

- Score: 181 | [HN](https://news.ycombinator.com/item?id=47422759) | Link: https://susam.net/wander/

### TL;DR
Wander is a tiny, fully client-side “stumble” tool for the small web. You drop two files (index.html + wander.js) into a /wander/ directory, then curate links to pages and other Wander consoles. The JS console recursively fetches other consoles’ wander.js files, creating a decentralized, transitive discovery graph—like a webring crossed with StumbleUpon, but with no central service, server, or database. HN discussion focuses on serendipitous discovery, possible UX pitfalls, and how this differs from a basic random blogroll.

---

### Comment pulse
- Decentralized StumbleUpon-style discovery → each console links to sites and other consoles; the JS walks this graph for recursive, serendipitous recommendations.  
- Concern: consoles that don’t link outward can “trap” users → suggested fix: keep a session-wide set of discovered consoles and choose randomly from that.  
- Distinct from a random link page → guarantees every console has recommendations and exposes neighbours’ curated lists, enabling consistent transitive exploration.

---

### LLM perspective
- View: This is a minimal protocol-in-practice; conventions in wander.js effectively define the network’s behavior.  
- Impact: Personal-site owners get a low-friction way to share audiences without central platforms or logins.  
- Watch next: Tools to visualize the Wander graph, detect dead links, and optionally score consoles by activity or reciprocity.
