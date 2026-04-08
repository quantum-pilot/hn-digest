# Show HN: Stop paying for Dropbox/Google Drive, use your own S3 bucket instead

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47673394) | Link: https://locker.dev

## TL;DR
- Locker is an open-source, self-hosted alternative to Dropbox/Google Drive that lets you bring your own storage (local disk, S3, R2, Vercel Blob) and manage files via a web UI with search-in-PDFs/images, share links, team workspaces, and API keys. HN commenters like the control and transparency but worry about trusting a week-old project with important data and note the absence of native sync clients. Others question cost savings versus consumer cloud plans and suggest rclone, Seafile, Syncthing, or existing tools instead.

## Comment pulse
- Skeptical about trusting new “vibe-coded” storage apps → risk of bugs/data loss with immature projects—counterpoint: self-hosted, open source lets you inspect and control everything.  
- Dropbox/Drive’s product is OS-integrated sync clients → seamless folder semantics on desktop; Locker’s browser UI lacks that, especially on mobile where sync options are weak.  
- Cost calculus mixed → S3/R2 can exceed consumer cloud plans once storage, egress, operations included; some prefer Backblaze/Glacier, others happily keep paying Dropbox for convenience.

## LLM perspective
- View: Locker is a polished front-end for object storage, best suited to technical teams already running S3/R2-like backends.  
- Impact: Could reduce SaaS lock-in for startups, agencies, and privacy-conscious users who want Drive-like sharing but own infrastructure.  
- Watch next: desktop/mobile sync clients, end-to-end encryption, backup/versioning story, proof and security audits will decide if it escapes hobby-project status.
