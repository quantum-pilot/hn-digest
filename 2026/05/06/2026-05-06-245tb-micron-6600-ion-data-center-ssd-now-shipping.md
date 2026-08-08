# 245TB Micron 6600 ION Data Center SSD Now Shipping

- Score: 248 | [HN](https://news.ycombinator.com/item?id=48031867) | Link: https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now

### TL;DR

Micron says its 245TB 6600 ION is now shipping as the highest-capacity commercially available SSD, using G9 QLC NAND in U.2 and E3.L formats for AI, object, and file storage. Rated at up to 30W, one drive replaces roughly six 44TB hard drives by raw capacity; Micron claims an equivalent deployment needs 82% fewer racks and about half the peak power. Discussion tempered the headline with workload realities: 2.7GB/s sequential writes and modest IOPS suit dense, sustained storage rather than consumer-style bursts or latency-sensitive tiers.

### Comment pulse

- Consumer frustration centered on rising SSD prices and absent 16–32TB portable options — counterpoint: hyperscaler demand and slow fab expansion explain scarcity.
- Readers reframed 2.7GB/s writes as predictable sustained throughput; filling or restoring 245TB still takes many hours.
- Low drive-writes-per-day looked alarming until commenters converted it into tens of petabytes written over warranty life.

### LLM perspective

- Rack economics—not per-drive speed—matter most for archival, data-lake, and high-capacity object workloads.
- Operators should model rebuild time, failure domains, controller limits, and network bandwidth before consolidating so much data per device.
- Watch independent sustained-write, endurance, thermal, and mixed-workload tests against HDD arrays and competing high-capacity SSDs.
