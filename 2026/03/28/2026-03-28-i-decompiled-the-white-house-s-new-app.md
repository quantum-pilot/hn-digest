# I decompiled the White House's new app

- Score: 338 | [HN](https://news.ycombinator.com/item?id=47555556) | Link: https://thereallo.dev/blog/decompiling-the-white-house-app

### TL;DR

A decompilation describes the White House Android app as an Expo/React Native front end over WordPress APIs. It found WebView JavaScript that hides consent, login, and paywall elements; third-party code from GitHub Pages and Elfsight; extensive OneSignal profiling hooks; and development artifacts in production. The headline location claim—a compiled pipeline polling every 4.5 minutes—is not shown reachable or active. HN testers saw no location request, noted Android requires manifest declarations, and argued the code may be an unused OneSignal SDK component that React Native tree-shaking failed to remove.

### Comment pulse

- Static code presence was mistaken for behavior — counterpoint: the WebView injection and remote-script dependencies still warrant runtime verification.
- Reviewers said Android cannot request undeclared location permissions; version targeting or rapid patches were suggested but unconfirmed.
- No certificate pinning enables interception by trusted compromised or enterprise CAs, not arbitrary attackers presenting self-signed certificates.

### LLM perspective

- **View:** The investigation surfaces credible attack surfaces, but reachability analysis and device testing must precede claims about behavior.
- **Impact:** Government apps merit stricter dependency, consent, and provenance standards because perceived authority amplifies ordinary marketing-stack risks.
- **Watch next:** Reproducible APK hashes, cross-version manifests, dynamic traffic traces, WebView isolation, and an official remediation response.
