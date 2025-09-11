# ICE is using fake cell towers to spy on people's phones

- Score: 651 | [HN](https://news.ycombinator.com/item?id=45184368) | Link: https://www.forbes.com/sites/the-wiretap/2025/09/09/how-ice-is-using-fake-cell-towers-to-spy-on-peoples-phones/

TL;DR
Forbes reports an unsealed warrant showing ICE deployed a cell-site simulator (“Stingray”) in Utah to precisely locate a deportee who’d escaped a Venezuelan prison. After coarse carrier location data, agents sought court approval for the device. Records show ICE bought ~$1M in “cell site simulator vehicles” and maintains up to $4.4M in contracts with Harris, indicating ongoing, mobile use under Biden. Separate scans at a Washington protest detected IMSI-catcher-like activity. HN discusses DIY detection tools, trust risks, and 5G SA mitigations.

Comment pulse
- DIY detection is possible (EFF Rayhunter, Snoopsnitch) → cheap hardware, but supply-chain trust in GitHub/Microsoft questioned; phones should warn on rogue towers.
- SAN saw IMSI bursts at an ICE protest → consistent with Stingrays; attach-rejects can be benign — counterpoint: chilling effect on protests.
- Locking to 5G standalone reduces IMSI-catcher downgrades → T-Mobile supports SA on iOS 17+ if provisioned; coverage gaps still force fallbacks.

LLM perspective
- View: ICE’s Stingray use persists with warrants and new mobile platforms, raising collateral collection risks in populated areas and protests.
- Impact: Targets, bystanders, and First Amendment activities; vendors gain revenue; carriers and OS vendors face pressure for mitigations and transparency.
- Watch next: FOIA releases on warrants and logs; court challenges to CSS at protests; handset features like baseband alerts and SA-only modes.
