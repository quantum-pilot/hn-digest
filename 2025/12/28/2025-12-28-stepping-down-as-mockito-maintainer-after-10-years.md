# Stepping down as Mockito maintainer after 10 years

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46414078) | Link: https://github.com/mockito/mockito/issues/3777

### TL;DR
After nearly a decade maintaining Mockito, the lead maintainer plans to step down in 2026. He cites the draining Java 22 agent change, Kotlin’s JVM “shenanigans” complicating Mockito’s core, and finding more joy contributing to Rust/Servo as key reasons. The post highlights how platform decisions and Kotlin’s design shift complexity onto unpaid volunteers. HN commenters mainly express sympathy, debate mocking’s architectural downsides, worry about Mockito’s Kotlin future, and criticize the JVM platform team’s handling of agent changes.

### Comment pulse
- Maintainer burnout is understandable → running a dominant OSS library for a decade, under pressure from platform shifts, is exhausting and under-rewarded.  
- Mocks aren’t the villain → overuse enables convoluted architectures and unreadable tests, but disciplined layering and clear test plans keep Mockito productive.  
- JVM agent change mishandled → commenters see Mockito scapegoated for security tightening, with poor tooling and consultation—counterpoint: platform teams must prioritize ecosystem safety.  

### LLM perspective
- View: Maintainer’s exit showcases systemic fragility: critical ecosystem tools depend on a few volunteers absorbing platform and language churn.  
- Impact: Java and Kotlin teams, plus companies relying on Mockito, must invest more in stewardship, migration tooling, and alternative testing approaches.  
- Watch next: Track successor maintainers, Java agent build tooling, and whether Kotlin-focused frameworks like MockK gain share as ecosystems respond.
