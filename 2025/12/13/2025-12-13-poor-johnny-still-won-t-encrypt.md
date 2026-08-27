# Poor Johnny still won't encrypt

- Score: 73 | [HN](https://news.ycombinator.com/item?id=46251952) | Link: https://bfswa.substack.com/p/poor-johnny-still-wont-encrypt

### TL;DR

Email encryption remains nearly as awkward as in 1998: OpenPGP still demands key discovery and management, while S/MIME fits enterprises better but often requires manual PKI work and careful retention of old keys. Webmail dominance and weak MTA-STS adoption further limit protection, while stateful messengers offer forward secrecy and easier encrypted conversations. Commenters showed that managed S/MIME can work at organizational scale, yet recovery, search, interoperability, multi-device use, and long-term key custody remain decisive usability failures.

### Comment pulse

- Key backup exposes a fundamental trade-off → easy recovery can weaken hostile-device threat models, while strict ephemerality destroys valued history.
- S/MIME is viable under central administration → government smart cards and one small company demonstrate deployment, but outsiders rarely participate.
- Proton interoperability was disputed → commenters supplied public-key lookup endpoints and examples of external encrypted delivery.

### LLM perspective

- View: Cryptography is available; lifecycle management and universal recipient interoperability remain the unsolved product.
- Impact: Organizations must choose between searchable archives, recoverability, and protection from servers or compromised endpoints.
- Watch next: Measure MTA-STS adoption and test cross-provider key discovery, rotation, revocation, backup, and device replacement.
