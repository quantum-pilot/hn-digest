# Foreign hackers breached a US nuclear weapons plant via SharePoint flaws

- Score: 307 | [HN](https://news.ycombinator.com/item?id=45657287) | Link: https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html

- TL;DR
    - Attackers exploited unpatched on‑prem SharePoint spoofing and RCE flaws to breach the NNSA’s Kansas City National Security Campus, which makes 80% of non‑nuclear weapon parts. Microsoft ties the wider campaign to Chinese groups prepping ransomware; a source claims a Russian actor. DOE says impact was limited and systems restored. The incident spotlights IT‑to‑OT pivot risks and the lag in zero‑trust protections for operational tech; even unclassified manufacturing data can be strategically revealing. HN debates SharePoint’s reliability versus Microsoft’s enterprise scalability and backward compatibility.

- Comment pulse
    - Microsoft stack signals poor engineering culture → commenters see Outlook/SharePoint as red flags. — counterpoint: Ubiquity makes avoidance unrealistic; detractors resist standard tools.
    - Exchange scales and preserves backward compatibility → admins cite 70k+ users and legacy macro support; SharePoint still seen as uniquely brittle.
    - Unexpected feedback loops happen → anecdote of Excel strings triggering firewall logs and alerts; underscores audits, red-teaming, and defense-in-depth.

- LLM perspective
    - View: Patch on-prem SharePoint fast; assume compromise, monitor lateral movement, and enforce strict IT/OT segmentation with zero-trust controls.
    - Impact: NNSA contractors, DOE CIOs, and regulated critical manufacturers will revisit on-prem Microsoft deployments, patch SLAs, and OT isolation policies.
    - Watch next: Attribution clarity, CISA advisories on CVE-2025-53770/49704, DoD OT zero-trust guidance, and audits verifying air-gaps and PLC/SCADA segmentation.
