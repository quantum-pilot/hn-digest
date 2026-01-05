# Maybe comments should explain 'what' (2017)

- Score: 179 | [HN](https://news.ycombinator.com/item?id=46486780) | Link: https://www.hillelwayne.com/post/what-comments/

- TL;DR  
Wayne disputes the slogan that comments should describe only intent, not behavior. He argues you shouldn’t use comments to prop up unclear code, but also that pushing every explanation into identifiers, tests, or commit messages forces readers into needless context switches. Sometimes the most efficient option is a concise "what" comment placed exactly where a tricky construct appears. HN discussion converges on pragmatic guidelines: favor clarity for future maintainers, especially around domain rules, over any purist cleanliness doctrine.

- Comment pulse  
  - Domain-heavy code needs "what" comments → accounting and backup rules encode real-world conventions no name can convey—counterpoint: some insist anything tied to reality is "why".  
  - Over-extraction harms debugging → "Clean Code"–style tiny methods scatter linear logic across files; many report constant navigation pain and prefer Ousterhout’s coarser, locality-focused design philosophy.  
  - Style must serve future readers → longer names, narrative comments, and junior-dev reviews help; codebases work best as ongoing conversations, not rigidly applied cleanliness rules.

- LLM perspective  
  - View: Treat "what" vs "why" as a spectrum; optimize for reader effort at the point of maintenance, not ideology.  
  - Impact: Teams that explicitly document domain rules in-line reduce onboarding time, misinterpretations, and regressions from overzealous refactors.  
  - Watch next: Establish comment guidelines with examples; measure bug-fix duration and revert rates as comment density and decomposition patterns change.
