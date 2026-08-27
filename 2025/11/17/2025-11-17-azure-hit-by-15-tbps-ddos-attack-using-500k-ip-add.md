# Azure hit by 15 Tbps DDoS attack using 500k IP addresses

- Score: 170 | [HN](https://news.ycombinator.com/item?id=45955900) | Link: https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/

### TL;DR

Microsoft reported that the Aisuru IoT botnet directed a 15.72Tbps, 3.64-billion-packet-per-second UDP flood from more than 500,000 IP addresses at one Azure public IP in Australia. Aisuru reportedly compromises home routers and cameras, and its minimally spoofed traffic made tracing and provider enforcement easier. The same botnet had been linked to other enormous attacks and grew after a router firmware-update server compromise infected about 100,000 devices. The report demonstrates aggregate risk from poorly secured consumer infrastructure, though several figures originate with providers and researchers involved.

### Comment pulse

- Readers questioned the economics of DDoS-for-hire attacks against gaming targets and proposed gambling or competitive motives without firm evidence.
- Discussion emphasized signed firmware updates and challenged unsupported claims that DDoS commonly distracts defenders from intrusions.

### LLM perspective

- View: The pivotal failure is scalable device compromise, not merely the bandwidth of one flood.
- Impact: One poisoned update channel can recruit consumer hardware into infrastructure-scale attacks.
- Watch next: Provider takedowns, firmware-signing practices, botnet reconstitution, and independently confirmed mitigation outcomes.
