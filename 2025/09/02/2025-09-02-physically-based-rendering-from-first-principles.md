# Physically based rendering from first principles

- Score: 288 | [HN](https://news.ycombinator.com/item?id=45106846) | Link: https://imadr.me/pbr/

- TL;DR
    - An interactive primer walks from electromagnetism and Maxwell to ray optics, then builds PBR: Snell and Fresnel-Schlick, microfacet BRDF (Cook–Torrance with GGX and Schlick-GGX), metals vs dielectrics, spectral power/reflectance and metamerism, the rendering equation, and roughness/metallic controls. HN praised the visuals but debated the “first‑principles” framing: some found Chapter 1 tangential and pedagogically risky; others liked the deeper context. Practical notes: sporadic Firefox/Android issues, monolithic WebGL/JS source shared, and calls for more spectral/wave-based extensions.

- Comment pulse
    - “First principles” labeling misleads beginners → axioms are fragile; starting at EM invites pedantry and errors, obscuring PBR goals — counterpoint: context motivates Snell/Fresnel intuitively.
    - Physics depth doesn’t map cleanly to rasterized PBR → waves-to-rays and spectral-to-RGB jumps hide assumptions; Wavetracer shows benefits of full wave optics.
    - Interactivity impressed readers → custom WebGL/JS achieved it; some Android/Firefox glitches reported; author shared an 8k-line single file and prefers handwritten code.

- LLM perspective
    - View: Interactive layering builds intuition, but anchoring early on BRDF goals and deferring deep physics would improve focus.
    - Impact: Newcomers grok roughness/metallic, Fresnel, GGX; educators get reusable demos; practitioners may critique rigor yet shareable visuals help onboarding.
    - Watch next: Add spectral rendering vs RGB, importance sampling and envmap prefiltering, plus a modular TypeScript rewrite with tests.
