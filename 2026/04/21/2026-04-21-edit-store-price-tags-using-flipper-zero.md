# Edit store price tags using Flipper Zero

- Score: 268 | [HN](https://news.ycombinator.com/item?id=47822978) | Link: https://github.com/i12bp8/TagTinker

### TL;DR

TagTinker is a GPL-licensed Flipper Zero application for studying infrared electronic shelf-label protocols on owned or explicitly authorized hardware. It supports addressed-frame analysis, signal and response tests, monochrome payload preparation, and controlled text, image, or test-pattern display experiments. The project adapts earlier reverse-engineering work but deliberately omits deployment instructions and forbids retail use, price changes, control bypasses, and interference. Its source-first release must be built locally, and the maintainer warns that removing some tags’ batteries can erase volatile configuration and leave them unresponsive without the original base station.

### Comment pulse

- Retail veterans were surprised by unsecured one-way IR, but noted its low power, low cost, and operational simplicity.
- Several argued altered displays do not change checkout prices and resemble swapping paper labels more than compromising a pricing database.
- Others called the risk dangerous — counterpoint: fraudulently altered labels generally need not be honored, and tampering remains detectable and illegal.

### LLM perspective

- Security should match impact: display authenticity matters even when checkout systems remain authoritative.
- Cheap, flexible tags externalize abuse detection to cameras, staff, and reconciliation processes.
- Open research can expose weak protocols while enabling legitimate interoperability and home-display reuse.
