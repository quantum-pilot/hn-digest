# Oldest recorded transaction

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45149626) | Link: https://avi.im/blag/2025/oldest-txn/

- TL;DR
  - The post riffs on a 5,000-year-old Sumerian “receipt” as the most durable database, then tests modern DB limits: MySQL dates only to 1000 CE; Postgres/SQLite handle proleptic Julian dates back to 4713 BCE. This prompts how to model older or uncertain dates (e.g., museums). HN discusses writing’s accounting origins, practical “circa”/range storage, context on early logographic tablets, and a nod to Transaction Processing’s history.

- Comment pulse
  - Writing emerged from accounting → earliest tablets are tallies of goods; receipts survive because they were ubiquitous — counterpoint: survivorship bias shapes what we find.
  - Museums store uncertain dates as text/circa → reliable sorting needs ranges or uncertainty types; ISO 8601 allows year 0000 and negative years by agreement.
  - “Oldest” phrasing nitpick → say “oldest known,” since earlier records may be lost; oldest surviving example needn’t be the first.

- LLM perspective
  - View: Use proleptic calendars with explicit uncertainty intervals; avoid overloading TIMESTAMP for BCE or fuzzy dates.
  - Impact: Museums, archives, historians, and astronomy workflows gain consistency via standardized uncertain-date types and indexable range operations.
  - Watch next: ISO 8601-2 uncertainty syntax, Postgres range indexes and EXCLUSION constraints, conversion libraries across proleptic Julian/Gregorian.
