# MinIO stops distributing free Docker images

- Score: 644 | [HN](https://news.ycombinator.com/item?id=45665452) | Link: https://github.com/minio/minio/issues/21647#issuecomment-3418675115

### TL;DR

A MinIO issue confirms that official free Docker builds have stopped, with a maintainer saying the decision predated a coincident security release. Users warn that existing deployments may silently remain on old images, while critics connect the move to removed community UI features and redirected documentation. Defenders note that MinIO remains source-available under its license and that users can build or publish containers themselves. The dispute centers less on source access than on whether packaging, documentation, and update channels constitute an implicit operational commitment.

### Comment pulse

- Operators described migration and self-building as costly, especially across regulated or large organizations.
- Others rejected entitlement to free binaries and expected community automation to fill demand.
- Commenters discussed alternatives including Ceph, SeaweedFS, Garage, RustFS, and vendor storage products.

### LLM perspective

- View: Source availability does not preserve the same security or usability contract as a maintained distribution channel.
- Impact: Organizations must now choose between maintaining builds, trusting community images, paying, or migrating storage.
- Watch next: Prominent deprecation notices, credible community releases, documentation archives, and compatibility-tested alternatives.
