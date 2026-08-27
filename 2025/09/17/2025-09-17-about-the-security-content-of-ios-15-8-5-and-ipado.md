# About the security content of iOS 15.8.5 and iPadOS 15.8.5

- Score: 346 | [HN](https://news.ycombinator.com/item?id=45270108) | Link: https://support.apple.com/en-us/125142

### TL;DR

Apple released iOS and iPadOS 15.8.5 for older devices including the iPhone 6s, iPhone 7, first-generation iPhone SE, iPad Air 2, iPad mini 4, and seventh-generation iPod touch. The update fixes CVE-2025-43300, an ImageIO out-of-bounds write where processing a malicious image could corrupt memory. Apple says it knows of a report that the flaw may have been used in an extremely sophisticated attack against specific targets. The notice supplies no exploit-chain or victim details.

### Comment pulse

- Commenters praise support for old hardware but debate how Apple’s unspecified window compares with newer Android vendors’ commitments.
- Readers infer serious targeted spyware risk, though broader exploit-chain claims in comments exceed Apple’s brief advisory.

### LLM perspective

- View: Backporting this ImageIO fix matters because image parsers expose long-lived devices to potentially low-interaction attacks.
- Impact: Owners of supported legacy devices gain protection, but the advisory’s sparse detail limits independent assessment of exposure.
- Watch next: Further vendor disclosures, related vulnerability patches, and whether Apple extends fixes to any additional legacy releases.
