# We all dodged a bullet

- Score: 806 | [HN](https://news.ycombinator.com/item?id=45183029) | Link: https://xeiaso.net/notes/2025/we-dodged-a-bullet/

TL;DR
A phishing campaign (npmjs.help) hijacked maintainers of tiny, ubiquitous npm packages (e.g., color-string, color-name, is-arrayish). Injected code only redirected MetaMask crypto payments, sparing most users since many usages were CLI-only. The author argues we “dodged a bullet” and that every dependency can be malicious, yet shipping pressure limits vetting. HN pushes deeper fixes: npm’s permissive model, auto-updating editor plugins, and sprawling dependency trees magnify risk; proposals include capability-sandboxed runtimes, richer standard libraries, fewer micro-dependencies, and delaying updates. Some dispute that “anyone” would fall for the phish, urging stricter hygiene.

Comment pulse
- The ecosystem is brittle → VS Code/NX incident showed auto-updated tools exfiltrate creds despite pinning; deep JS/Python trees amplify blast radius; richer stdlibs would reduce tiny deps.
- Capability model > trust → Cloudflare workerd-style minimal permissions and isolation enforce least privilege; Deno helps but “allow all” erodes benefits — counterpoint: usability friction slows adoption.
- Update discipline as control → Two-week release quarantine cuts supply-chain risk; air-gapped dev helps, but npm’s pace and editor auto-updates erode this.

LLM perspective
- View: Make least-privilege the default: sandboxed runtimes, no network/file by default, and editor extension vetting.
- Impact: Maintainers, IDE vendors, and registries must add signing, quarantine, and reproducible builds; orgs enforce update staging.
- Watch next: npm/JS proposals for a standard library, Sigstore/TUF adoption, VS Code Marketplace malware scans, org “quarantine window” policies.
