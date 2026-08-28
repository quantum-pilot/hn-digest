# The Deletion of Docker.io/Bitnami

- Score: 348 | [HN](https://news.ycombinator.com/item?id=45048419) | Link: https://community.broadcom.com/tanzu/blogs/beltran-rueda-borrego/2025/08/18/how-to-prepare-for-the-bitnami-changes-coming-soon

### TL;DR

Broadcom says Bitnami stopped publishing new Docker Hub images and OCI Helm charts on August 28, while postponing deletion of the public catalog until September 29 and scheduling temporary brownouts. Existing artifacts move to an unsupported, temporary Legacy registry; users should mirror dependencies or migrate. Bitnami Secure Images offer hardened Photon-based builds, stable tags, support, and compliance metadata, with only some development/testing images free. Container and chart source remains Apache-licensed on GitHub. The company frames hosted builds as unsustainable; commenters sharply dispute the commercialization strategy and value.

### Comment pulse

- Users debated whether Bitnami’s packaging is modest glue or substantial maintenance work worth paying for.
- Some recommended official upstream images; others emphasized the harder problem of replacing Bitnami Helm charts.
- A reported $50,000 price was a commenter claim, not confirmed by the source.

### LLM perspective

- View: Open source availability does not guarantee continued free building, hosting, patching, or compatibility work.
- Impact: Unpinned public-registry dependencies can become sudden operational and security liabilities.
- Watch next: Inventory Bitnami pulls, mirror required digests, and test replacements before Legacy images accumulate vulnerabilities.
