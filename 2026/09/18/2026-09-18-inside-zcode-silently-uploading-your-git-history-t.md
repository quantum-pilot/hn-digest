# Inside ZCode: Silently uploading your Git history to the cloud

- Score: 250 | [HN](https://news.ycombinator.com/item?id=49750694) | Link: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/

### TL;DR

An investigator reports that logged-in ZCode silently archived workspaces, including Git objects, LFS caches, reflogs, and configuration, encrypted them for a server-held key, and attempted direct uploads to Aliyun OSS despite UI switches. Their 345MB commercial workspace produced a 313MB encrypted snapshot, 86.6% from .git. A translated company response shared in comments apologized, attributed uploads to default-enabled Repo Wiki generation, said cloud data was immediately destroyed, claimed the issue was fixed, and promised open sourcing and third-party review. Commenters emphasized OS-level sandboxing.

### Comment pulse

- Encryption did not provide user control → server-supplied public keys allegedly made snapshots readable by Zhipu, not their local owners.
- Disclosure and controls reportedly failed → the investigator found no effective upload toggle or policy language covering full-history snapshots.
- Agents require least privilege → commenters recommended separate accounts, narrow filesystem scopes, containers, and treating harnesses as untrusted users.

### LLM perspective

- View: A rollback feature becomes a data-governance incident when collection scope, destination, keys, and defaults are not explicit.
- Impact: Developers risk exposing deleted secrets, proprietary history, branch plans, and internal infrastructure metadata beyond current prompt context.
- Watch next: Verify the patched behavior, deletion guarantees, open-source release, independent audit, opt-in design, and exclusion of Git internals.
