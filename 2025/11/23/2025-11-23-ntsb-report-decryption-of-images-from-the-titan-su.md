# NTSB report: Decryption of images from the Titan submersible camera [pdf] (2024)

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46019636) | Link: https://data.ntsb.gov/Docket/Document/docBLOB?ID=18741602&FileExtension=pdf&FileName=Underwater%20Camera%20-%20Specialist%27s%20Factual%20Report-Rel.pdf

### TL;DR

Investigators recovered an intact SD card from the Titan wreck’s damaged SubC underwater camera, but its data partition used undocumented encryption without a LUKS header. The likely key resided in unencrypted UFS storage on a shattered system module. After copying that storage onto a surrogate board and reconnecting the card to manufacturer hardware, the team recovered 12 stills and nine videos. None came from the fatal voyage: timestamps and scene correlation place them earlier, while a misconfigured network path indicates later imagery was probably stored on the submersible’s external computer.

### Comment pulse

- Default encryption surprised even the manufacturer → transparent lower-layer security complicated forensic access despite intact media and recoverable configuration storage.
- Encryption tradeoffs polarized readers → automatic protection prevents unauthorized access. — counterpoint: hidden key management can permanently lock out legitimate owners.
- The recovery proved anticlimactic → meticulous hardware reconstruction yielded only pre-accident media because operational footage was routed elsewhere.

### LLM perspective

- View: The report is a case study in recovering configuration-bound encrypted storage, not evidence from the accident itself.
- Impact: Device makers need documented recovery architecture when safety investigations may depend on transparently encrypted embedded media.
- Watch next: Recovery of the external computer, clearer key-management documentation, and whether future cameras preserve independently accessible incident data.
