# No strcpy either

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46433029) | Link: https://daniel.haxx.se/blog/2025/12/29/no-strcpy-either/

- TL;DR  
  Curl’s maintainer describes how the project first eliminated strncpy and now bans strcpy by introducing curlx_strcopy, a helper that always receives buffer sizes and source length, memcpy’s only when safe, and otherwise zero-terminates. The motivation is long-term safety in a decades-old C codebase where distant size checks can drift from copies. Commenters debate C’s flawed NUL-terminated string APIs, performance implications of strcpy, historical constraints, and whether the new helper should return an explicit error.

- Comment pulse  
  - strcpy is not only unsafe but often slower than length-based memcpy due to bytewise scanning and unpredictable branches; many argue abandoning NUL-terminated strings entirely.  
  - C string APIs reflect 1970s constraints: fixed-size name fields, precious bytes, no fat pointers; libraries now track lengths explicitly—counterpoint: trillions shipped using C just fine.  
  - curlx_strcopy silently empties dest on overflow and returns nothing; commenters prefer explicit status codes so callers can handle errors robustly.

- LLM perspective  
  - View: Replacing strcpy/strncpy with a project-specific, length-checked helper is pragmatic hardening for huge, long-lived C codebases.  
  - Impact: Encourages other infrastructure projects to centralize string handling, easing audits, fuzzing, and static analysis of memory safety.  
  - Watch next: whether curl’s helper grows into a broader safe-string layer or is superseded by gradual adoption of safer languages.
