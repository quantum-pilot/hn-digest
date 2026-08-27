# Translating a Fortran F-16 Simulator to Unity3D

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45383637) | Link: https://vazgriz.com/762/f-16-flight-sim-in-unity-3d/

### TL;DR

Vazgriz ports a textbook F-16 flight model from Fortran into a playable Unity simulator, explaining the engineering along the way. The translation reconciles aerospace and Unity coordinate systems, U.S. customary and metric units, atmospheric calculations, lookup-table interpolation, engine thrust, aerodynamic forces and moments, damping, rigid-body integration, and a simplified PID-based flight-control system. Unit tests compare one simulation step with textbook outputs, while manual flight testing checks behavior. The author openly documents limits: restricted angle ranges, simplified controls and landing gear, and unrealistic behavior above roughly Mach 0.7.

### Comment pulse

- Readers shared memories of aerospace Fortran work and high-fidelity simulators that once required dedicated floating-point coprocessors.
- Some argued converting constants and formulas to metric once would be cleaner than repeated boundary conversions.

### LLM perspective

- View: The project succeeds as an auditable translation because it preserves reference behavior before pursuing greater realism.
- Impact: Separating the flight model from Unity physics makes legacy scientific code testable and approachable to game developers.
- Watch next: Broader aerodynamic tables, instrumented flight tests, high-lift devices, landing dynamics, and transonic modeling.
