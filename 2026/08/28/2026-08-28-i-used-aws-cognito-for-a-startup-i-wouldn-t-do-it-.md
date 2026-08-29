# I used AWS cognito for a startup. I wouldn't do it again

- Score: 176 | [HN](https://news.ycombinator.com/item?id=49478091) | Link: https://joshkaramuth.com/blog/aws-cognito-authentication-startup-nightmare/

### TL;DR

A startup developer regrets choosing AWS Cognito despite its free tier and AWS integration. They cite fragmented documentation, disruptive Amplify v6 changes, cloud-dependent testing, limited hosted-UI customization, and effectively immutable user-pool settings that can force difficult migrations. Their lesson is to test realistic authentication flows and value engineering time over nominal service cost. Commenters largely corroborate configuration and documentation pain, but note that managed authentication offers production hardening; they also debate password-hash portability and Cognito's AWS-resource integration.

### Comment pulse

- AWS documentation is exhaustive but hard to navigate → versioned examples and scattered guidance obscure practical paths.
- Immutable pool choices create lasting migration costs → email behavior and custom attributes can require rebuilding user directories.
- Managed authentication absorbs serious security work → counterpoint: portability, local testing, backups, and developer experience remain weak.

### LLM perspective

- View: Cognito's low usage price can conceal a high integration and configuration-lock-in cost.
- Impact: Small teams risk spending scarce engineering time on identity plumbing instead of product work.
- Watch next: Prototype password reset, email identity, migration, backup, and custom-attribute flows before selecting any provider.
