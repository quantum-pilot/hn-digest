# AMD's random number generator can't generate a 0?

- Score: 277 | [HN](https://news.ycombinator.com/item?id=49798204) | Link: https://board.flatassembler.net/topic.php?t=24261

### TL;DR

A forum author found that 16-bit `RDRAND` and `RDSEED` calls on tested AMD processors never returned zero as a successful value, while 32- or 64-bit calls could contain zero in their low 16 bits. HN commenters reproduced the `RDRAND16` behavior on Zen 2 and proposed a narrower explanation: zero may be generated, but the carry flag is incorrectly cleared, causing conforming callers to retry. Newer Zen 4 testing did not reproduce it, so the scope and exact affected hardware remain uncertain.

### Comment pulse

- The defect appears specific to 16-bit calls → reproduced Zen 2 tests returned zero only with the failure flag cleared.
- Hardware output should not be used directly → security-sensitive applications should rely on the operating system’s mixed and conditioned randomness.
- The affected range remains unclear → one Zen 2 reproduction contrasted with a successful Zen 4 intrinsic test and unrelated AMD bulletins.

### LLM perspective

- View: This looks more like an instruction-status defect than proof that the underlying generator excludes zero.
- Impact: Correct retry logic quietly biases 16-bit output, while truncating successful wider calls avoids the observed behavior.
- Watch next: AMD should publish affected microarchitectures, root cause, microcode status, and separate findings for RDRAND and RDSEED.
