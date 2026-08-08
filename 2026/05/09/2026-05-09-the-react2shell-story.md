# The React2Shell Story

- Score: 209 | [HN](https://news.ycombinator.com/item?id=48065511) | Link: https://lachlan.nz/blog/the-react2shell-story/

### TL;DR

Security researcher Lachlan Davidson found React2Shell, a critical unauthenticated RCE affecting React Server Components, by reverse-engineering the undocumented Flight protocol. Flight accepted inherited properties; crafted thenables exploited JavaScript `await`, invoked React’s `Chunk.prototype.then` on attacker-controlled state, and ultimately used an internal file-blob lookup to construct and execute arbitrary code. Davidson began investigating November 24, reported Meta on November 30, and a coordinated fix shipped December 3 as CVE-2025-55182. HN praised the disclosure response while debating whether RSC’s server-client blending exposes unavoidable complexity or an unnecessary developer footgun.

### Comment pulse

- Meta and Vercel praised Davidson’s cooperation → repeated validation calls helped harden remediations before public disclosure.
- RSC critics see hidden imports and blurred boundaries as dangerous → counterpoint: supporters say web applications inherently span client and server.
- The discovery required curiosity, protocol fluency, and persistence → apparent dead ends repeatedly supplied gadgets for the final exploit.

### LLM perspective

- **View:** Undocumented serialization formats become security-critical APIs once untrusted clients can synthesize rich runtime objects.
- **Impact:** Framework developers must enforce own-property lookup and runtime schemas rather than trust TypeScript annotations.
- **Watch next:** Patch uptake, variant gadgets, non-Node runtimes, independent Flight audits, and the promised aftermath report.
