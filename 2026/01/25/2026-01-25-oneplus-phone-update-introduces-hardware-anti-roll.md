# Oneplus phone update introduces hardware anti-rollback

- Score: 305 | [HN](https://news.ycombinator.com/item?id=46757944) | Link: https://consumerrights.wiki/w/Oneplus_phone_update_introduces_hardware_anti-rollback

### TL;DR

January ColorOS updates for several OnePlus, OPPO, Ace, and Pad models reportedly raise a hardware anti-rollback version by irreversibly programming Qualcomm Qfprom fuses. Once updated, flashing older firmware can fail at boot and leave recovery tools unable to restore the device without motherboard replacement. Existing custom ROMs built on older firmware are therefore dangerous, though future ROMs based on the new bootloader may remain possible. OnePlus removed downgrade packages but had issued no explanation in the supplied account.

### Comment pulse

- Anti-rollback protects the trust chain → otherwise physical attackers can reinstall signed but exploitable firmware — counterpoint: silent rollout risks hard bricks.
- Ownership is constrained → buyers cannot safely restore older software after a vendor-controlled irreversible change.

### LLM perspective

- View: The security mechanism is standard; undisclosed activation and destructive downgrade behavior are the consumer failure.
- Impact: Modders can lose devices, while ordinary users lose a recovery path they reasonably expected.
- Watch next: OnePlus guidance, compatible ROM bases, service remedies, affected regional builds, and pre-install warnings.
