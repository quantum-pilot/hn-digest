# Securing a DoD contractor: Finding a multi-tenant authorization vulnerability

- Score: 156 | [HN](https://news.ycombinator.com/item?id=48012162) | Link: https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup

## TL;DR
Strix, an autonomous open-source AI pentesting agent, tested Schemata, a DoD training platform, and found effectively no multi-tenant authorization: any ordinary user could list all users, organizations, courses, S3 document links, and even modify content. Exposed data included confidential military training manuals and identifiable U.S. service member records. Strix disclosed privately for five months with little action until they warned of publication, after which Schemata quickly patched. The story spotlights weak security culture, compliance theater, and the emerging role of AI-driven security testing.

---

## Comment pulse
- Startups routinely ship with missing auth, client-side keys, and no RLS → security talent is rare and speed-to-market is over-rewarded; penalties are minimal.  
- AI pentesting tools can outperform pricey firms → one user saw a $50 AI scan beat a $10k greybox test, especially at modern development velocity.  
- Certifications like SOC 2 / ISO don’t guarantee real security → auditors resemble ratings agencies pre-2008; serious multi-tenant bugs still slip through. — counterpoint: a careful audit should catch this.

---

## LLM perspective
- View: Multi-tenant auth remains a frequent systemic failure; AI agents make such oversights cheaper to find and therefore harder to excuse.  
- Impact: Startups, especially handling CUI or regulated data, will face growing pressure for continuous, automated security validation alongside traditional audits.  
- Watch next: Benchmarks comparing AI pentesters vs human firms; regulatory reaction when AI-found vulns surface at certified or government contractors.
