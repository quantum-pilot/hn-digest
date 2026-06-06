# Setting up a free *.city.state.us locality domain (2025)

- Score: 461 | [HN](https://news.ycombinator.com/item?id=48122635) | Link: https://fredchan.org/blog/locality-domains-guide/

- TL;DR  
  The article explains how U.S. residents can register a free subdomain like `name.city.state.us`: find a delegated locality, get free nameservers via Amazon Lightsail, complete the old Interim .US Domain Template, email it to the locality registrar, then configure DNS (e.g., for web or game servers). Discussion highlights how fragile and bureaucratic this ecosystem is: tiny legacy registrars are disappearing, undelegated cities require notarized government letters, a new self-service portal is flaky, and .us privacy rules remain awkward.

- Comment pulse  
  - Locality domains are fragile niche infrastructure → many are run by aging one-person ISPs; when they die, renewals and transfers hit bureaucratic walls — counterpoint: some report success with polite, local notary-backed requests.  
  - Undelegated or reclaimed localities are hard to obtain → registrars now demand notarized government letters, and city staff often lack procedures, time, or incentives to help private applicants.  
  - Tooling and policy are creaky → localitymanagement.us is overloaded and buggy; .us bans WHOIS privacy, though locality WHOIS currently exposes only registrar, not registrant, details.

- LLM perspective  
  - View: Locality domains are fun, historically rich, but too fragile and manual to be a primary namespace for most users.  
  - Impact: Best for hobbyists, civic hackers, and nostalgia projects; production services should pair them with conventional TLDs.  
  - Watch next: Whether NTIA/Neustar modernize delegation rules, stabilize the portal, or communities replicate locality-style naming under independent domains.
