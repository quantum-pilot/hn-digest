# Microsoft terminates VeraCrypt account, halting Windows updates

- Score: 447 | [HN](https://news.ycombinator.com/item?id=47690977) | Link: https://www.404media.co/microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates/

## TL;DR
- Microsoft terminated the account VeraCrypt uses to sign Windows binaries, blocking future updates of the long‑trusted open‑source disk‑encryption tool on Windows. This exposes how FOSS projects depend on opaque, commercial code‑signing and distribution pipelines controlled by big vendors. Commenters describe similar failures with Azure Trusted Signing, speculate Microsoft is both tightening certificate abuse and nudging developers to its new signing stack, and note other driver and VPN vendors are being abruptly cut off, prompting calls for independent signing authorities and regulation.

## Comment pulse
- Azure Trusted Signing is brittle: changing eligibility, failed identity checks, no human support, leaving FOSS projects stranded until they buy non-Microsoft code-signing certificates.  
- Some see this as security tightening or damage control after abuse of certificates—counterpoint: others think it’s mainly pushing developers onto Microsoft’s new signing stack.  
- Multiple driver vendors and VPNs report sudden Partner Center terminations, fueling arguments that platform gatekeepers need regulation and independent, non-conflicted signing authorities.  

## LLM perspective
- View: This highlights that FOSS security isn’t just cryptography; it’s also governance of access to proprietary distribution and signing infrastructure.  
- Impact: Windows users may see stalled updates for niche but critical tools, incentivizing migration to Linux, macOS, or unsigned portable builds.  
- Watch next: Watch whether industry groups or foundations become neutral signers, and how EU DMA enforcement constrains Microsoft’s and Apple’s signing policies.
