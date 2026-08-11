# What Is OAuth?

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47096520) | Link: https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b

### TL;DR

OAuth began as a standard replacement for incompatible, insecure ways of letting third-party clients act on a user’s account without receiving the user’s password. Its core is delegated authorization: with consent, a service issues a reusable secret to a known client, which uses it for later requests on the user’s behalf. OpenID Connect layers sign-in on top, conceptually resembling a magic link. Commenters agreed this three-party model is simple, but debated whether OAuth 2’s many grants, extensions, provider quirks, and scattered specifications make the framework needlessly difficult.

### Comment pulse

- OAuth 2’s modularity covers browsers, devices, machines, and public clients — counterpoint: interoperability often still requires provider-specific registration and code.
- Several practitioners preferred its evolving components to SAML’s monolith, because applications can consume tokens without caring which grant produced them.
- Readers suggested learning from the resource holder’s perspective: a user authorizes one service to access selected resources held by another.
