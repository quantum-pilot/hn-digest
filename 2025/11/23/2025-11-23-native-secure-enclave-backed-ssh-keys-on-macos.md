# Native Secure Enclave backed SSH keys on macOS

- Score: 278 | [HN](https://news.ycombinator.com/item?id=46025721) | Link: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf

- TL;DR  
  macOS 15 “Tahoe” quietly added native Secure Enclave–backed SSH keys via /usr/lib/ssh-keychain.dylib as a SecurityKeyProvider. You can create FIDO-style resident SSH keys tied to Touch ID using sc_auth, load them through ssh/ssh-agent/ssh-keygen, and never expose private key material outside the enclave. There’s also an exportable mode that encrypts keys with the enclave for backup and transfer. HN discussion focuses on key backup strategies, comparisons to YubiKeys/Secretive/TPM, and using SSH CAs or extended tooling for broader workflows.

- Comment pulse  
  - Non-exportable enclave keys concern some → device loss kills access; others note this matches YubiKeys and recommend multiple device keys or SSH CAs instead.  
  - sc_auth also supports an “exportable” variant → private key is enclave-encrypted, can be password-protected and re-imported elsewhere—counterpoint: exporting undermines strongest security model.  
  - Some extend enclave keys beyond SSH → patched GPG and custom agents use ECDSA-in-enclave; others clarify “private key files” here are non-secret FIDO handles.

- LLM perspective  
  - View: Using Secure Enclave as a native FIDO SecurityKeyProvider meaningfully hardens SSH auth on macOS with little user friction.  
  - Impact: Developers and ops teams gain hardware-backed keys without YubiKeys; expect gradual migration from Secretive and ad-hoc TPM integrations.  
  - Watch next: Watch for Apple docs, OpenSSH sk_enroll integration, and third-party tools leveraging biometryCurrentSet or attestation for higher-assurance SSH and code-signing.
