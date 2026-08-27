# NTSB report: Decryption of images from the Titan submersible camera [pdf] (2024)

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46019636) | Link: https://data.ntsb.gov/Docket/Document/docBLOB?ID=18741602&FileExtension=pdf&FileName=Underwater%20Camera%20-%20Specialist%27s%20Factual%20Report-Rel.pdf

### TL;DR

Investigators recovered Titan’s battered but sealed underwater camera and an intact SD card whose data partition used custom dm-crypt-style full-disk encryption without a LUKS header. The key was apparently stored in unencrypted UFS NVRAM on a damaged system-on-module. NTSB copied that memory onto a surrogate board and, with SubC and Canada’s TSB, used manufacturer hardware to retrieve 12 stills and nine videos. Timestamp and scene analysis showed none came from the accident voyage; the latest valid image was May 16, 2023.

### Comment pulse

- Recovery craft → investigators combined chip removal, binary imaging, hardware substitution, and manufacturer tooling despite a shattered processor.
- Operational surprise → SubC initially believed the card was unencrypted and apparently lacked clarity about its own storage stack.
- Empty payoff → extensive recovery yielded useful configuration evidence but no imagery from Mission 5 or the implosion.

### LLM perspective

- View: The report is chiefly a forensic-method case study, not new visual evidence about Titan’s loss.
- Impact: Device makers and investigators need documented key custody, storage paths, clocks, and recovery procedures before accidents.
- Watch next: Correlate external-computer evidence, camera configuration logs, manufacturing records, and remaining NTSB docket findings.
