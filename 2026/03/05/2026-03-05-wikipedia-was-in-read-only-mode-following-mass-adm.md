# Wikipedia was in read-only mode following mass admin account compromise

- Score: 857 | [HN](https://news.ycombinator.com/item?id=47263323) | Link: https://www.wikimediastatus.net

### TL;DR

Wikimedia placed its wikis in read-only mode on March 5 while investigating an incident, restored read-write access roughly 90 minutes later, and kept editing functions disabled while monitoring a fix. The status page gives no cause. Commenters, citing a public incident ticket, said a highly privileged staff account loaded random user scripts during testing and executed a malicious script from Russian Wikipedia, which propagated through global and user JavaScript and triggered alerts. They described vandalism and deletion routines, though one commenter said the infection affected Meta rather than Wikipedia itself.

### Comment pulse

- The alleged test design drew outrage → production scripts from strangers were loaded under a staff account able to modify globally executed CSS and JavaScript.
- Worm behavior exploited infected administrators → it hid evidence, replicated, vandalized random pages, and attempted bulk and random deletions.
- Cleanup looked manageable to some → counterpoint: normal revision history aided reverts, but the history also carried the malicious code.
