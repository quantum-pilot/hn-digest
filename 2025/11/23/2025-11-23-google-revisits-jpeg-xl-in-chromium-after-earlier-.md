# Google Revisits JPEG XL in Chromium After Earlier Removal

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46021179) | Link: https://windowsreport.com/google-revisits-jpeg-xl-in-chromium-after-earlier-removal/

### TL;DR

Chromium has reopened consideration of JPEG XL three years after Chrome removed it for insufficient ecosystem interest. A feature-complete contribution reportedly adds animation and passes most tests, but remains under review, unavailable to users, and dependent on maintenance and launch requirements. Safari, a Windows extension, PDF adoption, and continuing requests strengthen the format’s case. Commenters stressed that Chrome is welcoming outside work rather than promising implementation, and that the submitted C++ decoder may be unacceptable while Google Research develops a Rust alternative.

### Comment pulse

- Ecosystem momentum → Safari, PDF, imaging workflows, and continued requests weaken the earlier claim that JPEG XL lacked adoption.
- Security boundary → Chrome may require a maintained Rust decoder rather than accept the existing C++ integration.
- Codec trade-off → JPEG XL offers speed and maturity — counterpoint: newer AV-family codecs may improve compression at greater compute cost.

### LLM perspective

- View: Reopening review is meaningful policy movement, but it is not equivalent to scheduled Chrome support.
- Impact: Publishers cannot rely on JPEG XL broadly until Chromium ships interoperable decoding by default.
- Watch next: Track jxl-rs completeness, code review, maintenance ownership, animation tests, Firefox posture, and launch milestones.
