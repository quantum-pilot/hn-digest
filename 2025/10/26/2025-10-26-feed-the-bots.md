# Feed the bots

- Score: 128 | [HN](https://news.ycombinator.com/item?id=45711094) | Link: https://maurycyz.com/misc/the_cost_of_trash/

- TL;DR
  - A blog proposes “feeding the bots” with trap content to pollute LLM scrapes, including a fast Markov-text “babbler” and playful hidden instructions to mislead summarizers. HN debates defenses: public Basic Auth credentials won’t stop determined crawlers; ethical crawlers report increasing blocks (even for RSS). Some advocate flooding the web with plausible garbage to raise training costs; skeptics argue modern filters detect trash cheaply, shifting costs but not forcing human review.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Public Basic Auth for all sites → ineffective; bots can send Authorization headers; only deters naive scrapers — counterpoint: may throttle low-effort crawlers briefly.
  - Markov babbler/noise injection → low-cost, plausible text could taint training data; praised for elegance and speed.
  - Ethical crawler perspective → slow, respectful crawling still blocked; RSS feeds often gated; resorts to adaptive headers and infrequent requests.

- LLM perspective
  - View: Data-poisoning cat-and-mouse will push scrapers toward stronger heuristics, content provenance, and whitelisting.
  - Impact: Smaller sites may gate content; indie RSS suffers; cleaning pipelines get pricier for model builders.
  - Watch next: Benchmarks on poisoning effectiveness, prompt-injection defenses, and adoption of signed content or opt-in indexing.
