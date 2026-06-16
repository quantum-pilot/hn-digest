# A backdoor in a LinkedIn job offer

- Score: 549 | [HN](https://news.ycombinator.com/item?id=48546294) | Link: https://roman.pt/posts/linkedin-backdoor/

- TL;DR
    - A LinkedIn “recruiter” for a crypto startup sent a candidate a GitHub repo and asked him to inspect a “deprecated Node modules” issue. On a throwaway VPS, with an AI code reviewer in read‑only mode, he found a backdoor hidden in a test file, triggered via npm’s prepare script on install to execute remote server code. Both the recruiter and the repo author identities were impersonated. HN discussion centers on platform abuse, weak cybercrime recourse, and interview-style attack vectors.

- Comment pulse
    - LinkedIn and GitHub are prime scam infrastructure → fake recruiters and impersonated devs linger despite reports; companies can’t easily disavow them on official pages.  
    - There’s no effective “911 for cybercrime” → IC3 exists but rarely responds; jurisdiction and low priority make enforcement rare — counterpoint: agencies triage toward violent crimes.  
    - Attack blurs into standard hiring workflow → repo-review and “fix the install” tasks pressure candidates to run untrusted code; many now recommend throwaway VMs.

- LLM perspective
    - View: This attack fuses social engineering with common dev workflows, eroding assumptions that interview repos are benign.  
    - Impact: Hiring pipelines, security teams, and individual developers must treat all third-party repos as untrusted, even during seemingly legitimate recruiting.  
    - Watch next: Package managers may sandbox lifecycle scripts; platforms might add stronger identity verification for recruiters and repository owners.
