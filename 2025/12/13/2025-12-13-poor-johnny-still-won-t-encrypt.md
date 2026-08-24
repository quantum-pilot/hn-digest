# Poor Johnny still won't encrypt

- Score: 73 | [HN](https://news.ycombinator.com/item?id=46251952) | Link: https://bfswa.substack.com/p/poor-johnny-still-wont-encrypt

### TL;DR

End-to-end email encryption remains almost as awkward as it was in 1998. OpenPGP still demands key discovery and management, while webmail displaced desktop clients that offered better support. S/MIME fits enterprise PKI and has wider client adoption, but Microsoft deployments remain manual and poorly documented. Meanwhile, low MTA-STS adoption leaves transport encryption largely opportunistic and downgradeable. Email’s replacements differ: Signal adds replay resistance, forward secrecy, and post-compromise protection; Slack and Teams remain readable by their servers. HN focused on backups, interoperability, and long-term key custody.

### Comment pulse

- Government smart cards and a small company’s long-running S/MIME deployment show organizations can encrypt, but search, webmail, peer adoption, and archives suffer.
- Key recovery split threat models: some accept ephemeral history; others want replicated encrypted backups resilient to lost devices without creating an exploitable recovery path.
- Proton interoperability criticism drew a concrete correction: public keys are retrievable and outside senders can encrypt, though outgoing defaults remain confusing.

### LLM perspective

- View: The unsolved problem is durable, comprehensible key lifecycle management across people and devices, not cryptographic primitives.
- Impact: Sensitive mail remains readable to providers or becomes inaccessible to owners when organizational key custody fails.
- Watch next: Automatic key discovery, recoverable multi-device stores, enforced transport policies, searchable local decryption, and managed S/MIME automation.
