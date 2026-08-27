# A race condition in Aurora RDS

- Score: 180 | [HN](https://news.ycombinator.com/item?id=45929921) | Link: https://hightouch.com/blog/uncovering-a-race-condition-in-aurora-rds

### TL;DR

Hightouch reports that two manual Aurora PostgreSQL failovers reversed themselves while normal write traffic continued, leaving some applications connected to a read-only instance. Logs showed storage-runtime crashes; pausing all writers allowed the next failover to succeed. AWS attributed the failure to an internal signaling problem while demoting the old writer and recommended avoiding writes during failover until a planned fix. Commenters disputed Hightouch's dual-writer interpretation but agreed the storage layer appears to have preserved consistency despite orchestration failure.

### Comment pulse

- The apparent breadth puzzled operators → others routinely fail over write-heavy Aurora clusters without encountering this behavior.
- Hightouch's mechanism remains contested → a commenter proposed watchdog termination after state mismatch, not simultaneous accepted writes.
- Storage isolation earned praise → lower layers rejected unsafe state even when failover orchestration malfunctioned.

### LLM perspective

- View: The incident separates availability failure from data-integrity failure; Aurora appears to have sacrificed the former to preserve the latter.
- Impact: Operators must treat planned failover as write downtime despite documentation and prior staging success.
- Watch next: Track AWS's fix, clarify triggering conditions, and test client reconnection behavior under controlled write loads.
