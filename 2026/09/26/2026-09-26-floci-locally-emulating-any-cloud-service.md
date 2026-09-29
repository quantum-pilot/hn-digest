# Floci: Locally emulating any cloud service

- Score: 217 | [HN](https://news.ycombinator.com/item?id=49854416) | Link: https://floci.io

### TL;DR

Floci offers MIT-licensed local emulators for AWS, Azure, GCP, and OCI, aimed especially at coding agents that need cloud APIs without credentials, bills, or production blast radius. The project claims 24-millisecond startup, 13 MiB idle memory, 180 services across four emulators, disposable state, and real engines for selected services. Supporters report lightweight integration testing and community-added compatibility; skeptics argue real cloud tests are often cheap, higher-fidelity, and necessary because emulator behavior can subtly drift from production.

### Comment pulse

- Local emulation limits agent risk → throwaway credentials and disposable state avoid accidental charges, leaked secrets, and damaged shared accounts.
- Verifiable compatibility invites distributed contribution → users can add services against test suites and objective protocol behavior.
- Emulators accelerate inner loops → lightweight integration tests run locally—counterpoint: cloud abstraction drift can create false confidence before production.

### LLM perspective

- View: Floci is most useful as a fast dependency substitute, not definitive proof of cloud compatibility.
- Impact: Developers and agents can iterate safely before reserving real-account tests for contract and end-to-end validation.
- Watch next: Conformance suites, service-depth metrics, drift tracking, security review, and sustainable sponsorship.
