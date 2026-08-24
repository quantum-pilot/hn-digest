# 8M users' AI conversations sold for profit by "privacy" extensions

- Score: 776 | [HN](https://news.ycombinator.com/item?id=46284266) | Link: https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection

### TL;DR

Koi Security reports that eight Chrome and Edge extensions from Urban VPN’s publisher, installed by more than eight million users, captured AI chats. Injected scripts reportedly intercepted prompts, responses, timestamps, identifiers, and model metadata across major assistants, then sent compressed records to Urban servers even when VPN or protection features were off. Koi says collection arrived in a default-enabled July 2025 update, was disclosed misleadingly as protective functionality, and was connected to affiliated data broker BiScience. Uninstalling was the only opt-out.

### Comment pulse

- Readers favored runtime, site-specific permissions and clearer exfiltration controls over broad install-time consent that silently survives extension updates.
- Mozilla’s reviewed-extension program drew praise — counterpoint: Urban VPN also passed manual review, and reviewers may not inspect every update.
- Commenters warned that corporate registration and polished legal pages reveal little about an extension operator’s actual incentives.

### LLM perspective

- View: Browser extension permissions remain dangerously coarse for tools able to observe authenticated web sessions.
- Impact: Silent chat capture can expose personal, professional, and proprietary information at mass scale.
- Watch next: Store removals, regulator action, publisher response, affected versions, and browser permission redesigns.
