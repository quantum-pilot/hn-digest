# Google will allow only apps from verified developers to be installed on Android

- Score: 3050 | [HN](https://news.ycombinator.com/item?id=45017028) | Link: https://9to5google.com/2025/08/25/android-apps-developer-verification/

- TL;DR
    - Google will require developer identity verification for any app installed on certified Android devices—including via third‑party stores and sideloading. Verification access starts in October; opens to all March 2026; enforcement begins Sept 2026 in Brazil, Indonesia, Singapore, Thailand and goes global in 2027. Google cites 50× more malware from internet sideloading, adds a new console and a separate flow for students/hobbyists, and says this isn’t content review. HN worries center on lock‑in via Play Integrity, friction for indie devs, and killing modded clients; a few note benefits against impostor apps.

- Comment pulse
    - Locks in Google via Play Integrity/attestation → banks and regulated apps refuse non‑certified/custom ROMs like GrapheneOS.
    - Security gains are marginal; real target is modded/gray apps (ReVanced/NewPipe) → bad actors can pass KYC; indies risk bans — counterpoint: identity/signature checks deter impostor banking apps.
    - Push for device owner rights → calls for right‑to‑root/maintain; some adopt two‑device setups; a third mainstream mobile OS remains impractical.

- LLM perspective
    - View: Likely an Android‑wide notarization layer enforced via Play Protect and package signatures, not per‑app content review.
    - Impact: Third‑party stores must integrate checks; enterprise sideloading pipelines need notarization; FOSS projects face KYC/identity exposure.
    - Watch next: Can users disable checks? Verification costs/KYC burden, FOSS exemptions, attestation tie‑ins, DMA/antitrust responses, post‑rollout malware metrics.
