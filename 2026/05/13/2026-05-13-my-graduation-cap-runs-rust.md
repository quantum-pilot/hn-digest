# My graduation cap runs Rust

- Score: 208 | [HN](https://news.ycombinator.com/item?id=48116207) | Link: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/

### TL;DR

A Purdue graduate built a tassel-triggered LED display under a rented graduation cap, replacing the rejected idea of setting it on fire. A reed switch and magnet detect tassel movement, while an ATtiny85 drives 48 WS2812B LEDs from a USB-C power bank. Rust firmware took about two hours because avr-hal and ws2812-avr needed forks and patches for the chip and 16 MHz clock; hardware took more than three. He will not wear it, judging the result too tacky. Commenters agreed Rust’s extra difficulty was justified by the title.

### Comment pulse

- Readers celebrated choosing Rust chiefly to make the headline work, despite Arduino libraries being easier.
- The $94 mandatory rental drew disbelief — counterpoint: US schools vary widely, with many selling regalia or letting graduates keep caps.
- Some suggested sharing rentals across non-overlapping ceremonies or skipping commencement entirely to avoid single-use regalia costs.

### LLM perspective

- View: A constrained novelty project makes unfamiliar embedded tooling memorable and exposes ecosystem gaps.
- Impact: Published ATtiny85 patches and source lower the next builder’s cost beyond the cap’s brief demonstration.
- Watch next: Upstream chip support, power safety, reed-switch reliability, and less seizure-prone animations.
