# Transcribe.cpp

- Score: 718 | [HN](https://news.ycombinator.com/item?id=48963879) | Link: https://workshop.cjpais.com/projects/transcribe-cpp

### TL;DR
transcribe.cpp is a new ggml-based C/C++ library for local automatic speech recognition that aims to replace whisper.cpp and fragile ONNX workflows. It unifies 16+ ASR model families behind one engine, with GPU acceleration via Vulkan, Metal, CUDA and TinyBLAS, plus streaming/batch APIs and bindings for Python, JS/TS, Rust and ObjC/Swift. Every shipped model is numerically validated and WER-tested against its reference implementation, targeting reliable, cross-platform, privacy-preserving speech-to-text on laptops, mobiles and low-power boards.

### LLM perspective
- View: A pragmatic consolidation layer for on-device ASR, closing gaps between research models and production-ready, multi-platform apps.  
- Impact: Most useful for indie devs and small teams shipping privacy-first transcription on desktops, mobiles, and embedded Linux hardware.  
- Watch next: Stability of APIs, mobile-focused benchmarks, packaging for app stores, and pace of adding new ASR families beyond Whisper descendants.
