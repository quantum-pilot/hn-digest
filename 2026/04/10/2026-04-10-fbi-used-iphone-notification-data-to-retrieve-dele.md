# FBI used iPhone notification data to retrieve deleted Signal messages

- Score: 559 | [HN](https://news.ycombinator.com/item?id=47716490) | Link: https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/

### TL;DR

Trial testimony says the FBI recovered incoming Signal message previews from an iPhone’s internal notification storage after the app had been deleted. Outgoing messages were absent. The defendant allowed notification content, so iOS retained plaintext previews; Signal offers “Name Only” or “No Name or Content” settings. The exact phone state and extraction method remain unknown, with a backup one possibility, and neither Apple nor Signal commented. Commenters argued end-to-end encryption cannot protect plaintext exposed to operating-system services, backups, or compromised endpoints, and that privacy-preserving defaults matter more than optional controls.

### Comment pulse

- The relevant preview control lives inside Signal, not iOS; changing only system display settings may still leave content in storage.
- Median users keep defaults, so secure messengers should omit or encrypt notification payloads — counterpoint: previews provide meaningful everyday usability.
- Court testimony can expose real forensic capability, though agencies sometimes drop cases or use parallel construction to conceal techniques.

### LLM perspective

- **View:** Message transport remained encrypted; the failure arose after decryption, where an integrated operating-system feature created another durable copy.
- **Impact:** Users with endpoint seizure risk must treat notifications, backups, summaries, and paired devices as part of their threat model.
- **Watch next:** Apple’s token-validation change, notification retention rules, backup protection classes, Signal defaults, payload encryption, and independent forensic testing.
