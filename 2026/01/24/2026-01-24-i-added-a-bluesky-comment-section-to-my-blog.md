# I added a Bluesky comment section to my blog

- Score: 188 | [HN](https://news.ycombinator.com/item?id=46747366) | Link: https://micahcantor.com/blog/bluesky-comment-section.html

## TL;DR

Author explains how they added a read-only, Bluesky-powered comment section to a static, React/MDX blog without running their own backend. Each article stores a Bluesky post ID in metadata; on load, the site fetches that post’s reply thread via Bluesky’s API and renders a simple threaded UI using React Query, text-only content, and basic indentation. They avoided implementing onsite posting (OAuth, full client UI) as unnecessary complexity, while HN discussion explores static-site-native comments and alternative federation-based approaches.

---

## Comment pulse

- Static-site owners import comments as markdown during builds → manual review ensures zero spam and full ownership, at cost of more work.  
- Some reuse concept with Mastodon or Bluesky web components → avoid React, keep theming flexible, even mimicking Hacker News styling.  
- Others propose automation layers → Cloudflare Workers or scripts to turn submissions into markdown, or auto-discover the right Bluesky thread from the post URL.  

---

## LLM perspective

- View: Decoupling comments from origin servers via social APIs reduces hosting friction but trades independence for platform stability and policies.  
- Impact: Small blogs gain low-effort interaction and identity, but readers without Bluesky/Mastodon accounts lose the ability to participate.  
- Watch next: Worth tracking generic, protocol-agnostic comment widgets plus tools for periodically mirroring external threads into local archives or static builds.
