# How ChatGPT serves ads

- Score: 488 | [HN](https://news.ycombinator.com/item?id=47942437) | Link: https://www.buchodi.com/how-chatgpt-serves-ads-heres-the-full-attribution-loop/

### TL;DR

Traffic captured from a consented mobile fleet shows ChatGPT ads arriving as structured `single_advertiser_ad_unit` events inside the conversation’s server-sent-event stream, alongside model output. The cards carry advertiser metadata, hosted creative, and four encrypted attribution tokens. Clicking opens an in-app webview; participating merchant sites run OpenAI’s OAIQ SDK, which stores an `oppref` token in a first-party cookie for 30 days and reports content views. Six conversations on one account received topic-matched advertisers, though the researcher found no evidence about whether prior chats influence targeting.

### Comment pulse

- Several commenters stressed ads currently target the free tier and ad-supported Go plan — counterpoint: others expect expansion to costlier plans.
- The main fear was covert paid influence inside generated text, not the visible card-and-pixel mechanism documented here.
- Others expect adversarial content and “generative engine optimization” to become the harder attribution problem.

### LLM perspective

- Keeping ad units structurally separate from model prose makes auditing and user recognition easier.
- Attribution should disclose retention, merchant participation, targeting inputs, and whether conversation history contributes.
- Independent tests should verify ad relevance never changes factual answers or suppresses competing options.
