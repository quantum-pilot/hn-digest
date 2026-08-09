# Cyber.mil serving file downloads using TLS certificate which expired 3 days ago

- Score: 153 | [HN](https://news.ycombinator.com/item?id=47490816) | Link: https://www.cyber.mil/stigs/downloads

### TL;DR

The public.cyber.mil download host presented an IdenTrust TLS certificate that expired March 20, three days before the HN post. Commenters say the DoD page instructed civilian-network users to continue through the browser’s advanced warning while renewal was underway. Encryption may still function, but bypassing certificate validation removes server authentication, obscures whether a key leaked or was revoked, and trains users to ignore warnings—making interception and download substitution harder to detect. HN calls the lapse inexcusable while explaining that public-facing DoD sites sit outside its internal CAC-based PKI.

### Comment pulse

- Expiry is not broken encryption by itself → validity limits exposure when keys leak and revocation is incomplete.
- Telling users to bypass warnings creates error fatigue — counterpoint: DoD PKI, CAC authentication, isolation, and vendor approvals make automation unusually difficult.
- Monitoring could flag deadlines weeks ahead → legacy enterprise services often lack ACME support, but complexity does not excuse unsafe guidance.

### LLM perspective

- **View:** The operational failure became a security failure when users were told to disable the trust check.
- **Impact:** Anyone bypassing the warning to download STIG material faced origin uncertainty; operators damaged confidence in future browser warnings.
- **Watch next:** Certificate replacement, removal of bypass instructions, CAA and ACME adoption, revocation status, and automated expiry monitoring.
