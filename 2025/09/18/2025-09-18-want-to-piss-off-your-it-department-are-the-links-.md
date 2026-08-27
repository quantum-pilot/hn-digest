# Want to piss off your IT department? Are the links not malicious looking enough?

- Score: 438 | [HN](https://news.ycombinator.com/item?id=45295898) | Link: https://phishyurl.com/

### TL;DR

The small joke tool turns an ordinary destination into a redirect whose generated domain and path look deliberately malicious, with selectable themes and escalating length. It claims the resulting link merely redirects to the submitted URL. HN users enjoyed producing alarming examples, but the discussion exposed a serious lesson: corporate compliance messages, cloud senders, and security gateways often make legitimate links indistinguishable from phishing by using odd domains, urgent language, or opaque rewritten URLs. One commenter also outlined how such a redirector could later become abusive.

### Comment pulse

- Security training teaches users to inspect destinations, while link-scanning products defeat that habit by rewriting every target through unfamiliar infrastructure.
- A benign redirect can become malicious after earning trust — counterpoint: the supplied tool states that it only redirects normally.

### LLM perspective

- View: The joke works because enterprise email has already trained users that suspicious-looking links may be mandatory and legitimate.
- Impact: Inconsistent sender and redirect practices weaken human phishing heuristics, increasing both false alarms and unsafe clicks.
- Watch next: Audit open-redirect controls, destination transparency, abuse reporting, redirect immutability, and corporate email-domain consistency.
