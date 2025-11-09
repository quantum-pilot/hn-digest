# Immutable Software Deploys Using ZFS Jails on FreeBSD

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45852895) | Link: https://conradresearch.com/articles/immutable-software-deploy-zfs-jails

- TL;DR
    - The article shows how to deploy apps as immutable FreeBSD jails by cloning a ZFS snapshot per release and fronting them with Caddy health checks for zero‑downtime cutovers and instant rollbacks. It builds a base template (base.txz + freebsd-update), creates per‑commit jails, runs services via rc.d, and switches traffic by updating Caddy. HN commenters validate the approach, suggest keeping state in dedicated ZFS datasets, note VNET/interface quirks, and debate base tools vs jail managers, cautioning that ezjail is dated.

- Comment pulse
    - Roll-your-own ZFS+VNET jails work well → keep app state in a delegated “data” dataset; OS reprovisioning is trivial; interface names need careful uniqueness.
    - Clone-per-release scales and predates containers → 2007 setup used ZFS clones, VLANs, iSCSI for Xen; today prefer filesystem clones and NFS.
    - Prefer base tools over managers → use bsdinstall jail, cloned_interfaces, freebsd-update -j; ezjail is old — counterpoint: some still find ezjail useful.

- LLM perspective
    - View: ZFS snapshots + jails + health-checked proxy deliver immutable deploys without containers or Kubernetes complexity.
    - Impact: Best fit for small/medium FreeBSD shops needing safe rollbacks; reduces tooling sprawl and operational risk.
    - Watch next: Automate IP allocation and Caddy updates; compare with BastilleBSD/jailctl; measure failover latency, snapshot storage, and patching cadence.
