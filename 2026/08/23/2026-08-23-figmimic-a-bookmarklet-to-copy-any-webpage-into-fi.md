# Figmimic – A bookmarklet to copy any webpage into Figma as editable layers

- Score: 123 | [HN](https://news.ycombinator.com/item?id=49402213) | Link: https://marcua.net/minitools/figmimic/

### TL;DR

Figmimic is a roughly 400 KB bookmarklet that turns the current webpage into editable Figma frames on the clipboard rather than a flat screenshot. Bundling Figma’s capture library lets it operate without loading remote code, including on authenticated pages and sites with strict content-security policies. Installation fails silently in Firefox because bookmark URLs exceed its limit, clipboard permissions can require another click, and third-party images may be omitted. Commenters valued internal-dashboard capture but questioned differentiation from Figma’s extension, reliability, maintenance, and contractual copying risks.

### Comment pulse

- Bookmarklets can reuse authenticated sessions and reshape private interfaces → that power enables useful overlays but expands privacy and authorization concerns.
- Extensions may distribute and update more reliably → bookmarklets remain convenient for small, transparent, user-triggered tools.
- Real-world capture is inconsistent → some sites take minutes or never confirm copying, though partial success still saves recreation work.

### LLM perspective

- View: The distinctive claim is portable authenticated-page capture; the input does not establish superiority over Figma’s official extension.
- Impact: Designers can prototype from existing interfaces faster, while organizations must police sensitive data, licenses, and contract restrictions.
- Watch next: Side-by-side extension tests, browser compatibility, capture fidelity, update integrity, clipboard reliability, and safeguards for confidential pages.
