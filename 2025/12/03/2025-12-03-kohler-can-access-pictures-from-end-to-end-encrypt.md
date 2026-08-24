# Kohler Can Access Pictures from "End-to-End Encrypted" Toilet Camera

- Score: 216 | [HN](https://news.ycombinator.com/item?id=46129476) | Link: https://varlogsimon.leaflet.pub/3m6zrw6k2bs2p?interactionDrawer=quotes

### TL;DR

Kohler’s $600 toilet-mounted health sensor sends bowl images and related data to company systems. Although marketing calls the protection end-to-end encryption, Kohler told the author that its servers decrypt and process the data; the implementation described is transport encryption plus encryption at rest, with safeguards intended to prevent employees viewing identifiable images. Terms allow de-identified data to be shared and used for business or AI training. Commenters call this misleading terminology, while proposing on-device analysis or anonymous summaries to reduce exposure.

### Comment pulse

- The dispute is semantic and substantive → servers are a processing endpoint, but ordinary users expect the provider cannot decrypt E2EE data.
- Useful results need not require raw uploads → commenters suggest local classification and transmitting only summaries.
- Privacy should begin with unlinkability → commenters prefer anonymous collection because transport encryption cannot protect data after server decryption.

### LLM perspective

- View: Security language should describe who holds decryption keys, not merely whether each network hop is encrypted.
- Impact: Buyers must evaluate consent, retention, model training, and breach exposure as medical-data risks.
- Watch next: Seek a corrected privacy claim, key-flow documentation, retention limits, deletion controls, and independent security review.
