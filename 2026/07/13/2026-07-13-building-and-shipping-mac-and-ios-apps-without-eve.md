# Building and shipping Mac and iOS apps without ever opening Xcode

- Score: 256 | [HN](https://news.ycombinator.com/item?id=48896665) | Link: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/

### TL;DR

The post shows how to keep Xcode installed but move routine Mac and iOS development entirely to command-line tools. After one-time Apple ID, certificate, and notarization setup, XcodeGen recreates projects from YAML; xcodebuild compiles and archives; a release script signs, notarizes, staples, verifies, and installs Mac apps; and devicectl deploys signed iOS builds. Repository instructions teach coding agents which path to run. HN’s strongest concern was security: local agents need keychain and filesystem access, prompting suggestions for VMs, separate users, containers, scoped secrets, and alternative Linux-capable tooling.

### Comment pulse

- Headless automation works → standard Apple CLIs expose the whole pipeline, while checked-in scripts and agent instructions make it repeatable instead of conversational.
- Local agents expand the blast radius → signing keys and personal files share the host — counterpoint: VMs, separate users, and ACLs can isolate access.
- Apple’s toolchain is not the only route → commenters cited Linux builders and specialized CLIs offering signing, provisioning, diagnostics, or transparent dry runs.

### LLM perspective

- **View:** Executable process knowledge—scripts, declarative projects, and repository guidance—turns fragile GUI rituals into auditable automation.
- **Impact:** Teams can shorten release loops, but automation that touches signing identities must be permissioned and reviewed like production infrastructure.
- **Watch next:** Reproducible isolation, least-privilege keychain access, CI portability, certificate recovery, App Store distribution, and whether agent-generated scripts stay maintainable.
