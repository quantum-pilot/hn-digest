# FBI cyber cop: Salt Typhoon pwned 'nearly every American'

- Score: 297 | [HN](https://news.ycombinator.com/item?id=45074157) | Link: https://www.theregister.com/2025/08/28/fbi_cyber_cop_salt_typhoon/

- TL;DR
    - US officials say China-aligned Salt Typhoon infiltrated telecoms since 2019, exfiltrating bulk geolocation, traffic metadata, and some call content—likely touching “nearly every American” and victims in 80+ countries. Around 200 US orgs, including major carriers, were compromised; over 100 current/former senior officials were deeply targeted. Three PRC firms are linked to the operation. The campaign remains active. HN debates whether lawful-intercept backdoors and poor telecom hygiene enabled this, versus inevitability given state resources, and stresses auditing LI systems, resilience, and reversing cybersecurity cuts.

- Comment pulse
    - Backdoors enabled this → LI/CALEA systems are hidden, poorly audited, and once compromised can siphon traffic undetected—counterpoint: top-tier actors penetrate even without backdoors.
    - Likely pivot was LI mediator gear → Few vendors control MD consoles that trigger SPAN taps; compromise one and you tap many carriers.
    - Incident remains uncontained → Data still flowing; community wants detailed IOCs, LI audits, and restoration of gutted cybersecurity budgets.

- LLM perspective
    - View: Centralized, opaque LI is a systemic single point of failure; mandate operator-visible, immutable audit logs and strong access controls.
    - Impact: Telcos, LI vendors, and regulators must redesign interception workflows, segment networks, retire EOL gear, and enforce hardware-rooted key management.
    - Watch next: Detailed IOCs and exploited device families, firmware patches, independent LI platform audits, and any allied sanctions or indictments.
