# Show HN: Bor – Open-source policy management for Linux desktops

- Score: 167 | [HN](https://news.ycombinator.com/item?id=49142569) | Link: https://getbor.dev/blog/2026-08-02-bor-v080-release/

### TL;DR
Bor is an open-source Linux desktop policy manager that pushes centrally defined settings to enrolled machines via mTLS‑secured gRPC agents, avoiding SSH and arbitrary remote scripts. It targets organizations wanting Windows‑style group policy for GNOME/KDE and browsers, with tamper‑resistant files, real‑time drift correction, and integration with LDAP/AD/FreeIPA rather than replacing them. HN discussion focuses on comparisons with Ansible and Samba GPO, security trade‑offs of not supporting custom scripts, and suitability for schools, nonprofits, and enterprises.  

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Need Linux Intune alternative → admins like centralized, DE‑aware policies but want custom scripts and SSO integration — counterpoint: author prioritizes security, avoiding RCE-style agents.  
- Positioning vs Samba GPO and Ansible → Bor adds UI, tamper protection, native lockdown mechanisms, and avoids coding policies as scripts, appealing to AD‑centric admins.  
- Architecture choice mTLS/gRPC push → outbound agents through NAT, no SSH surface; inotify plus app‑level locks revert or block user/root configuration drift quickly.  

---

### LLM perspective
- View: Treating policies as declarative, non‑scriptable state is safer and more auditable than remote‑execution‑driven configuration management for endpoints.  
- Impact: Could standardize Linux desktop management in education and SMEs, reducing Windows lock‑in where Intune/Group Policy were the deciding factors.  
- Watch next: Robust Cinnamon, XFCE, and browser coverage, third‑party audits of the CA/agent model, and integrations with SAML/OIDC identity providers.
