# iOS 18.6.1 0-click RCE POC

- Score: 228 | [HN](https://news.ycombinator.com/item?id=45019671) | Link: https://github.com/b1n4r1b01/n-days/blob/main/CVE-2025-43300.md

### TL;DR

A proof of concept modifies two bytes in a particular DNG image and sends it to an iPhone, apparently reaching an out-of-bounds write in Apple’s stripped JPEG lossless decompression code within RawCamera.bundle. The author could not reproduce the path with ordinarily converted DNGs and infers that iOS 18.6.2 fixed the same flaw because the file no longer crashes it. Crucially, commenters stress that this demonstration appears to provide denial of service, not a completed remote-code-execution chain.

### Comment pulse

- Readers discussed Lockdown Mode, forensic backup scanning, BlastDoor, daily reboots, and the limits of each mitigation.
- Commenters described fuzzing and reverse engineering as common discovery methods and noted Apple’s history of image-parser vulnerabilities.

### LLM perspective

- View: The byte-level crash is credible evidence of unsafe parsing, but the headline overstates what this proof demonstrates.
- Impact: Interactionless media decoding makes even a crash-only primitive important because attackers may combine it with other vulnerabilities.
- Watch next: Await a traced code path, affected-version matrix, exploitability analysis, and confirmation linking the sample to the patched CVE.
