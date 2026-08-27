# FFmpeg has issued a DMCA takedown on GitHub

- Score: 543 | [HN](https://news.ycombinator.com/item?id=46394327) | Link: https://twitter.com/FFmpeg/status/2004599109559496984

### TL;DR

An FFmpeg developer pursued a GitHub DMCA takedown after Rockchip allegedly copied thousands of FFmpeg lines, removed licensing or attribution, and failed to correct the violation for nearly two years. HN commenters clarified that the core issue is not simply static versus dynamic linking: the LGPL can permit static use when recipients can relink modified library versions. Rockchip instead lacked authority to relicense FFmpeg code under Apache 2.0. The proper structure would preserve LGPL notices and separate modified FFmpeg code into an appropriately licensed component or fork.

### Comment pulse

- LGPL does not mandate dynamic linking → compliance can instead provide object files or another practical relinking path.
- Delay exhausted maintainers’ patience → archived discussion suggested Rockchip repeatedly prioritized new chip work over licensing repairs.
- AI raised a parallel concern → generated code remains infringing when it reproduces protected implementation beyond permissible similarity.

### LLM perspective

- View: License compatibility is irrelevant when copied code is stripped of its actual copyright terms and attribution.
- Impact: Hardware vendors integrating upstream multimedia code must fund compliance work alongside product development.
- Watch next: Repository restoration, corrected licensing, source separation, and Rockchip’s response to the takedown will show remediation quality.
