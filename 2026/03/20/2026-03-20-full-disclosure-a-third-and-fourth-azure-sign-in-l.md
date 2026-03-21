# Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

- Score: 280 | [HN](https://news.ycombinator.com/item?id=47448994) | Link: https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found

## TL;DR
Researcher “nyxgeek” discloses two more Azure Entra ID sign‑in log bypasses, on top of two earlier ones, all found via simple fuzzing. GraphGoblin uses an absurdly long but valid `scope` (e.g., thousands of `openid` entries) and Graph****** uses a ~50k‑char User‑Agent; both return fully functional tokens while generating no Entra sign‑in or Log Analytics entries, likely due to logging database field overflows. Microsoft silently patched them but labeled severity “Moderate” and paid no bounty, prompting criticism of its security culture and transparency. Defenders with E5 can detect such gaps by correlating Microsoft Graph Activity logs with sign‑in logs via KQL.

---

## Comment pulse
- Azure/Microsoft security is seen as systematically weak → CISA, ProPublica, Ars reports, and past multi‑tenant breaches reinforce distrust of Azure’s cloud isolation.
- Cybersecurity feels disastrously behind its societal importance → complex, fragile auth/ logging stacks protect critical infrastructure with error modes as basic as column overflows.
- Audit logs themselves aren’t fully trustworthy → Azure UI bugs misattribute actions; logs reflect APIs, not user intent — counterpoint: technically “accurate” but useless for human accountability.

---

## LLM perspective
- View: Treat cloud sign‑in logs as fallible telemetry, not ground truth; always cross‑check with independent activity sources.
- Impact: Security teams, auditors, and regulators must assume occasional silent log loss when designing detection and incident response.
- Watch next: Public postmortems on logging integrity, cross‑cloud comparisons, and whether MSRC tightens bounty/severity policies for auth‑logging flaws.
