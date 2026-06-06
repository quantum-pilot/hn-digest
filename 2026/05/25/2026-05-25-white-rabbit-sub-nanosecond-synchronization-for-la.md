# White Rabbit – sub-nanosecond synchronization for large distributed systems

- Score: 187 | [HN](https://news.ycombinator.com/item?id=48245916) | Link: https://ohwr.org/projects/white-rabbit/

### TL;DR
White Rabbit is an open-hardware, Ethernet-based timing network from CERN that delivers sub-nanosecond synchronization and picosecond-level jitter across thousands of nodes spaced up to ~10 km. It combines Synchronous Ethernet, augmented PTP, and calibrated fiber-delay compensation so the physical layer clock is shared, while still carrying gigabit data. HN discussion highlights that it achieves ~10 ps jitter over tens of kilometers, pushes into relativity-measurable timing, and that precise global time doesn’t magically overcome distributed-consensus latency limits.

### Comment pulse
- White Rabbit modifies Ethernet physical/clocking for timing → all NICs lock to a shared layer-1 clock, enabling picosecond alignment while still carrying data.  
- Sub-nanosecond sync over tens of kilometers → two-way time transfer, fiber-delay calibration, temperature compensation, and local oscillators yield ~10 ps jitter.— counterpoint: assumes symmetric paths.  
- Precise shared clocks don’t bypass consensus limits → they reduce uncertainty and scheduling jitter; decision latency still bounded by signal propagation and protocol design.

### LLM perspective
- View: Treats time as a first-class network service, turning Ethernet into a deterministic timing fabric for measurement and control.  
- Impact: Lowers barrier for labs and industry to deploy picosecond-level synchronization without proprietary timing gear or separate trigger cabling.  
- Watch next: Robust 10G/100G variants, integration with TSN and PTP profiles, plus security models preventing spoofed timing in critical infrastructure.
