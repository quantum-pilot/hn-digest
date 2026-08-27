# Apple Photos app corrupts images

- Score: 1069 | [HN](https://news.ycombinator.com/item?id=45274277) | Link: https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/

### TL;DR

A photographer reports rare, apparently random file corruption when importing OM System camera images into Apple Photos. After replacing cables, SD card, laptop, and camera, the problem persisted. Keeping originals revealed one file that was intact on the card but altered after import; its size matched while its checksum and bytes differed, and re-importing succeeded. The author estimates losing 30% of one wedding shoot but lacks reproducible steps or proof of the precise cause. They now import through Darktable and delay formatting cards.

### Comment pulse

- Commenters suspect an import-pipeline race, but others say camera USB behavior or transfer hardware remains insufficiently isolated.
- Photographers strongly advise copying, verifying, and backing up originals before deleting or formatting a memory card.

### LLM perspective

- View: The preserved source and differing checksum establish corruption somewhere in that import path, not conclusively inside Photos itself.
- Impact: A rare silent integrity failure becomes catastrophic when “delete after import” removes the only trustworthy copy.
- Watch next: A reproducible transfer case, card-reader comparison, Apple bug investigation, and end-to-end checksum verification during imports.
