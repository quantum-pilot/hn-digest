# We built another object storage

- Score: 125 | [HN](https://news.ycombinator.com/item?id=46254087) | Link: https://fractalbits.com/blog/why-we-built-another-object-storage/

### TL;DR
FractalBits is an S3‑compatible object store aimed at AI and analytics workloads with huge numbers of small objects. It argues current “high‑performance” tiers like S3 Express are economically unusable for high IOPS, especially when you need directory semantics and atomic renames. Its core is a Zig‑based on‑disk adaptive radix tree for full‑path metadata, with quorum replication and strong consistency, delivered in a BYOC model on your AWS account. HN discussion questions whether optimizing for many tiny remote files is wise, compares it to filesystems/KV stores, and probes its open‑source governance and longevity.

---

### Comment pulse
- OSS‑minded users probe AIstore comparisons, clustering/k8s, benchmarks, AI‑written marketing, CLA/governance; maintainer answers with perf numbers, centralized metadata, Apache‑2.0 code, AWS‑only BYOC deployment.  
- AI/ML engineers say training should batch into large files and cache on NVMe; millions of 4KB network reads are an anti‑pattern — counterpoint: random sampling and real‑time analytics still favor fast small‑object access.  
- Others ask why not just a filesystem or KV/DB; defenders highlight S3‑style HTTP access, cross‑tenant auth, object‑level atomicity, and pervasive small‑object usage in the wild.

---

### LLM perspective
- View: A fast, strongly consistent, S3‑compatible store for small objects targets people who can’t or won’t redesign data formats.  
- Impact: Most value lands with teams already abusing S3 for tiny files, especially those blocked by S3 Express request pricing.  
- Watch next: Need durability/failure reports, k8s/on‑prem stories, ops tooling, and head‑to‑head results versus batched formats like WebDataset or Parquet.
