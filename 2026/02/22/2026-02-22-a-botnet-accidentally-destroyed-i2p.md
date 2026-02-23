# A Botnet Accidentally Destroyed I2P

- Score: 148 | [HN](https://news.ycombinator.com/item?id=47106985) | Link: https://www.sambent.com/a-botnet-accidentally-destroyed-i2p-the-full-story/

- TL;DR  
  A massive IoT botnet, Kimwolf, tried to repurpose the I2P anonymity network as backup command-and-control in February 2026, injecting ~700k nodes into a network that normally has ~15–55k. The flood effectively Sybil-attacked and crippled I2P, initially misattributed to recurring state actors who have hit it every February. Botnet operators later admitted the collateral damage was accidental. I2P’s developers responded within six days with version 2.11.0, adding default post-quantum crypto and new Sybil mitigations.

- Comment pulse  
  Article lacks technical depth → commenters recommend Krebs’ longer investigation for protocol details, attack mechanics, and clearer numbers.  
  Resilience questioned → some argue anonymity networks should tolerate huge hostile majorities; others note decentralized spam/Sybil resistance remains unsolved at these scales.  
  Threat framing debated → state campaigns target I2P for dissident traffic; yearly attacks may track budget cycles, while “hostile vs normal” use blurs when C2 traffic overloads infrastructure.

- LLM perspective  
  View: Commodity IoT botnets now unintentionally endanger privacy infrastructure, not just traditional web services, demanding new design assumptions.  
  Impact: I2P’s rapid PQC rollout and Sybil defenses set a precedent; similar networks may feel pressured to harden faster.  
  Watch next: detailed technical postmortems, empirical Sybil-resistance benchmarks, and whether C2 operators continue experimenting with anonymity networks after this failure.
