# Volkswagen blocks Home Assistant by requiring client assertion

- Score: 366 | [HN](https://news.ycombinator.com/item?id=48319509) | Link: https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967

### TL;DR

Volkswagen’s unofficial Car-Net access stopped authenticating the Home Assistant integration while official app and browser logins still worked. Issue participants attributed the break to a client assertion or restriction on unapproved third parties across Volkswagen Group brands; existing tokens may survive temporarily, and official access may require developer registration or a commercial API. Users tested indirect routes through Tibber, Smartcar, and MQTT, but questioned durability and privacy. HN framed the lockout as an ownership and interoperability problem, invoking the EU Data Act while debating security, infrastructure cost, and hardware attestation.

### Comment pulse

- Data-access rights may offer recourse → commenters cited EU Data Act duties to provide users machine-readable, continuous product data, though enforcement appears indirect.
- Manufacturer motives divided opinion → critics saw control and monetization — counterpoint: one operator reported Home Assistant generated 20% of traffic from under 1% users.
- Workarounds shift trust elsewhere → Tibber or Smartcar may restore data, but introduce partner dependence, uncertain longevity, and additional privacy exposure.

### LLM perspective

- **View:** Cloud-only vehicle control turns purchased hardware into a revocable service whose practical capabilities depend on vendor-approved identity.
- **Impact:** Open-source integrations lose reliable access; owners either surrender automation, route data through intermediaries, or build local CAN-based alternatives.
- **Watch next:** Volkswagen registration terms, v5.4.7 behavior, token expiry, EU Data Act complaints, and whether attestation spreads across VAG brands.
