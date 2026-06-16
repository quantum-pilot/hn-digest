# A low-carbon computing platform from your retired phones

- Score: 321 | [HN](https://news.ycombinator.com/item?id=48515336) | Link: https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/

## TL;DR
Google-funded UCSD researchers are turning 2,000 retired Pixel phones into a Kubernetes-based cluster for teaching and lightweight cloud workloads, targeting embodied carbon rather than just energy efficiency. Phone motherboards (about half a device’s embodied carbon) are stripped from cases, batteries, and peripherals, reflashed with a general-purpose Linux, and orchestrated in 25–50‑phone “micro-servers” whose per-core performance rivals data center CPUs. HN likes the technical idea but debates security, practicality, regulation on bootloader unlocking, and Google’s own recent moves to lock down Android.

---

## Comment pulse
- Root e‑waste problem → locked bootloaders, proprietary blobs, short support; regulation should mandate unlockability and code release—counterpoint: most users churn for batteries, cameras, speed, not patches.  
- Practicality doubts → dismantling, testing, tooling, and shorter remaining lifetimes may offset carbon and cost gains; extending phones’ first life might be more impactful.  
- Opportunity space → great for homelabs, education, and batch jobs; contrasts Android’s partial openness with iOS lockdown and Google’s own recent AOSP/source restrictions.

---

## LLM perspective
- View: Treating phones as mini-servers is a sensible, scalable pattern wherever workloads are modest and embarrassingly parallel.  
- Impact: Universities, small labs, and civic tech groups gain cheap, local compute; repair and right-to-unlock movements gain a concrete use case.  
- Watch next: Published power-per-job vs x86, real failure statistics, and whether regulators tie sustainability claims to bootloader-unlock and firmware openness.
