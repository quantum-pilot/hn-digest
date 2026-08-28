# CocoaPods trunk read-only plan

- Score: 248 | [HN](https://news.ycombinator.com/item?id=45091493) | Link: https://blog.cocoapods.org/CocoaPods-Specs-Repo/

### TL;DR

CocoaPods plans to make its central trunk permanently read-only on December 2, 2026, after notification emails and a November test window. Existing specifications and builds should remain available through GitHub and jsDelivr, but trunk will accept no new pods or versions. Private spec repositories and vendored dependencies remain unaffected. A May 2025 security change already blocks new pods using `prepare_command`, while grandfathering existing ones. The schedule is intentionally long and may move later if necessary.

### Comment pulse

- Many thanked maintainers for preserving builds while giving the Apple ecosystem ample migration time.
- Swift Package Manager experiences were sharply divided: some reported crashes and missing features; others found it dramatically simpler than CocoaPods.
- Former users welcomed removing CocoaPods’ workspace, Ruby, CDN, and release-management complexity.

### LLM perspective

- View: Freezing the registry converts an open-ended security burden into a stable historical archive.
- Impact: Maintainers must publish elsewhere before the cutoff; consumers can keep old builds but lose trunk updates.
- Watch next: Notification reach, the November test’s breakage reports, and whether SwiftPM closes disputed workflow gaps.
