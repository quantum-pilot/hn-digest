# Claude for Chrome

- Score: 799 | [HN](https://news.ycombinator.com/item?id=45030760) | Link: https://www.anthropic.com/news/claude-for-chrome

- TL;DR
  - Anthropic is piloting a Chrome extension that lets Claude see and act in your browser, with site-level permissions and confirmations for risky actions. Their red-team found 23.6% prompt-injection success without mitigations, reduced to 11.2% with new defenses; four browser-specific attack types dropped 35.7%→0%. Access is limited to 1,000 Max users while they refine classifiers, blocks, and permissions; avoid sensitive sites. HN applauds transparency but flags the lethal trifecta risk, technical brittleness (DOM/context), and questions whether 11% is deployable.

- Comment pulse
  - High-risk trifecta → private data + untrusted inputs + exfil/actions; mitigate via separate accounts, per-request auth, cookie isolation — counterpoint: comparable to human phishing susceptibility.
  - DOM/screenshot dumps overwhelm context → pages hit 60–70k tokens; better: compact render-derived representations, explicit clickable affordances, or machine APIs instead of brittle UI automation.
  - Current agents lose thread on multi-step tasks → loops stop early, radio-button choices misread; limiting tools and avoiding screenshots can help for narrow tasks.

- LLM perspective
  - View: Anthropic foregrounds measured safety over capability hype, using a small pilot to harvest real adversarial data.
  - Impact: Near-term value on low-risk sites; long-term needs OS/browser permission brokers and standardized “safe actions” per site.
  - Watch next: Independent attack-rate benchmarks, default cookie scoping, per-action auth UX, and multi-step reliability evaluations beyond demos.
