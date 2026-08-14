# Kubernetes on Oxide: How customer needs shaped our integrations

- Score: 153 | [HN](https://news.ycombinator.com/item?id=49286485) | Link: https://oxide.computer/blog/kubernetes-on-oxide

### TL;DR

Customer workflows drove Oxide from no supported Kubernetes integration to three provisioning paths: Rancher, Omni with Talos, and the Cluster API provider CAPOx. A shared cloud controller manager now reconciles nodes and implements LoadBalancer services by moving floating IPs between eligible workers, although users see both external and internal addresses. Storage remains incomplete: Oxide disks cannot attach or detach while an instance runs, so a native CSI driver requires full-stack hot-plug support. Meanwhile, Longhorn on local disks avoids stacking two replication layers.

### Comment pulse

- Cluster API won praise as a GitOps-friendly, Kubernetes-native alternative to third-party fleet platforms.
- Commenters requested Karpenter, Gateway API, and native load balancing; Oxide says autoscaling discussions and broader service-controller work are underway.
- Oxide targets rack-scale VM infrastructure, whereas some on-premises users prefer container-first Kubernetes directly on bare metal.

### LLM perspective

- View: Standard extension points turned each customer obstacle into a reusable provider capability instead of workflow-specific glue.
- Impact: Operators gain several cluster paths, but stateful workloads still depend on interim storage architecture and careful replication choices.
- Watch next: Disk hot-plug, the CSI release, autoscaling, external subnets, OIDC, and native load balancing.
