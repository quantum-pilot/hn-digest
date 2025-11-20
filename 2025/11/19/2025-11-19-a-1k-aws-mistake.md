# A $1k AWS mistake

- Score: 267 | [HN](https://news.ycombinator.com/item?id=45977744) | Link: https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/

### TL;DR
A team mirrored multi‑hundred‑GB datasets into S3, assuming EC2↔S3 in‑region traffic was free. Because their EC2s sat in a private VPC using a NAT Gateway, all S3 traffic exited via NAT and came back, incurring ~$1k in “data processing” fees. The fix was creating a free S3 VPC Gateway Endpoint so S3 traffic stays inside AWS’s network and bypasses NAT. HN discussion centers on why this isn’t the default, NAT alternatives, and AWS’s weak cost‑control story.

---

### Comment pulse
- S3 endpoints should be default → common, costly pitfall; many hit four‑ and five‑figure bills. — counterpoint: defaults must protect “air‑gapped” VPCs and cross‑region S3 workflows.
- Avoid managed NAT Gateway → run fck‑nat, tiny Linux NAT instance, or IPv6 egress‑only gateways to dodge per‑GB NAT processing charges.
- Cloud billing is hostile to tinkerers → delayed alerts, rare hard caps, and org incentives favor surprise overages; new flat‑rate plans are a small but promising step.

---

### LLM perspective
- View: Treat “network path” as a first‑class architectural concern; cost, security, and performance all flow from routing choices.
- Impact: Small teams and hobbyists are most exposed; one misconfigured NAT or ML job can erase months of savings or revenue.
- Watch next: More flat‑rate and capped offerings, better real‑time cost guards, and tooling that auto‑suggests endpoints/NAT changes from observed traffic.
