# How to escape the Linux networking stack

- Score: 87 | [HN](https://news.ycombinator.com/item?id=45954638) | Link: https://blog.cloudflare.com/so-long-and-thanks-for-all-the-fish-how-to-escape-the-linux-networking-stack/

### TL;DR

Cloudflare describes trying to forward packets through leased soft-unicast IP and port slices while ordinary sockets use the same space. Linux conntrack can silently rewrite a bound socket's source port after a collision, violating the assigned slice. Netlink reservations worked but were costly and fragile. Fake connected sockets created with TCP Fast Open blocked collisions, yet early demultiplexing then captured packets before custom routing. Disabling early demux had modest overhead, but terminating and proxying TCP ultimately proved simpler, observable, and fast enough; Fish now handles only ICMP.

### Comment pulse

- Readers wanted more practical documentation on namespaces, veth pairs, bridges, macvlan, and the layer-two concepts underlying container networking.
- Some expected a userspace TCP/IP stack; replies noted modern kernel async and zero-copy paths reduce that advantage.

### LLM perspective

- View: The best engineering result was abandoning a clever solution once the simpler proxy delivered operational benefits.
- Impact: Cloudflare accepts minor proxy overhead in exchange for correct address leasing and better reachability telemetry.
- Watch next: Future full-packet tunneling needs, early-demux costs at scale, and kernel support for mixed ownership.
