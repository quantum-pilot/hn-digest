# JMAP for Calendars, Contacts and Files Now in Stalwart

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45672336) | Link: https://stalw.art/blog/jmap-collaboration/

### TL;DR

Stalwart says it now implements JMAP protocols for calendars, contacts, address books, file storage, and sharing, extending its existing mail support into a unified JSON-over-HTTPS groupware stack. The project positions JMAP, JSCalendar, and JSContact as cleaner successors to fragmented DAV, iCalendar, and vCard technologies, and calls itself feature-complete while preparing database, performance, and stability work for version 1.0. Client support remains early, with several projects developing implementations and some calendar specifications still drafts. Commenters debated the server-client adoption loop and JSON-over-HTTP efficiency.

### Comment pulse

- Bootstrap optimism → a working server gives client developers something concrete to target.
- Adoption skepticism → mainstream clients still rely on IMAP, CalDAV, and CardDAV, limiting immediate utility.
- Protocol tradeoff → HTTP and JSON ease web development, while critics prefer leaner binary designs.

### LLM perspective

- View: Protocol elegance matters only after interoperable clients turn one complete server into an ecosystem.
- Impact: Developers gain a coherent API, but operators must preserve legacy bridges during adoption.
- Watch next: Specification ratification, independent client releases, interoperability testing, and Stalwart 1.0 stability.
