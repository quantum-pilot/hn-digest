# Bucketsquatting is finally dead

- Score: 301 | [HN](https://news.ycombinator.com/item?id=47361913) | Link: https://onecloudplease.com/blog/bucketsquatting-is-finally-dead

### TL;DR
"Bucketsquatting" vulnerability, S3 global names freed after deletion; new account-regional namespaces `<prefix>-<accountid>-<region>-an` reserve names to one account, enforced by `s3:x-amz-bucket-namespace`, recommended default; existing buckets need migration; GCS uses domain-verified bucket names; Azure still has global, cramped storage-account namespace; discussion covers AWS’s broader identity immutability and support issues, Azure naming pain and desire for v2-style APIs, alternative naming schemes, IaC defaults, and provider bugs from deterministic scratch-bucket names seen in recent CVEs.

---

### Comment pulse
- AWS identity artifacts stick forever → root emails on deleted accounts block reuse, MFA loss locks roots; plus-addressing and non-human roots suggested mitigations.  
- Azure storage suffers global, 24‑char, alphanumeric account names; no separators. Commenters want per-customer namespaces; ex‑S3 engineer laments legacy API constraints and missing v2.  
- People debate Discord-style tags vs UUIDs/petnames for democratizing names; others praise Terraform-style randomized bucket suffixes and note cloud scratch-bucket bugs enabling squatting.

---

### LLM perspective
- View: Adopting the -an namespace pattern plus org-wide SCPs should become a baseline control, especially for regulated or multi-team AWS environments.  
- Impact: Expect IaC modules, internal templates, and security linters to standardize on this naming, gradually making legacy naked bucket names a smell.  
- Watch next: Watch for Azure introducing similar per-account namespaces and for AWS extending namespace ideas to other globally scoped resources beyond S3.
