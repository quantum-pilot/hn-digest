# We can’t send mail farther than 500 miles (2002)

- Score: 635 | [HN](https://news.ycombinator.com/item?id=46805665) | Link: https://web.mit.edu/jemorris/humor/500-miles

- TL;DR  
  - Campus email stopped working for recipients farther than ~500 miles. The culprit: a SunOS upgrade silently reverted Sendmail from v8 to v5, which ignored newer config options. That left the SMTP connect timeout as zero, causing connections slower than ~3 ms—about 560 miles of light-travel time on their switched network—to fail. HN readers treat this as a classic debugging parable about respecting “impossible” bug reports, valuing good user-collected data, and trading similarly strange real-world failure stories.

- Comment pulse  
  - User stats (radius map) were ideal debugging data → encourage users to share patterns. — counterpoint: story tone undersells chairman’s contribution.  
  - Classic HN staple → readers relish the improbable diagnosis and yearly rereads reinforce humility about assumptions and careful, data-driven debugging.  
  - Shared similar war stories (mouse shorting PC, video file killing laptop) → illustrates how physical quirks and edge cases can masquerade as software/network “mysteries”.

- LLM perspective  
  - View: Weird constraints often reduce to a misconfigured constant; cultivate habits of checking version mismatches and defaults first.  
  - Impact: Reminds ops and devs that absurd-sounding user patterns may encode exactly the dimension the system is sensitive to.  
  - Watch next: For AI systems, expect analogous “500-mile” bugs where latent variables create bizarre, patternful failures tied to data or hardware.
