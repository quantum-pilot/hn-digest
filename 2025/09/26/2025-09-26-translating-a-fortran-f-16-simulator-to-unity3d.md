# Translating a Fortran F-16 Simulator to Unity3D

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45383637) | Link: https://vazgriz.com/762/f-16-flight-sim-in-unity-3d/

- TL;DR
    - An engineer ports the classic Fortran F‑16 flight model from “Aircraft Control and Simulation” into Unity, translating aerospace coordinates, US‑customary units, and lookup‑table‑driven aerodynamics. They implement an Air Data Computer, engine power lag and trilinear thrust interpolation, normal/axial force coefficients vs lift/drag, and roll/pitch/yaw moments, noting atmospheric (≤35k ft) and AOA table (−10°–45°) limits with extrapolation. HN mixes FORTRAN/SCIF and Falcon nostalgia with calls to convert everything to metric, plus nautical‑mile clarifications—and a FORmula TRANslator pun.

- Comment pulse
    - Nostalgia for FORTRAN, SCIF stories, and Falcon sims → early flight models needed 80x87; realism wowed some, bored others; Falcon BMS endures.
    - Convert everything to metric → simplifies code, consistency with Unity; fewer conversions, easier physics — counterpoint: keeping U.S. units preserves textbook constants and table fidelity.
    - Nautical mile clarification → historically one minute of latitude; modern definition fixes it to exactly 1,852 m despite Earth’s irregularity.

- LLM perspective
    - View: Preserve original tables, but guard against unit mistakes, index off-by-ones, and axis-handedness errors during conversions.
    - Impact: Accessible Unity/C# code enables more accurate indie flight sims, classroom labs, and hobby aircraft projects.
    - Watch next: Validate against wind-tunnel curves; add dynamic stall and >35k ft atmosphere; profile double precision and timestep stability.
