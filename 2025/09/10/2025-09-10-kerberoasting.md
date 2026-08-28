# Kerberoasting

- Score: 141 | [HN](https://news.ycombinator.com/item?id=45196437) | Link: https://blog.cryptographyengineering.com/2025/09/10/kerberoasting/

### TL;DR

Kerberoasting lets any low-privilege Active Directory user request a service ticket and attempt to recover a weak service-account password offline. The danger rises when services use human passwords, excessive privileges, or legacy RC4 with fast unsalted NT-hash derivation rather than managed random keys and AES. The author connects the technique to the Ascension Health ransomware incident and criticizes Microsoft for preserving unsafe compatibility. Commenters corrected ticket terminology and cracking-rate language, explained legacy constraints, and recommended managed service accounts, least privilege, strong passwords, AES enforcement, and monitoring.

### Comment pulse

- Several specialists corrected TGS versus TGT terminology while agreeing that the described attack chain remains valid.
- Administrators shared account queries and event-based auditing approaches for identifying explicitly configured legacy encryption.

### LLM perspective

- View: Kerberoasting converts weak credential policy into an offline computation problem with no rate limiter.
- Impact: A single overprivileged service password can turn an initial endpoint compromise into domain-wide damage.
- Watch next: Inventory service accounts, disable RC4 where possible, rotate managed keys, and monitor unusual ticket requests.
