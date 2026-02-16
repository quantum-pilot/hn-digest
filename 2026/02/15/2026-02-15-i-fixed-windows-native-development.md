# I fixed Windows native development

- Score: 633 | [HN](https://news.ycombinator.com/item?id=47022891) | Link: https://marler8997.github.io/blog/fixed-windows/

- TL;DR  
  The post argues that “Install Visual Studio” as a build prerequisite forces Windows C/C++ projects into huge, opaque, unreproducible toolchains. The author’s tool, msvcup, talks directly to Microsoft’s Visual Studio JSON manifests to fetch only the MSVC compiler and Windows SDK into versioned directories, then wraps them with tiny “autoenv” shims so builds can run from plain scripts and CI without vcvarsall or the VS installer. Commenters point to LTSC/unattended VS installs, cross‑platform dependency hell, and supply‑chain trust concerns.

- Comment pulse  
  Stable VS toolchains already exist → LTSC and scripted unattended installers give pinned versions for teams — counterpoint: still heavyweight, over-installs, and needs admin/GUI setup.  
  Windows isn’t uniquely cursed → Linux C/C++ and .NET have their own dependency/version hell; only glibc compatibility is usually rock solid.  
  curl-ing binaries from GitHub is risky → no hashes/signatures, unknown account — counterpoint: code is open, scripts are inspectable, author has prior Zig/Win32 work.

- LLM perspective  
  View: Treating compilers/SDKs as declarative, per-project dependencies is the right direction for native builds on all platforms.  
  Impact: Most useful for CI, cross-compiling C/C++, and teams avoiding global, admin-installed Visual Studio instances.  
  Watch next: Add signing and reproducible hashes, integrate with major build systems, and see whether Microsoft offers slimmer, manifest-driven toolchain bundles.
