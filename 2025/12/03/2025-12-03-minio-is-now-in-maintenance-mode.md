# MinIO is now in maintenance-mode

- Score: 384 | [HN](https://news.ycombinator.com/item?id=46136023) | Link: https://github.com/minio/minio/commit/27742d469462e1561c776f88ca7a1f26816d69e2

### TL;DR
MinIO has updated its README to declare the once-popular S3-compatible server in maintenance mode: no new features, minimal security fixes, and a push toward its commercial AIStor product. HN commenters see this as the culmination of a long retreat from genuine open source, enabled by contributor license agreements and tight corporate control. Attention is shifting to alternatives like Garage, RustFS, SeaweedFS, ironbucket, and hs5, with debates over stability, licensing (AGPL vs Apache), and governance models that prevent future rug-pulls.

### Comment pulse
- RustFS vs Garage vs SeaweedFS → RustFS ships fast under Apache license but is unstable; Garage is steadier under AGPL; SeaweedFS promising yet maturity questioned.  
- Governance worries → MinIO’s closed contribution model, feature removals, and CLAs seen as a textbook rug-pull—counterpoint: maintainers still owe staff and investors a business model.  
- New projects emerging → ironbucket and hs5 aim to recreate early-MinIO simplicity, with smaller scopes, clearer AGPL compliance, and invites for contributors and early adopters.  

### LLM perspective
- View → This accelerates a split between corporate-controlled “source-available” storage and community-guarded S3-compatible stacks.  
- Impact → Organizations relying on MinIO must plan migrations, validate protocol quirks, and reassess support contracts versus truly open alternatives.  
- Watch next → Whether a credible fork, CNCF-backed replacement, or AGPL enforcement action emerges will determine trust in storage vendors.
