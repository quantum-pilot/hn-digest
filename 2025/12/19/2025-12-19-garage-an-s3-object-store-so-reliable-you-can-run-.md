# Garage – An S3 object store so reliable you can run it outside datacenters

- Score: 418 | [HN](https://news.ycombinator.com/item?id=46326984) | Link: https://garagehq.deuxfleurs.fr/

## TL;DR
Garage is an open-source, S3-compatible object store aimed at reliability and simplicity rather than peak performance. It’s delivered as a single dependency-free Linux binary, replicates data across three zones, runs on modest and heterogeneous hardware, and already works with tools like Nextcloud, Matrix, and Mastodon. Hacker News readers see it as a promising MinIO alternative: easier to deploy but slower at high throughput, with concerns around LMDB metadata robustness, RAM requirements, and missing S3 features like object tags.

---

## Comment pulse
- Deployment vs performance → Easier to set up than MinIO and solid for typical loads, but nowhere near MinIO’s 20–25 Gbit/s throughput—counterpoint: design explicitly de-prioritizes top speed.  
- Reliability stack worries → Default LMDB backend can corrupt after power loss without careful filesystems/snapshots; some argue hardware (PLP SSDs, UPS) matters as much as software guarantees.  
- Ecosystem and features → Many evaluating Garage as MinIO replacement; alternatives include SeaweedFS, Ceph/Rook, VersityGW; lack of S3 object tags is a blocker for some.

---

## LLM perspective
- View: Garage fits “small, reliable, self-hosted S3” better than “hyperscale S3 clone”; expectations should match that positioning.  
- Impact: Teams fleeing MinIO’s licensing shifts gain a viable, simpler clusterable backend, especially for federated and personal cloud services.  
- Watch next: Native object tagging, a more crash-resilient metadata engine, and independent benchmarks versus SeaweedFS, Ceph, and others will determine long-term adoption.
