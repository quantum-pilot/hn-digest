# Towards trust in Emacs

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47778938) | Link: https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html

- TL;DR  
Emacs 30 introduced a trust system that disables risky features, like on-the-fly Elisp diagnostics, for untrusted files, but the default creates constant friction. The trust-manager package makes trust mostly automatic: it asks once per project, pre-trusts your own config and load-path, shows a mode-line indicator for untrusted buffers, and offers simple customization. HN discussion debates usable security, unclear threat models, Emacs’s quirky handling of buffers like *scratch*, and whether editors need capability-based sandboxes instead.

- Comment pulse  
  - Security friction backfires → users bypass controls with personal machines or lax configs, arguably reducing overall safety more than the original vulnerabilities.  
  - Explain threat model first → if “trusted vs untrusted” isn’t defined, users mindlessly accept prompts or disable trust — counterpoint: some consciously accept local-risk tradeoffs.  
  - Editor trust model seen as flawed → complaints about untrusted *scratch* buffers, incoherent rules, and calls for fine-grained, capability-based sandboxes instead of blanket project trust.

- LLM perspective  
  - View: Package usefully smooths Emacs 30 usability while preserving security intent; its ideas could inform upstream defaults or alternative UIs.  
  - Impact: Emacs users get safer Elisp editing with fewer surprises, lowering incentives to disable trust features in corporate-managed environments.  
  - Watch next: Measure how often prompts appear, rates, and security incidents; refine heuristics and explore sandboxed execution for untrusted Elisp.
