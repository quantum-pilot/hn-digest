# Don't use passkeys for encrypting user data

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47189749) | Link: https://blog.timcappalli.me/p/passkeys-prf-warning/

## TL;DR
Author warns against using WebAuthn passkeys, via the PRF extension, as keys for encrypting long‑lived user data like backups or wallets. Authentication credentials are designed to be reset; encryption keys are not, so deleting or losing a passkey can silently destroy irreplaceable data. They urge the industry to reserve passkeys for phishing‑resistant login, or at least add clear warnings and documentation. HN commenters debate passkey UX, platform lock‑in, and whether this risk is unique to passkeys or to all encryption.

## Comment pulse
- Passkeys create UX footguns → users don’t know where credentials live, cross‑device behavior is inconsistent, and accidental creation/deletion feels worse than passwords plus a manager.  
- Auth vs encryption mismatch → passkeys feel disposable, but PRF‑derived keys can be irreplaceable; designers should add keys and not rely on a single credential.  
- Risk debated → some say data‑loss scenarios are unrealistic or generic to encryption; others report relatives deleting stored credentials accidentally—counterpoint: clearer warnings might reduce this.  

## LLM perspective
- View: Treat passkeys as one factor in a recovery‑friendly key hierarchy; never the sole key protecting long‑term, irreplaceable data.  
- Impact: Messaging apps, wallets, and cloud backup providers should re‑evaluate architectures that bind data directly to a single WebAuthn credential.  
- Watch next: An “encryption‑critical” flag for passkeys, UX studies on deletion flows, and reference designs for multi‑key recovery patterns.
