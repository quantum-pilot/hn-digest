# Google suspended my company's Google cloud account for the third time

- Score: 397 | [HN](https://news.ycombinator.com/item?id=45798827) | Link: https://www.agwa.name/blog/post/google_suspended_sslmates_cloud_account_again

### TL;DR

SSLMate’s author says Google suspended the company’s Cloud account for a third time, initially providing little explanation and disabling resources needed to manage the appeal. The account existed mainly to create service accounts for customer integrations, following Google’s documented pattern; repeated suspensions nevertheless made that dependency a reliability risk. After the latest post reached Hacker News, most access returned without a clear cause. The author is considering customer-created keys or OIDC, trading easier setup against security, operational independence, and substantially more configuration.

### Comment pulse

- Commenters treated automated enforcement and weak appeal channels as recurring platform risks, often citing their own unverified incidents.
- Smaller providers were suggested for human support, though commenters noted moderation failures are not exclusive to large platforms.

### LLM perspective

- View: Administrative control-plane dependence deserves the same failure planning as a technical service dependency.
- Impact: A suspended provider account can break customer integrations even when the underlying product behaves correctly.
- Watch next: Whether direct OIDC principals can replace provider-owned service accounts without burdening customers.
