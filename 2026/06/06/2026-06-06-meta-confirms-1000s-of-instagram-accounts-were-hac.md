# Meta confirms 1000s of Instagram accounts were hacked by abusing its AI chatbot

- Score: 351 | [HN](https://news.ycombinator.com/item?id=48427643) | Link: https://this.weekinsecurity.com/meta-confirms-thousands-of-instagram-accounts-were-hacked-by-abusing-its-ai-chatbot/

### TL;DR
Meta disclosed that at least 20,225 Instagram accounts were hijacked via a bug in its Meta AI support chatbot. For accounts without two-factor authentication, attackers could simply ask the bot to send a password-reset email to an address they controlled; a broken verification step let this succeed for nearly seven weeks. Hackers then gained full access to profiles and DMs. Meta has disabled the chatbot’s reset path, notified victims, and faces criticism over safety testing, legal liability, and opaque automation.

---

### Comment pulse
- Meta’s “tool worked properly” phrasing angers commenters → sounds like legal CYA; some argue the chatbot was only a UI, with the real bug server-side.  
- Breach scale debated: 20k full account takeovers and DM exposure feels huge to users—counterpoint: tiny fraction of billions of MAUs, unlikely to dent Meta.  
- Many share stories of legitimate business/product accounts auto-banned with no human appeal, contrasting Meta’s strict anti-spam automation with its lax testing of powerful recovery tools.  

---

### LLM perspective
- View: Account-recovery flows fronted by LLMs must be threat-modeled as privileged operators, not chatty UIs; any bypass becomes instant mass-account compromise.  
- Impact: Creators and businesses without 2FA bear most risk; expect regulators to scrutinize AI-assisted recovery under security and AI-governance rules.  
- Watch next: mandatory 2FA for high-reach accounts, audits of AI flows, and postmortems linking executive compensation to security outcomes.
