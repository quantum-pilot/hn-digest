# NTSB report: Decryption of images from the Titan submersible camera [pdf] (2024)

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46019636) | Link: https://data.ntsb.gov/Docket/Document/docBLOB?ID=18741602&FileExtension=pdf&FileName=Underwater%20Camera%20-%20Specialist%27s%20Factual%20Report-Rel.pdf

### TL;DR
The NTSB recovered the Titan submersible’s SubC Rayfin camera and found its SD card intact but fully encrypted with a custom dm-crypt–style full-disk setup, no LUKS header. The decryption key lived on a damaged SOM board’s UFS NVRAM, not on the card itself. After desoldering and cloning that chip to a surrogate SOM and using SubC’s own tools, investigators finally decrypted the card. Only 12 stills and 9 videos were recovered, all from test and training operations—nothing from the accident dive.

---

### Comment pulse
- OceanGate culture was disturbingly cavalier → interviews show engineers and even the engineering director believed the CEO was likely to kill himself with Titan.  
- SubC misunderstood its own product → they initially thought data was unencrypted; key was sitting in clear on UFS; odd misconfig wrote one image to /mnt/nas/Stills.  
  — counterpoint: deeper stacks and default encryption make such misunderstandings increasingly common, not just at this vendor.  
- Encryption-by-default debate → improves security but raises risk owners lose access, and complicates forensic/data-recovery work; lower-layer “hidden” encryption is widespread already.

---

### LLM perspective
- View: This is a clean case study in real-world digital forensics: encryption, damaged hardware, vendor confusion, and careful lab work.  
- Impact: Regulators and investigators need better cooperation and documentation from vendors to handle encrypted, embedded systems in accidents.  
- Watch next: Industry and safety bodies may push for recoverability standards: key-escrow, dual-recording, or black-box–style logging on crewed experimental vehicles.
