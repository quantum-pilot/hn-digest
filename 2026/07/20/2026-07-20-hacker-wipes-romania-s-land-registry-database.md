# Hacker wipes Romania's land registry database

- Score: 553 | [HN](https://news.ycombinator.com/item?id=48978605) | Link: https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/

## TL;DR
A hacker using valid credentials broke into Romania’s land registry agency (ANCPI), tried and failed to extort it, then wiped production systems and online backups and leaked internal data. Real-estate transactions and ownership certificates have been frozen nationwide for days, but the agency claims offline backups in multiple locations allow a full rebuild and is migrating services to the government cloud. The attacker, known as ByteToBreach, has been doxxed as an Algerian citizen, and similar land registries have been hit worldwide.

---

## Comment pulse
- Even with offline backups, recent transactions likely vanished → creates room for disputes, targeted fraud, and messy reconstruction via paperwork and testimonies.  
- Root cause seen as governance, not tech → crony contracts, underpaid/underqualified staff, bad specs; moving to “government cloud” may just repackage the same problems.  
- Doxxing a named Algerian suspect matters → Algeria has an extradition treaty with Romania, so unlike Russian safe havens, arrest is at least plausible—counterpoint: good opsec would have prevented attribution.

---

## LLM perspective
- View: Land registries are now clearly prime ransomware/extortion targets; they need bank-level security, not commodity government IT.  
- Impact: Governments, notaries, and lenders must assume multi-week registry outages and design legal and business continuity processes around that.  
- Watch next: Whether Romania’s rebuild adds immutable logs, regular restore drills, and stronger identity controls—or just rehosts the same design in a new cloud.
