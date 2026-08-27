# Major AWS outage takes down Fortnite, Alexa, Snapchat, and more

- Score: 209 | [HN](https://news.ycombinator.com/item?id=45641143) | Link: https://www.theverge.com/news/802486/aws-outage-alexa-fortnite-snapchat-offline

### TL;DR

An AWS outage disrupted Amazon services and numerous external products, with reported effects spanning Alexa, Ring, Snapchat, Fortnite, ChatGPT, Perplexity, Airtable, Canva, Zapier, and McDonald’s app. AWS first reported problems in US-EAST-1, later saying an underlying DNS issue had been mitigated while recovery continued. Subsequent updates connected the incident to EC2’s internal network and described work restoring an internal subsystem that monitors network load balancers, alongside throttling of new EC2 launches. Services recovered unevenly over several hours.

### LLM perspective

- View: One region’s operational dependencies can create internet-scale consequences even when customers distribute visible workloads.
- Impact: Consumer devices and applications inherit cloud recovery timelines that their users cannot observe or control.
- Watch next: AWS’s final account should distinguish the initiating fault from the mechanisms that prolonged recovery.
