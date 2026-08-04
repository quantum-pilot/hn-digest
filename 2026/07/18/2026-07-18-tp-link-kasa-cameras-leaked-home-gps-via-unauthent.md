# TP-Link Kasa cameras leaked home GPS via unauthenticated UDP for 6 years

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48952565) | Link: https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md

### TL;DR

Research on TP-Link’s Kasa EC71 found that firmware 2.3.26 answered an unauthenticated UDP request on port 9999 with precise, persistent home coordinates, device identifiers, and alias. Identical GPS exposure was documented in 2020. The flaw was LAN-local, but factory resets left prior-owner coordinates available through setup Wi-Fi; flash also retained plaintext email and an unsalted MD5 password hash. Researchers extracted fleet-wide RSA private keys, though active interception was not demonstrated. Firmware 2.4.1 removed the GPS response, encrypted credentials, and provisioned per-device keys. EC70 v4 and EC71 v4 are confirmed affected.

### Comment pulse

- Severity hinged on threat model → LAN attackers may infer location already — counterpoint: secondhand devices exposed previous owners through setup Wi-Fi after factory reset.
- Network containment remains valuable → VLANs and router blocks reduce exposure — counterpoint: cloud-dependent devices often lose core functions when isolated.
- Disclosure was operationally rough → six months brought mistaken triage, missed updates, rollout instability, and a beta that permanently bricked the researcher’s camera.

### LLM perspective

- **View:** Sensitive data surviving reset transformed ordinary resale into a path for recovering the previous owner’s location and credentials.
- **Impact:** A single device compromise could expose fleet cryptographic material and a reusable TP-Link identity, expanding risk beyond the camera.
- **Watch next:** Confirm 2.4.1 rollout, reset sanitization, wider model scope, key uniqueness, token revocation, user notice, and regression testing.
