# Is BGP safe yet?

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47600382) | Link: https://isbgpsafeyet.com/

### TL;DR  
Cloudflare’s isbgpsafeyet.com tracks which networks deploy RPKI, a cryptographic system for validating who may originate IP prefixes, to reduce BGP route leaks and hijacks. The page explains BGP hijacks in simple diagrams, lets users test their ISP, and categorizes hundreds of operators as safe, partially safe, or unsafe based on RPKI and filtering. Commenters debate how much protection this really adds, discuss missing mechanisms like ASPA/BGPSec, and propose newer cryptographic approaches such as proof‑carrying data for routing.

---

### Comment pulse  
- RPKI only fixes origin, not path → hijacks via forged paths remain; BGPSec rejected as impractical; research like proof-carrying data and ASPA suggested.  
- Coverage looks good from headline table → “show all” reveals hundreds of unsafe networks, including BT, Vodafone branches, Starlink, big mobile ISPs worldwide.  
- Site focuses on ROA invalids → ignores ASPA and BGPSec, overstating safety — counterpoint: still valuable awareness tool and simple end-user test.

---

### LLM perspective  
- View: Origin validation is becoming normal for large backbones, but robust path validation and universal deployment are still open problems.  
- Impact: As more transit networks drop invalids, pressure increases on regional, mobile, and hosting providers to deploy RPKI and ASPA.  
- Watch next: Measured impact of ASPA rollout, any serious BGPSec replacements, and prototypes of proof-carrying-data routing in operator testbeds.
