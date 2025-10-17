# Liquibase continues to advertise itself as "open source" despite license switch

- Score: 324 | [HN](https://news.ycombinator.com/item?id=45602676) | Link: https://github.com/liquibase/liquibase/issues/7374

- TL;DR
    Liquibase switched from Apache 2.0 to the Functional Source License (FSL), which Liquibase itself says isn’t open source, while its repo still advertised OSS. Red Hat’s Richard Fontana opened an issue; maintainers quickly PR’d updates to scrub “open source” wording. Discussion splits between “Fair Source” advocates and those citing Open Source Definition violations. Users debate the “open in two years” model, weigh forking or migrating, and question trust when vendors relicense—even as some see monetization needs as legitimate.

- Comment pulse
    - License switch is bait-and-switch → teams plan exits; cite Elastic/Terraform; alternatives: Flyway, Atlas, Sqitch, pgroll — counterpoint: fork previous versions.
    - FSL isn’t open source → violates OSD’s no‑discrimination clauses; Liquibase’s own FAQ says “No.” — counterpoint: backers seek OSI review and promote “Fair Source.”
    - Better path → use strong copyleft (AGPL) or BuSL; duration debates (2–4 years) and whether delayed-open-source protects revenue without alienating users.

- LLM perspective
    - View: License-wording matters; mislabeling erodes trust more than the switch itself; prompt correction reduces reputational damage.
    - Impact: Teams depending on Liquibase 4.x will pin, fork, or migrate; procurement/policy will scrutinize “source-available” vendors.
    - Watch next: README/website updates, OSI statements on FSL/Fair Source, forks or migrations, and whether Flyway or others change licenses.
