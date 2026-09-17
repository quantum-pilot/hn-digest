# Hackers Got Inside a Flock Camera

- Score: 535 | [HN](https://news.ycombinator.com/item?id=49726586) | Link: https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/

### TL;DR

A hacker collective physically removed a Flock license-plate camera and recovered much of its storage, including an on-device key that unlocked videos and stills. Analysis found roughly 1.6 million images of 50,200 vehicles across 21 logged days, person-detection code, short video clips, and repeated storage failures. Most sensitive storage remained inaccessible, and investigators found no active facial recognition. Flock condemned the removal and requested responsible disclosure. HN discussion centered on inadequate physical-threat modeling, encryption design, and whether Flock’s disclosure policy is meaningfully usable.

### Comment pulse

- Public placement makes physical access foreseeable → secure boot and device-specific key management should assume attackers can obtain complete hardware.
- Collection exceeded public expectations → recovered video and person detection challenge descriptions of the devices as mere plate readers.
- Disclosure restrictions divide researchers → critics call Flock’s policy performative—counterpoint: prohibiting tests against customer cameras and routine configuration reports is common.

### LLM perspective

- View: The breach reveals both excessive collection and a mismatch between stated encryption assurances and recoverable local data.
- Impact: Communities evaluating ALPR contracts now have concrete evidence about capture volume, object detection, and operational reliability.
- Watch next: Seek independent reproduction, key-management remediation, retention details, fleet-wide exposure analysis, and contractual security audits.
