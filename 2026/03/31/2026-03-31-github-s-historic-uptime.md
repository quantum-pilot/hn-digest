# GitHub's Historic Uptime

- Score: 369 | [HN](https://news.ycombinator.com/item?id=47591928) | Link: https://damrnelson.github.io/github-historical-uptime/

- TL;DR  
  Post visualizes GitHub’s historical uptime from its official status page, hinting at worse reliability after the Microsoft acquisition and Azure migration. Commenters question pre‑2018 data accuracy and note features like Actions misleadingly show 100% uptime before launch. Alternative community status tracking reports much lower aggregate availability, but its methodology (counting third‑party outages, aggregating all components) is debated. Overall trend: reliability problems, especially with GitHub Actions, have been ongoing for years rather than a single post‑acquisition cliff.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Status-page-derived “historic uptime” is biased → pre‑2018 data spotty; products show 100% before launch. — counterpoint: per‑service graphs still show similar decline.  
  - Azure migration blamed → users report GitHub outages correlating with Azure issues; long migration window suggests platform changes harmed reliability, though not enough to explain all 6+ years.  
  - GitHub Actions seen as main culprit → frequent failures, operational complexity; critics say expanding beyond core Git hosting violated “do one thing well” philosophy.  

- LLM perspective  
  - View: Historic uptime claims should be normalized for product launch dates and third‑party dependencies, and cross‑checked with independent monitoring data.  
  - Impact: Engineers relying on Actions need contingency plans: retries, mirroring to alternative CI, and clear incident playbooks for GitHub partial outages.  
  - Watch next: Track GitHub’s SLOs per component over time; watch Azure and OpenAI incidents to see whether dependency coupling tightens or loosens.
