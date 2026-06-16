# The RCE that AMD wouldn't fix

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48492215) | Link: https://mrbruh.com/amd2/

### TL;DR
AMD’s Ryzen Master AutoUpdate tool fetched its update manifest over HTTPS, but the actual executables over plain HTTP and executed them without signature checks, enabling trivial remote code execution via MITM or DNS poisoning. AMD’s bug bounty vendor rejected the report as “MITM, out of scope”; AMD later reversed course after publicity, asked the researcher to pull the blog, took 124 days to ship a partial fix (HTTPS only, CRC-32 “verification”), and still paid no bounty.  
If you use AMD tools, the author recommends uninstalling and reinstalling fresh versions.

---

### Comment pulse
- Hardware updaters are often insecure → HTTP downloads, CRC-32 “verification,” and fragile redirect handling are common; compromise of vendor infra still means mass compromise.  
- Bug bounty scope vs. real risk → MITM exclusions may make sense for “installed rogue CA” scenarios, but not when the product itself uses HTTP—counterpoint: programs define scope to control costs.  
- AMD-specific criticism → Longstanding reputation for poor software, low pay, and weak engineering culture seen as underlying cause of such security failures.

---

### LLM perspective
- View: Auto-updaters remain a weak link; simple design errors (HTTP, no signatures) yield RCE despite widespread prior art.  
- Impact: PC users and enterprises relying on vendor tools inherit silent, hard-to-audit risk from opaque, proprietary updaters.  
- Watch next: Systematic auditing of OEM updaters; OS-level enforcement of signed/HTTPS updates; clearer, less gameable bug-bounty scopes.
