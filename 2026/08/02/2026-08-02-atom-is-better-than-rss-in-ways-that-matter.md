# Atom is better than RSS, in ways that matter

- Score: 129 | [HN](https://news.ycombinator.com/item?id=49138897) | Link: https://chrismorgan.info/atom%3Erss

- TL;DR
    - Argues that Atom is a technically better-designed syndication format than RSS: clearer spec, fewer ambiguities, richer markup (including HTML/code in titles), and better extensibility. Commenters mostly agree on Atom’s cleanliness but say real-world pain stems from sloppy RSS generators, not the spec alone. Several advocate JSON Feed as a simpler, reader-centric alternative, while others note that typical users can’t tell formats apart; the real battles today are over full vs partial feeds and centralized platforms vs the Fediverse.  

*Content unavailable; summarizing from title/comments.*

- Comment pulse
    - JSON Feed seems most practical: simple JSON, favicon/icon fields, no HTML in titles — counterpoint: some authors want semantic markup and emphasis in titles.  
    - Atom spec and tooling give unambiguous timestamps and encodings; RSS feeds often break from legacy, hand-rolled generators — counterpoint: blaming languages like Ruby is misguided.  
    - Readers rarely notice Atom vs RSS; pain comes from partial feeds, over-polling, and platform lock-in, reviving decentralization debates and “worse is better” history.  

- LLM perspective
    - View: Model posts and metadata once, then serialize to Atom/RSS/JSON Feed; argue about structure, not wire format.  
    - Impact: Fewer parser edge-cases, easier cross-posting into ActivityPub or email, and more resilient archives independent of any single reader ecosystem.  
    - Watch next: CMS plugins that emit validated feed types by default, and Fediverse bridges that subscribe to legacy feeds seamlessly.
