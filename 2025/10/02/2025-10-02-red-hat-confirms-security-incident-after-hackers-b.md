# Red Hat confirms security incident after hackers breach GitLab instance

- Score: 231 | [HN](https://news.ycombinator.com/item?id=45448772) | Link: https://www.bleepingcomputer.com/news/security/red-hat-confirms-security-incident-after-hackers-claim-github-breach/

- TL;DR
    - Red Hat confirmed a breach of a self-managed GitLab instance used by its Consulting division after the Crimson Collective claimed 570GB from 28k repos, including ~800 Customer Engagement Reports. Those reports and code allegedly contained tokens and DB URIs used to reach some customer infrastructure. Red Hat says products and supply chain are unaffected, has isolated the instance, and is notifying clients. HN discussion fixated on the GitLab—not GitHub—clarification, jokes about unanswered extortion emails, and skepticism toward checkbox ISO27001 security.

- Comment pulse
    - GitLab, not GitHub → matters because self-hosted GitLab shifts security to Red Hat; commenters suspect lax account/secret hygiene.
    - Ignoring extortion emails → some praise “can’t be extorted if unreachable”; — counterpoint: could increase data exposure pressure on customers.
    - ISO27001 criticism → treated as a sales checkbox; scope carved out, quick fixes during audits, posture unchanged afterward.

- LLM perspective
    - View: Consulting artifacts with secrets are high-risk; secret sprawl via CERs turns one breach into many.
    - Impact: Immediate token revocation, rotation of DB credentials, and customer perimeter monitoring for unusual Red Hat-sourced access.
    - Watch next: Disclosure depth: number of affected customers, confirmed downstream intrusions, and GitLab CE hardening steps (MFA, SSO, secret scanning, repo sanitization).
