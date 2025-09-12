# Cloudflare Radar: AI Insights

- Score: 385 | [HN](https://news.ycombinator.com/item?id=45093090) | Link: https://radar.cloudflare.com/ai-insights

- TL;DR
    - Cloudflare Radar’s AI Insights aggregates network-wide telemetry on AI crawlers and usage: who’s crawling, for what purpose, how crawl-to-refer ratios are shifting, robots.txt trends, and Workers AI model/task popularity. Cloudflare reports training now drives ~80% of AI crawling while referrals to publishers decline. HN debates whether Cloudflare is becoming a paid gatekeeper via bot verification versus providing a much-needed identity standard. Readers flag data surprises: Character.AI’s high DNS popularity and Llama‑3‑8B leading Workers deployments; questions arise over labeling Common Crawl as an “AI bot.”

- Comment pulse
    - Cloudflare gatekeeps AI crawlers, possibly charging → risks to small search engines/archives — counterpoint: bot verification standards are overdue and within CF’s remit.
    - Character.AI ranks #2 by 1.1.1.1 DNS queries → indicates youth adoption; some suspect DNS caching skew; Workers usage shows Llama‑3‑8B dominates.
    - Labeling Common Crawl’s CCBot as an “AI bot” → risks overblocking research/archival crawls; potential loophole: route access through CC to bypass restrictions.

- LLM perspective
    - View: Cloudflare is centralizing bot identity and telemetry, reshaping crawling economics and giving publishers a lever over AI access.
    - Impact: AI vendors must authenticate crawlers and negotiate terms; small crawlers face friction; publishers get dashboards and enforceable robots.txt semantics.
    - Watch next: WebBotAuth adoption, crawl-to-refer trends, enforcement of AI user-agent directives, and whether Common Crawl receives carve-outs.
