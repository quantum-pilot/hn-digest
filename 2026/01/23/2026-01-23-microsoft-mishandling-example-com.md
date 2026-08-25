# Microsoft mishandling example.com

- Score: 223 | [HN](https://news.ycombinator.com/item?id=46731996) | Link: https://tinyapps.org/blog/microsoft-mishandling-example-com.html

### TL;DR

Testing a dummy address revealed that Outlook’s Autodiscover service maps the reserved example.com domain to Sumitomo Electric mail servers. The behavior reproduced across Windows, macOS, networks, profiles, DNS resolvers, and a cloud PC even though the domain has a null MX and no discovery records. Microsoft’s API returned unvalidated IMAP and SMTP endpoints; decoded metadata dates the database mapping to February 2020. The author warns that test credentials could reach an unrelated company. Commenters also questioned Outlook’s broader practice of routing external mail credentials through Microsoft.

### Comment pulse

- Cloud-mediated mail expands the trust boundary → commenters reported Outlook sending private-server credentials through Microsoft and making connections outside interactive use.
- The mapping suggests failed ownership validation → a reserved domain reached real mail servers — counterpoint: commenters could only speculate about the cause.
- Reserved namespaces require historical care → old Active Directory guidance later collided with multicast DNS, though that usage predated the reservation.

### LLM perspective

- View: Autodiscovery should not override authoritative DNS with an unvalidated provider mapping.
- Impact: Testers may expose credentials, while administrators cannot infer the actual connection path from domain records.
- Watch next: Mapping removal, ownership verification, reserved-domain blocks, credential-flow disclosure, and regression tests.
