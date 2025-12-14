# Why Twilio Segment moved from microservices back to a monolith

- Score: 115 | [HN](https://news.ycombinator.com/item?id=46257714) | Link: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices

- TL;DR  
    - Twilio Segment originally put each “destination” integration in its own microservice and repo to isolate failures and support custom transforms. At ~140 services, shared libraries, autoscaling quirks, and deployment/testing overhead turned the system into a fragile distributed monolith. They collapsed everything into a single service and monorepo, backed by a fast, recorded HTTP test suite and centralized queuing, boosting reliability and developer velocity despite weaker fault isolation. HN commenters argue much of the pain reflected organizational discipline and tooling gaps more than architecture alone.

- Comment pulse  
    - Shared libs and lockstep deploys → effectively a distributed monolith; microservices share stable APIs — counterpoint: some updates (e.g., security) must hit every service anyway.  
    - Root cause was org and tooling, not architecture → poor CI, autoscaling, oncall, and test strategy; with discipline and better platforms, microservices could have worked.  
    - Practitioners report monoliths easier for refactoring, contracts, and debugging; microservices add coordination overhead. Several want multi-service monorepos plus smarter CI instead of strict monolith/multi-repo split.

- LLM perspective  
    - View: Architecture debates hide a process lesson—without automated testing, deployment, and scaling, any style decays into fragile complexity.  
    - Impact: Teams maintaining many near-identical adapters or integrations can likely simplify into one codebase and service, slashing ops toil.  
    - Watch next: Better repo/CI partitioning, contract-testing, and schema versioning tools that let organizations get microservice benefits without drowning in coordination.
