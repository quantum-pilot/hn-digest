# FFmpeg at Meta: Media Processing at Scale

- Score: 219 | [HN](https://news.ycombinator.com/item?id=47305236) | Link: https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/

### TL;DR
Meta used to maintain a heavily modified internal FFmpeg fork to support its massive video workload (tens of billions of runs per day), mainly for multi-lane parallel transcoding and real-time quality metrics. These changes diverged from upstream and became costly to maintain. Meta then worked with FFmpeg, FFlabs, and VideoLAN to upstream multi-output parallel threading (FFmpeg 6–8) and in-loop decoding for live quality metrics (FFmpeg 7), letting them retire the fork. HN discussion praises both the engineering and open-source contributions, while criticizing the late upstreaming and marketing tone.

### Comment pulse
- Meta’s OSS stance → strong appreciation for React/React Native and upstreamed FFmpeg work — counterpoint: blog downplays years of not-upstreaming and feels spin-heavy.  
- Engineering angles → readers want time-axis parallelization and reuse of inter-frame analysis, raising questions about keyframe placement and encoder internals.  
- Economic/scale context → awe at tens of billions of FFmpeg runs and big wall-time savings; calls for Fabrice Bellard to be richly rewarded.

### LLM perspective
- View: This is a textbook case of why eliminating long-lived forks via upstream collaboration pays off at hyperscale.  
- Impact: All FFmpeg users—especially smaller platforms—inherit Meta-driven efficiency and live-quality tooling without bearing development cost.  
- Watch next: Generalized parallel encoding APIs, broader real-time metric adoption, and cleaner integration paths for proprietary accelerators without fragmenting FFmpeg.
