# LinkedIn scans for 6,278 extensions and encrypts the results into every request

- Score: 359 | [HN](https://news.ycombinator.com/item?id=47967262) | Link: https://404privacy.com/blog/linkedin-is-scanning-your-browser-extensions-this-is-how-they-use-the-data/

### TL;DR
LinkedIn runs a hidden extension scan in Chrome, probing 6,278 known extensions via `chrome-extension://` URLs and logging which ones succeed. Those results, plus 48 other device/browser traits, are encrypted and attached as a header to every subsequent LinkedIn API call in your session. Because LinkedIn already knows your real identity and employer, this effectively ties sensitive inferences (job hunting, politics, religion, disabilities, corporate tooling) to named individuals and organizations. EU regulators are treating it as a potential criminal, not just privacy, issue.

---

### Comment pulse
- This is covert, identity-linked fingerprinting → lets LinkedIn infer job search, beliefs, health, income from extensions—counterpoint: some argue it’s “just” anti-scraping defense.  
- Mechanism blame on Chrome → web pages brute-force `web_accessible_resources` to detect extensions; Brave blocks this, highlighting browser design as a root problem.  
- Practice seen as industry-standard → device fingerprints using extension lists are widespread for fraud prevention, but many say LinkedIn’s scale and opacity cross a red line.

---

### LLM perspective
- View: The real issue is identity linkage; anti-fraud rationales don’t justify undisclosed, sensitive-profiling tied to real names.  
- Impact: Browsers, regulators, and enterprises will reassess extension models, fingerprinting norms, and vendor due-diligence for employee tools.  
- Watch next: DMA enforcement, outcomes of the Bavarian investigation, and browser changes limiting `chrome-extension://` probing and high-entropy fingerprints.
