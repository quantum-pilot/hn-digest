# Simple trick to increase coverage: Lying to users about signal strength

- Score: 427 | [HN](https://news.ycombinator.com/item?id=45795036) | Link: https://nickvsnetworking.com/simple-trick-to-increase-coverage-lying-to-users-about-signal-strength/

- TL;DR
    - Android has an undocumented CarrierConfig flag (KEY_INFLATE_SIGNAL_STRENGTH_BOOL) that lets carriers show one extra signal bar; AT&T and Verizon enable it. The post argues this, like “fake 5G” icons, erodes trust. HN readers report phones showing bars while radio metrics are unusable (e.g., −140 dBm), and share ways to see real dBm. Others note bar thresholds vary by OEM and have grown “optimistic,” partly to match iPhone displays and marketing. Bottom line: bars are branding; use dBm or diagnostics for truth.

- Comment pulse
    - Bars mislead → dBm shows reality; users saw −140 dBm with “good” bars; use *#*#INFO#*#* or apps to check — counterpoint: readings vary across devices/SIMs.
    - Industry normalization → iPhones shifted bar breakpoints over generations; others matched to avoid perception gaps; result: optimistic bars, occasional 2 bars yet zero data.
    - 5G labeling is murky → tests show ~40% “5G” icons on 4G; many run NSA without 5G core; marketing drives UX.

- LLM perspective
    - View: Exposing raw metrics beats cosmetic bars; make “Show signal in dBm/ASU” a user-facing toggle.
    - Impact: Clearer indicators reduce support churn, improve site surveys, and curb misleading 5G/UI claims through transparency standards.
    - Watch next: Android/GSMA standard for bar thresholds; carrier opt-out logs; independent audits comparing bars to dBm and throughput across devices.
