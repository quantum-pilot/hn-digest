# Proton meet isn't what they told you it was

- Score: 159 | [HN](https://news.ycombinator.com/item?id=47624558) | Link: https://www.sambent.com/proton-meet-isnt-what-they-told-you/

### TL;DR
The article argues that Proton Meet’s core privacy marketing is misleading: while end-to-end content encryption via MLS appears real and Swiss-hosted, all call routing uses LiveKit Cloud, a California company running on US platforms (Oracle, AWS, etc.). LiveKit is an independent data controller for call records and telemetry, explicitly cooperating with US law enforcement under the CLOUD Act, and its telemetry always goes to the US. Proton also sets a 90‑day tracking cookie and downplays LiveKit’s role in its main privacy policy, despite promising “no tracking” and “not even government agencies” access. HN readers mostly agree the presentation is awful, but debate how serious the metadata risk is, given E2EE and realistic threat models.

---

### Comment pulse
- Article is structurally unreadable and feels like a hit piece → focus on LiveKit use without quantifying actual incremental risk or asking Proton.  
- Some say “US infra = bad” is oversimplified → content is E2EE; primary exposure is metadata and CLOUD Act access to logs—counterpoint: that’s exactly many users’ threat model.  
- Broader debate: privacy claims are inherently fragile due to client updates and hardware backdoors → others argue privacy is incremental, and Proton remains better than mainstream options.

---

### LLM perspective
- View: The real issue is marketing overreach vs. architecture reality, not that Proton Meet is uniquely “bad.”  
- Impact: High‑risk users (journalists, activists, regulated orgs) may wrongly assume immunity from US legal reach.  
- Watch next: Proton’s response, technical options for EU-only routing/telemetry, and clearer, threat-model-specific disclosures in their marketing and policies.
