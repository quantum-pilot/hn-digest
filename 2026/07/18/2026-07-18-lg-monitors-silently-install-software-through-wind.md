# LG monitors silently install software through Windows Update without consent

- Score: 968 | [HN](https://news.ycombinator.com/item?id=48956688) | Link: https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent

### TL;DR

Windows Update can associate certain LG monitors with LG Monitor App Installer and silently install it without an approval prompt. Gamers Nexus reproduced the chain on a new UltraGear and a three-year-old UltraFine; across 32 boots, the app promoted a McAfee trial 31 times and an LG utility once. The Store listing grants internet and broad system-resource access. Dell and other peripheral vendors use the same device-metadata channel. HN blamed both LG for abusing trusted distribution and Microsoft for enabling it, while noting the practice is longstanding rather than unprecedented.

### Comment pulse

- Responsibility is shared → Windows initiates and trusts the package, while LG deliberately uses that channel to deliver unrelated subscription advertising.
- Novelty claims drew correction → peripherals have triggered manufacturer packages for years — counterpoint: LG’s persistent promotion made the abuse unusually visible.
- Blocking metadata apps is possible but obscure → Group Policy or Device Installation Settings can disable downloads, also preventing legitimate companion software.

### LLM perspective

- **View:** The security boundary is not the cable but Windows’ policy decision to translate hardware identity into privileged software installation.
- **Impact:** A trusted driver channel becomes an advertising and privacy risk when downloaded package scope exceeds what the hardware requires.
- **Watch next:** Seek Microsoft enforcement, LG removal, narrower permissions, explicit consent, enterprise controls, uninstall testing, and affected-model disclosure.
