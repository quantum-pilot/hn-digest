# Subscription bombing and how to mitigate it

- Score: 279 | [HN](https://news.ycombinator.com/item?id=47609882) | Link: https://bytemash.net/posts/subscription-bombing-your-signup-form-is-a-weapon/

### TL;DR

Subscription bombing weaponizes forms to bury a victim’s genuine fraud alerts under hundreds of welcome and reset emails. Suga detected bots creating accounts with real addresses and garbage names, then requesting resets within 60 seconds; only 1–2 sign-ups per hour came from rotating countries, defeating simple rate limits. Firewall rules halved traffic, Cloudflare Turnstile stopped it, and Suga now sends only one verification email until ownership is proven. HN warned invisible Turnstile can still pass sophisticated automation and described analogous credit-card testing, favoring layered behavioral controls over any single CAPTCHA.

### Comment pulse

- One site processed about 2,000 one-dollar card checks despite Turnstile; silent blocking now fakes generic declines instead of contacting its processor.
- Newsletter operators combine normal-mode challenges, webdriver detection, honeypots, extra steps, and short bans because VPNs weakened IP reputation.
- Cloudflare dependence centralizes infrastructure and can exclude users — counterpoint: suppressing all post-verification emails greatly limits harm without universal CAPTCHA friction.

### LLM perspective

- **View:** Any unauthenticated action causing third-party email or payment traffic needs its own abuse budget and verification boundary.
- **Impact:** The primary victims are outsiders, so product metrics and provider penalties must internalize damage the site barely feels.
- **Watch next:** Per-address velocity, cross-account payment attempts, challenge bypass rates, sender complaints, disposable-email patterns, and issuer notification workflows.
