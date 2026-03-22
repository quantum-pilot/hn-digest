# Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

- Score: 304 | [HN](https://news.ycombinator.com/item?id=47464134) | Link: https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/

- TL;DR  
Ubuntu 26.04 LTS switches its new Rust-based sudo-rs implementation to show asterisks for each password character, ending sudo’s 46‑year tradition of completely silent prompts. The change slightly exposes password length, but developers argue shoulder‑surfing risk is negligible compared with the usability gain, especially for newcomers and high‑latency SSH sessions. Purists can restore silence via a sudoers option. HN discussion broadens this into a debate over UX vs. “security theater” and explores alternative, more obfuscated feedback designs.

- Comment pulse  
  - Opt-out configs shared → Users document sudoers tweaks and desktop login settings (KDE, GNOME, NixOS) to disable visual echo and restore historical silent-password behavior system‑wide.  
  - Silent prompts hurt UX → Stories of failed installs, confusing resets, and high‑latency SSH sessions show no‑feedback sudo can block adoption and mask mis-typed passwords.  
  - Security tradeoff debated → Many see length leakage as minor beside keystroke logging and $5 wrenches—counterpoint: short passwords gain protection from not revealing character count.

- LLM perspective  
  - View: This marks Linux distros increasingly prioritizing sane defaults for non-experts while preserving expert control through straightforward configuration toggles.  
  - Impact: Tutorials, onboarding material, and remote-access workflows will quietly update to assume visible sudo feedback, influencing other Unix-like platforms.  
  - Watch next: Whether Red Hat, Debian, and BSDs adopt similar feedback, and how future Rust rewrites reshape Unix interface conventions.
