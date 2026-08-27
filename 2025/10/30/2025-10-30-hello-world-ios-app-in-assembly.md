# Hello-World iOS App in Assembly

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45755821) | Link: https://gist.github.com/nicolas17/966a03ce49f949dd17b0123415ef2e31

### TL;DR

A compact ARM64 assembly program demonstrates an iOS application that launches through UIKit and displays a yellow view. It manually builds an Objective-C `AppDelegate` class at runtime, registers the launch method, creates a window and view controller, sends Objective-C messages, and manages an autorelease pool and calling conventions. The experiment exposes machinery normally hidden by Swift or Objective-C, but remains dependent on high-level Apple frameworks. The supplied gist lacks build and deployment instructions and drew low-level correctness questions.

### Comment pulse

- Supporters valued assembly as a way to inspect abstraction costs and runtime behavior.
- Skeptics noted UIKit, Core Animation, and the Objective-C runtime remain substantial abstractions, limiting “bare metal” claims.

### LLM perspective

- View: This is an educational boundary-crossing exercise, not evidence that assembly is practical for ordinary iOS development.
- Impact: Readers can see how ABI rules, dynamic dispatch, and application lifecycle connect beneath language tooling.
- Watch next: Add reproducible build steps, verify register preservation, document signing, and compare binary size with C or Swift.
