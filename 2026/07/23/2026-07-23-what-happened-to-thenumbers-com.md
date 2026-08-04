# What happened to TheNumbers.com

- Score: 269 | [HN](https://news.ycombinator.com/item?id=49024691) | Link: https://stephenfollows.com/p/what-just-happened-to-thenumberscom-should-worry-us-all

### TL;DR

The Numbers, a 30-year-old film database with 2 million pages and 160,000 source files, disappeared March 5 after months of overwhelming automated traffic and suspicious probes for backdoors. Only 10% of visits were human; restoring the legacy server risked immediate compromise, so its owners launched a reduced site and began rebuilding. The article suggests, without proof, that prediction-market traders might seek unpublished box-office data, while AI lowers attack costs and crawlers destroy old web economics. HN readers debate static publishing and caching versus the deeper security and incentive failures.

### Comment pulse

- AI crawlers externalize costs → one public-data operator saw bots ignore a 10-GB download and crawl terabytes of HTML, adding roughly $1,000 monthly.
- Architecture can absorb read traffic → commenters propose static generation, CDNs, and aggressive caching — counterpoint: these do not neutralize exploitable legacy endpoints.
- Openness feels less reciprocal → maintainers hesitate to publish when extraction raises bills and feeds commercial models — counterpoint: others welcome broader model training.

### LLM perspective

- View: This is not merely scaling failure; monetized reference data converts availability, integrity, and publication timing into attack surfaces.
- Impact: Small knowledge sites may retreat behind APIs, subscriptions, bot challenges, or licensing, reducing public access and archival resilience.
- Watch next: Track restored features, incident findings, static/CDN architecture, bot ratios, pay-per-use enforcement, prediction-market safeguards, and sustainable licensing.
