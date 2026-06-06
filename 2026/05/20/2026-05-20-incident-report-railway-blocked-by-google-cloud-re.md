# Incident Report: Railway Blocked by Google Cloud [resolved]

- Score: 547 | [HN](https://news.ycombinator.com/item?id=48201484) | Link: https://status.railway.com/incident/I23M92U0

### TL;DR
Railway, a PaaS hosting provider, experienced a major outage when Google Cloud blocked its GCP account, cutting off compute, networking, and key control-plane services like the dashboard and API. Railway worked with Google to regain access, but lingering GCP networking issues slowed service restarts. Recovery was staged: restoring compute, throttling non‑enterprise builds, gradually bringing workloads back, and auto‑redeploying unhealthy services. By May 20, services were largely restored and a formal postmortem was published, with users advised to redeploy if needed.

---

### LLM perspective
- View: A single cloud account as a critical dependency creates a hidden single point of failure for downstream platforms.  
- Impact: PaaS customers inherit cloud-vendor account risks, even when their own usage is compliant and workloads are healthy.  
- Watch next: Expect more explicit SLAs, multi‑cloud control planes, and automated failover strategies for provider account or networking lockouts.
