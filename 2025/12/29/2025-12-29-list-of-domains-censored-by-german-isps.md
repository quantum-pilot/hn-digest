# List of domains censored by German ISPs

- Score: 261 | [HN](https://news.ycombinator.com/item?id=46423566) | Link: https://cuiiliste.de/domains

### TL;DR

The page lists domains first blocked by participating German internet providers, largely piracy, streaming, ROM, music, book, and Sci-Hub sites, with recorded dates from 2022 through December 2025. HN commenters treated publication as an inadvertent discovery guide—the Streisand effect—but clarified that the censorship reportedly uses ISP DNS rather than deeper traffic filtering. Consequently, changing resolvers or operating a recursive DNS server may bypass it, unlike more robust blocking used elsewhere, while raising questions about centralization and SNI-based enforcement.

### Comment pulse

- Publication amplifies targets → readers immediately bookmarked the list as a catalog, frustrating others tired of the recurring joke.
- DNS blocking is weak enforcement → alternative resolvers or self-hosted recursion reportedly bypass restrictions affecting ISP DNS users.
- Resolver choice has broader tradeoffs → public services avoid flaky ISP DNS but concentrate queries among a few providers.

### LLM perspective

- View: Transparent blocklists improve accountability while simultaneously lowering discovery costs for the prohibited material.
- Impact: German ISP customers can audit censorship and understand that enforcement depends substantially on resolver configuration.
- Watch next: Verify block authority, update cadence, ISP participation, false positives, and whether enforcement expands beyond DNS.
