# Marble Fountain

- Score: 430 | [HN](https://news.ycombinator.com/item?id=45866697) | Link: https://willmorrison.net/posts/marble-fountain/

- TL;DR
  - Will Morrison’s 3D‑printed “Marble Fountain” procedurally packs many marble tracks into a single print volume, enforcing slope, turn radii, spacing, and collision constraints. Aggressive banking intentionally bleeds rotational energy to cap speed; a ball‑screw‑like lift and particle‑system supports complete the build. OpenSCAD hits limits; a rewrite and camera‑based velocity modeling are planned. Reliability is good but imperfect (occasional losses, motor heat). HN discusses banking physics, 3D printing as the right medium, and why audio‑encoding tracks failed.

- Comment pulse
  - Reliability hinges on two-rail force balance → equal normals prevent lift-off; current build drops a ball ~30 minutes—counterpoint: camera feedback could automate tuning.
  - Encode audio via tracks → tried MIDI-to-marble and drum tests; balls jitter too much for clear pitch; softer material or larger bearings might work.
  - 3D printing shines for organic interwoven forms → complexity is “free” versus subtractive methods; otherwise fabrication would be tedious and impractical.

- LLM perspective
  - View: Procedural path solving plus aggressive banking is smart; but without physics model, tuning doesn't generalize across geometries and materials.
  - Impact: Adding dynamics, material models, and parameter sweeps could standardize reliability and enable kit-style reproducibility for exhibits and classrooms.
  - Watch next: Publish speed–curvature measurements, motor thermal headroom, and a camera-closed-loop tool to auto-adjust bank, slope, spacing.
