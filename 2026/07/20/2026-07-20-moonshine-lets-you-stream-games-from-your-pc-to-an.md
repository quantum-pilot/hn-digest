# Moonshine: Lets you stream games from your PC to any device running Moonlight

- Score: 327 | [HN](https://news.ycombinator.com/item?id=48972970) | Link: https://github.com/hgaiser/moonshine

## TL;DR
Moonshine is a Rust-based, headless game-streaming server for Moonlight clients that targets Linux PCs with Vulkan-capable GPUs. It launches each game in its own isolated Wayland compositor, so your main desktop stays free and no physical monitor or dummy plug is needed. It supports hardware-accelerated H.264/H.265/experimental AV1, HDR, full input (mouse, keyboard, gamepads with haptics), and surround audio. Compared to Sunshine, it’s narrower in platform support but more focused on isolated sessions; VPN is required for safe internet use.

## LLM perspective
- View: A strong option for Linux homelab and living-room streaming where you want a “console-like” UI without tying up the desktop.  
- Impact: Encourages more Vulkan video encoder usage and Wayland-native workflows; could push GPU vendors to stabilize AV1 drivers faster.  
- Watch next: Windows/BSD support, better remote security layers than “VPN only,” and performance benchmarks vs Sunshine and proprietary solutions.
